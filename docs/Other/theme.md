---
parent: Other
permalink: /code
---


# Jekyll Theme - Cheat sheet
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Table of contents

```
## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---
```

## Labels
Default label
{: .label }

```
Default label
{: .label }
```

Blue label
{: .label .label-blue }

```
Blue label
{: .label .label-blue }
```

Green label
{: .label .label-green }

```
Green label
{: .label .label-green }
```

Purple label
{: .label .label-purple }

```
Purple label
{: .label .label-purple }
```

Yellow label
{: .label .label-yellow }

```
Yellow label
{: .label .label-yellow }
```

Red label
{: .label .label-red }

```
Red label
{: .label .label-red }
```




## Callouts

{: .highlight-title }
> Yellow
> 
> Text here

```
{: .highlight-title }
> Yellow
> 
> Text here
```

{: .important-title }
> Blue
> 
> Text here

```
{: .important-title }
> Blue
> 
> Text here
```


{: .new-title }
> Green
> 
> Text here

```
{: .new-title }
> Green
> 
> Text here
```


{: .note-title }
> Violet
> 
> Text here

```
{: .note-title }
> Violet
> 
> Text here
```


{: .warning-title }
> Red
> 
> Text here

```
{: .warning-title }
> Red
> 
> Text here
```



## Buttons

[Grey button](https://just-the-docs.com){: .btn }
[Purple button](https://just-the-docs.com){: .btn .btn-purple }
[Blue button](https://just-the-docs.com){: .btn .btn-blue }
[Green button](https://just-the-docs.com){: .btn .btn-green }
[White button](https://just-the-docs.com){: .btn .btn-outline }

```
[Grey button](https://just-the-docs.com){: .btn }
[Purple button](https://just-the-docs.com){: .btn .btn-purple }
[Blue button](https://just-the-docs.com){: .btn .btn-blue }
[Green button](https://just-the-docs.com){: .btn .btn-green }
[White button](https://just-the-docs.com){: .btn .btn-outline }
```


## Misc

### Comment

```
{ % comment % }
    COMMENT HERE
{ % endcomment % }
```

### New page header

```
---
parent: Other
---

# Title of the page
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## First topic
```

### Resize and center images

`{: .image90 }`
`{: .image80 }`
`{: .image70 }`
`{: .image60 }`
`{: .image50 }`
`{: .image40 }`
`{: .image30 }`