"""Social cards (1200x630, the picture LinkedIn shows when an article is shared).
Each card: the section (icon + name), the title, and the author line. Rendered by headless Chrome,
saved as JPEG in assets/2026/social/<slug>.jpg, and `image:` added to the article's front matter.
Articles with their own `image:` are left alone; --force redraws the cards already in assets/2026/social
(after a title change). Needs Pillow (pip install pillow) and Chrome.
Usage: python -X utf8 scripts/make_social_cards.py . [--force] [--only-html]"""
import html, os, re, subprocess, sys

from PIL import Image

repo = os.path.abspath(sys.argv[1])
here = os.path.join(os.environ.get('TEMP', '.'), 'lazysnail-cards')
os.makedirs(here, exist_ok=True)
chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
out_dir = os.path.join(repo, 'assets', '2026', 'social')
os.makedirs(out_dir, exist_ok=True)


def file_url(p):
    return 'file:///' + p.replace('\\', '/')


# Sections: category -> (label, key)
sections = {}
cur_key = None
in_cats = False
for line in open(os.path.join(repo, '_data', 'sections.yml'), encoding='utf-8'):
    m = re.match(r'- key: (\S+)', line)
    if m:
        cur_key, in_cats = m.group(1), False
        continue
    if line.strip() == 'categories:':
        in_cats = True
        continue
    m = re.match(r'    ([^:]+): (.+)', line)
    if in_cats and m:
        sections[m.group(1).strip()] = (m.group(2).strip().strip('"'), cur_key)

# Icons: the inner SVG of each case of section-icon.html
icon_src = open(os.path.join(repo, '_includes', 'section-icon.html'), encoding='utf-8').read()
icons = {}
for m in re.finditer(r'\{%- when ([^%]+?) -%\}\n(.*?)\n(?=\{%-)', icon_src, re.S):
    for key in re.findall(r'"([^"]+)"', m.group(1)):
        icons[key] = m.group(2)

font = file_url(os.path.join(repo, 'assets', 'fonts', 'inter-latin-wght-normal.woff2'))
portrait = file_url(os.path.join(repo, 'assets', '2026', 'site', 'arnaud-cartoon.jpg'))

TEMPLATE = """<!doctype html><html><head><meta charset="utf-8"><style>
@font-face {{ font-family: Inter; src: url("{font}") format("woff2"); font-weight: 100 900; }}
html, body {{ margin: 0; width: 1200px; height: 630px; overflow: hidden; background: #fff; }}
body {{ font-family: Inter, "Segoe UI", sans-serif; color: #1d1d1f; -webkit-font-smoothing: antialiased; }}
.card {{ box-sizing: border-box; width: 1200px; height: 630px; padding: 70px 84px 64px; display: flex; flex-direction: column; }}
.section {{ display: flex; align-items: center; gap: 18px; color: #6e6e73; font-size: 28px; font-weight: 600; }}
.tile {{ width: 64px; height: 64px; border-radius: 16px; background: #f5f5f7; display: grid; place-items: center; }}
.tile svg {{ width: 34px; height: 34px; }}
h1 {{ margin: 46px 0 0; font-size: 64px; line-height: 1.1; font-weight: 700; letter-spacing: -0.025em;
      }}
.foot {{ margin-top: auto; display: flex; align-items: center; gap: 22px; padding-top: 28px; border-top: 2px solid #e5e5ea; }}
.foot img {{ width: 72px; height: 72px; border-radius: 50%; object-fit: cover; object-position: center top; background: #f5f5f7; }}
.who {{ display: flex; flex-direction: column; gap: 4px; }}
.who b {{ font-size: 28px; font-weight: 600; }}
.who span {{ font-size: 22px; color: #6e6e73; }}
.site {{ margin-left: auto; font-size: 26px; font-weight: 600; color: #0066cc; }}
</style></head><body><div class="card">
<div class="section"><span class="tile"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">{icon}</svg></span>{section}</div>
<h1 id="t">{title}</h1>
<div class="foot"><img src="{portrait}" alt=""><div class="who"><b>Arnaud Gastelblum</b><span>Data Architect, Microsoft Fabric &amp; Power BI</span></div><span class="site">lazysnail.net</span></div>
</div><script>
var t = document.getElementById('t'), size = 64;
while (t.offsetHeight > size * 1.1 * 3 + 4 && size > 40) {{ size -= 2; t.style.fontSize = size + 'px'; }}
</script></body></html>"""

done = []
for root, dirs, files in os.walk(os.path.join(repo, 'docs')):
    for f in files:
        if not f.endswith('.md'):
            continue
        path = os.path.join(root, f)
        raw = open(path, 'rb').read().decode('utf-8')
        m = re.match(r'---\r?\n(.*?)\r?\n---', raw, re.S)
        if not m:
            continue
        fm = m.group(1)
        own = re.search(r'^image:\s*(\S+)', fm, re.M)
        if not re.search(r'^date:', fm, re.M):
            continue
        if own and not ('--force' in sys.argv and own.group(1).startswith('/assets/2026/social/')):
            continue
        title = re.search(r'^title:\s*(.+?)\s*$', fm, re.M).group(1).strip().strip('"\'')
        cat = re.search(r'^categories:\s*(.+?)\s*$', fm, re.M).group(1).strip().strip('"\'')
        label, key = sections.get(cat, ('Article', 'other'))
        slug = re.sub(r'[^a-z0-9]+', '-', os.path.splitext(f)[0][11:].lower()).strip('-')
        page = os.path.join(here, slug + '.html')
        open(page, 'w', encoding='utf-8').write(TEMPLATE.format(
            font=font, portrait=portrait, icon=icons.get(key, ''), section=html.escape(label), title=html.escape(title)))
        done.append((path, slug, page, raw, m))

if '--only-html' in sys.argv:
    print(len(done), 'cards written as HTML in', here)
    sys.exit()

for path, slug, page, raw, m in done:
    png = os.path.join(here, slug + '.png')
    subprocess.run([chrome, '--headless=new', '--hide-scrollbars', '--allow-file-access-from-files',
                    '--force-device-scale-factor=1', '--window-size=1200,630', '--virtual-time-budget=2000',
                    '--screenshot=' + png, file_url(page)], capture_output=True)
    jpg = os.path.join(out_dir, slug + '.jpg')
    Image.open(png).convert('RGB').crop((0, 0, 1200, 630)).save(jpg, 'JPEG', quality=86, optimize=True, progressive=True)
    if not re.search(r'^image:', m.group(1), re.M):
        nl = '\r\n' if '\r\n' in m.group(1) else '\n'
        fm_new = m.group(1) + nl + 'image: /assets/2026/social/' + slug + '.jpg'
        new = raw[:m.start(1)] + fm_new + raw[m.end(1):]
        open(path, 'wb').write(new.encode('utf-8'))
    print(f"{os.path.getsize(jpg) // 1024:4d} KB  {slug}")
print(len(done), 'cards')
