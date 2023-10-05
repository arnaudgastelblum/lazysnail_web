---
layout: post
title: SSIS - Export SSIS Catalog Environments
date: 2018-10-26 16:00:37.000000000 +02:00
categories: "SQL-Server"
tags: [other, sql-server]
comments: true
permalink: "/en/ssis-backup-ssis-catalog-environments/"
parent: SQL Server
---
# {{ page.title }}
{: .fs-9 }

<p><!-- wp:paragraph --></p>
<p><strong>You need to:</strong></p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:list --></p>
<ul>
<li><strong>Export your SSIS Environments (Variables)</strong></li>
<li><strong>Replicate it on your new server</strong></li>
<li><strong>Assign these variables to your new project</strong></li>
</ul>
<p><!-- /wp:list --></p>
<p><!-- wp:paragraph --></p>
<p>SSIS Catalog is not complex, but we don’t really want to spend our time to copy manually our configuration from one server to another one.<br />Often, we don’t have access to the production environment.<br />The SQL Code below helps you to create a script and automate all these very ennuying steps.</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p>I found the base line of this code on internet:&nbsp;<a href="http://www.sqlservercentral.com/articles/Integration+Services+(SSIS)/135173/">http://www.sqlservercentral.com/articles/Integration+Services+(SSIS)/135173/</a><br /><strong>Jeff Jordan</strong>&nbsp;did a really nice work.</p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:paragraph --></p>
<p><strong>His code&nbsp;helps you to:</strong></p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:list --></p>
<ul>
<li><em>Create your SSIS Catalog folder</em></li>
<li><em>Create your SSIS Environment</em></li>
<li><em>Add SSIS Variables in your SSIS Environment</em></li>
</ul>
<p><!-- /wp:list --></p>
<p><!-- wp:paragraph --></p>
<p><strong>I added some extra steps:</strong></p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:list --></p>
<ul>
<li><em>Assign your SSIS Environment to your SSIS Project</em></li>
<li><em>Assign your SSIS Environment Variables to your SSIS Project Variables</em></li>
<li><em>+ Some correction</em></li>
<li><em>+ A super nice ASCII message when everything is done.. Who can help you to have a smile and maybe a better life. (You should trust the power of smiling&nbsp;&nbsp;)</em></li>
</ul>
<p><!-- /wp:list --></p>
<p><!-- wp:paragraph --></p>
<p><strong>How does it works?</strong></p>
<p><!-- /wp:paragraph --></p>
<p><!-- wp:list {"ordered":true} --></p>
<ol>
<li>Copy the SQL Script below and paste it into a new blank query in SSMS (Management studio) –> Connected to your existing server (The server who has your environment already configured / Not the new one)</li>
<li>Configuration: Change the <em><strong>XXXX</strong> </em>value in the query
<ol>
<li><strong>@folder </strong>: Folder Name (Your configured server)</li>
<li><strong>@env </strong>: Environment Name (Your configured server)</li>
<li><strong>@destination_folder_name</strong> : Folder Name (Your new server)</li>
<li><strong>@destination_environment_name </strong>: Environment Name (Your new server)</li>
<li><strong>@destination_project_name </strong>: Project Name (Your new server)</li>
</ol>
</li>
<li>Run your query and copy the result into a new blank query in SSMS. –> Connected to your new server</li>
<li><strong>FIRST OF ALL: You should deploy your SSIS Project!!</strong> With the Deployment wizard or Visual Studio</li>
<li>Change the configuration information into the generated query</li>
<li>Run the query</li>
<li>Smile </li>
</ol>


## SQL Code

```
-- Backup / Restore SSIS Catalog Environments
--
--http://www.sqlservercentral.com/articles/Integration+Services+(SSIS)/135173/


SET NOCOUNT ON;
     
DECLARE 

        -- ---------------------------------------------------------------------------
        --     Configuration
        -- ---------------------------------------------------------------------------


        -- --------
        --  Current environment (For extraction)
        -- 
        @folder                       sysname  = 'XXXXX',
        @env                          sysname  = 'XXXXX',

        -- --------
        -- Destination environment (For Deployment)
        --
        @destination_folder_name      sysname = N'XXXXX',    -- Folder (SSIDB >> "FolderName")
        @destination_environment_name sysname = N'XXXXX',    -- Environment Name
        @destination_project_name     sysname = N'XXXXX',    -- Project Name
        

        -- ---------------------------------------------------------------------------
        --  End Configuration
        -- ---------------------------------------------------------------------------


        @project_id         int,
        @reference_location char(1),
        @folder_description nvarchar(1024),
        @sql                varchar(max) = '',
        @name               sysname,
        @cr                 char(1) = char(10),
        @tab                char(4) = SPACE(4),
        @ver                nvarchar(128) = CAST(serverproperty('ProductVersion') AS nvarchar);

SET @ver = CAST(SUBSTRING(@ver, 1, CHARINDEX('.', @ver) - 1) as int);       
IF (@ver &lt; 11)
BEGIN
        RAISERROR ('This procedure is not supported on versions prior SQL 2012', 16, 1) WITH NOWAIT;
END;
IF NOT EXISTS(SELECT TOP 1 1 FROM sys.databases WHERE name = 'SSISDB')
BEGIN
        RAISERROR('The SSISDB database does not exist on this server', 16, 1) WITH NOWAIT;
END;

/* TO DO - get the folder, environment description-*/
SET @sql = '/*------------------------------------------------------------------------------------------' + @cr;
SET @sql += @tab + 'This script creates a script to generate and SSIS Environment and its variables.' + @cr;
SET @sql += @tab + 'Replace the necessary entries to create a new envrionment' + @cr;
SET @sql += @tab + '***NOTE: variables marked as sensitive have their values masked with ''''.' + @cr;
SET @sql += @tab + @tab + 'These values will need to be replace with the actual values' + @cr;
SET @sql += '------------------------------------------------------------------------------------------*/' + @cr +@cr;
SET @sql += 'DECLARE @ReturnCode INT=0, @folder_id bigint' + @cr + @cr;       
SET @sql += '-- ---------------------------------------------' + @cr;
SET @sql += '--'+ @tab + 'Variable declarations, make any changes here' + @cr;
SET @sql += '-- ---------------------------------------------' + @cr;
SET @sql += 'DECLARE '+ @cr;
SET @sql += @tab + @tab + ' @folder  sysname  = ''' + @destination_folder_name + '''   /* this is the name of the new folder you want to create */'  + @cr;
SET @sql += @tab + @tab + ',@env     sysname  = ''' + @destination_environment_name + '''   /* this is the name of the new environment you want to create */' + @cr;
SET @sql += @tab + @tab + ',@project sysname = ''' + @destination_project_name + '''   /* this is the name of the new project you want to create */' + @cr;
       
PRINT @sql;

/*
        Generate the variable declarations at the "top" this makes it easier to replace/update the values
        The variable names here map to the name of the variable being created
*/

IF OBJECT_ID('tempdb..#env_var') IS NOT NULL DROP TABLE #env_var
IF OBJECT_ID('tempdb..#cmd')     IS NOT NULL DROP TABLE #cmd

-- ---------------------------------------------
--  Create Variables Declaration
-- ---------------------------------------------
    SELECT 
            [env_var] = 
                    @tab + @tab + ',@' + LEFT(ev.name +'                                                                 ', CASE WHEN( LEN(ev.name) >= 40 ) THEN LEN(ev.name) ELSE 40 END ) + ' '  
                    + CASE WHEN( ev.base_data_type = 'nvarchar' )
                        THEN ev.base_data_type +'(600) '
                        ELSE ev.base_data_type
                        END + '= N''' + ISNULL(CONVERT(varchar(max), ev.value), '') + ''''
                    , [name] = ev.name
    INTO #env_var
    FROM       [SSISDB].[catalog].[folders] f        
    INNER JOIN [SSISDB].[catalog].[environments]            e ON f.folder_id =  e.folder_id        
    INNER JOIN [SSISDB].[internal].[environment_variables] ev ON e.environment_id = ev.environment_id    
    WHERE 
            (f.name = @folder) 
        AND (e.name = @env)
    ;

/*
        Yes, I am looping here.  We don't know how many variables, sql_variant can be up to 8,000 bytes for the base type
        and don't want to be limited trying to print varchar(max) to the output window
        ... so we're going to print them one at a time
*/
WHILE EXISTS (SELECT TOP 1 1 FROM #env_var)
BEGIN
        SELECT TOP 1 @sql = env_var, @name = name FROM #env_var ORDER BY name;
        PRINT @sql;
        DELETE FROM #env_var WHERE name = @name;
END;

SET @sql = ';' + @cr + '/* Starting the transaction */' + @cr;
SET @sql += 'BEGIN TRANSACTION' + @cr;                  
SET @sql += @tab + 'IF NOT EXISTS (SELECT 1 FROM [SSISDB].[catalog].[folders] WHERE name = @folder)' + @cr;
SET @sql += @tab + 'BEGIN' + @cr;
SET @sql += @tab + @tab + 'RAISERROR(''Creating folder: %s ...'', 10, 1, @folder) WITH NOWAIT;' + @cr;
SET @sql += @tab + @tab + 'EXEC @ReturnCode = [SSISDB].[catalog].[create_folder] @folder_name=@folder, @folder_id=@folder_id OUTPUT' + @cr;
SET @sql += @tab + @tab + 'IF (@@ERROR &lt;> 0 OR @ReturnCode &lt;> 0) GOTO QuitWithRollback;' + @cr;
SET @sql += @tab + 'END' + @cr + @cr;   
SET @sql += @tab + 'RAISERROR(''Creating Environment: %s'', 10, 1, @env) WITH NOWAIT;' + @cr;
SET @sql += @tab + 'EXEC @ReturnCode = [SSISDB].[catalog].[create_environment] @folder_name=@folder, @environment_name=@env'  + @cr;
SET @sql += @tab + 'IF (@@ERROR &lt;> 0 OR @ReturnCode &lt;> 0) GOTO QuitWithRollback;' + @cr + @cr;
SET @sql += @tab +'-- ------------------------------------------    '+ @cr  
SET @sql += @tab + '--    Variable creation' + @cr;
SET @sql += @tab +'-- ------------------------------------------    '+ @cr  
PRINT @sql;


-- ---------------------------------------------
-- Generate the variable creation
-- ---------------------------------------------
SELECT [cmd] = @tab + 'RAISERROR(''   Creating variable: ' + ev.name + ' ...'', 10, 1) WITH NOWAIT;' + @cr
                                + @tab + 'EXEC @ReturnCode = [SSISDB].[catalog].[create_environment_variable]' + @cr
                                + @tab + @tab + '@variable_name=N''' + ev.name + '''' + @cr
                                + @tab + @tab + ', @sensitive=' + CONVERT(varchar(2), ev.sensitive) + @cr
                                + @tab + @tab + ', @description=N''' + ev.[description] + '''' + @cr
                                + @tab + @tab + ', @environment_name=@env' + @cr
                                + @tab + @tab + ', @folder_name=@folder' + @cr
                                + @tab + @tab + ', @value=@' + ev.name + @cr
                                + @tab + @tab + ', @data_type=N''' + ev.type + '''' + @cr
                                + @tab + 'IF (@@ERROR &lt;> 0 OR @ReturnCode &lt;> 0) GOTO QuitWithRollback;' + @cr
                        , [name] = ev.name
INTO #cmd
FROM [SSISDB].[catalog].[folders] f        
INNER JOIN [SSISDB].[catalog].[environments] e ON f.folder_id =  e.folder_id        
INNER JOIN [SSISDB].[catalog].[environment_variables] ev ON e.environment_id = ev.environment_id    
WHERE (f.name = @folder) AND (e.name = @env);

/*Print out the variable creation procs */
WHILE EXISTS (SELECT TOP 1 1 FROM #cmd)
BEGIN
        SELECT TOP 1 @sql = cmd, @name = name FROM #cmd ORDER BY name;
        PRINT @sql;
               
        DELETE FROM #cmd WHERE name = @name;
END;






-- ------------------------------------------
-- Set Environment to Project
-- ------------------------------------------


SET @sql = 'RAISERROR(''Configure Project: %s ...'', 10, 1, @project) WITH NOWAIT;' + @cr + @cr

SET @sql += '-- ------------------------------------------    '+ @cr
SET @sql += '-- Set Environment to Project  '                  + @cr
SET @sql += '-- ------------------------------------------    '+ @cr
SET @sql += 'RAISERROR(''   Set Environment (%s) as Reference ...'', 10, 1, @env) WITH NOWAIT;' + @cr
SET @sql += 'DECLARE @reference_id AS BIGINT'+ @cr
SET @sql += 'EXEC SSISDB.catalog.create_environment_reference'+ @cr
SET @sql += @tab + @tab + '@folder_name      = @folder,      -- Folder (SSIDB >> "FolderName")'+ @cr
SET @sql += @tab + @tab + '@environment_name = @env,         -- Environment Name              '+ @cr
SET @sql += @tab + @tab + '@project_name     = @project,     -- Project Name                  '+ @cr
SET @sql += @tab + @tab + '@reference_type   = ''R'','+ @cr
SET @sql += @tab + @tab + '@reference_id     = @reference_id OUTPUT'+ @cr

PRINT @SQL



-- ------------------------------------------
-- Set Environment Variable to Project Variables
-- ------------------------------------------


IF OBJECT_ID('tempdb..#cmd2')     IS NOT NULL DROP TABLE #cmd2

SET @sql  = '-- ------------------------------------------    '+ @cr
SET @sql += '-- Set Environment Variable to Project Variables '+ @cr
SET @sql += '-- ------------------------------------------    '+ @cr
PRINT @sql


-- -----------------
-- OLD
--  -> Assign only project variables (From environment to project variables)
--SELECT 
--     [cmd] =     
--          'RAISERROR(''   Set Project variable ('+ ev.name  +') ...'', 10, 1) WITH NOWAIT;' + @cr
--        + 'EXECUTE [SSISDB].[catalog].set_object_parameter_value '+ @cr
--        + @tab + @tab + '@object_type     = 20,' + @cr
--        + @tab + @tab + '@folder_name     = @folder,                    -- Folder (SSIDB >> "FolderName")'+ @cr
--        + @tab + @tab + '@project_name    = @project,             -- Environment Name'+ @cr
--        + @tab + @tab + '@parameter_name  = N'''+ ev.name +''',  -- Project Variable Name'+ @cr
--        + @tab + @tab + '@parameter_value = N'''+ ev.name +''',  -- Environment Variable Name'+ @cr
--        + @tab + @tab + '@object_name     = N'''','+ @cr
--        + @tab + @tab + '@value_type      = ''R'''+ @cr
--    ,[name] = ev.name
--    INTO #cmd2
--    FROM [SSISDB].[catalog].[folders] f        
--    INNER JOIN [SSISDB].[catalog].[environments] e ON f.folder_id =  e.folder_id        
--    INNER JOIN [SSISDB].[catalog].[environment_variables] ev ON e.environment_id = ev.environment_id    
--    WHERE (f.name = @folder) AND (e.name = @env);


   SELECT 
     [cmd] =     
          'RAISERROR(''   Set Project variable ('+ op.parameter_name  +') ...'', 10, 1) WITH NOWAIT;'   + @cr
        + 'EXECUTE [SSISDB].[catalog].set_object_parameter_value '                                               + @cr
        + @tab + @tab + '@object_type     = '+ CONVERT(NVARCHAR(5), op.object_type) +','                                               + @cr
        + @tab + @tab + '@folder_name     = @folder,                    -- Folder (SSIDB >> "FolderName")'       + @cr
        + @tab + @tab + '@project_name    = @project,                   -- Environment Name'                     + @cr
        + @tab + @tab + '@parameter_name  = N'''+ op.parameter_name +''',  -- Project Variable Name'    + @cr
        + @tab + @tab + '@parameter_value = N'''+ op.referenced_variable_name +''',  -- Environment Variable Name'+ @cr
        + @tab + @tab + '@object_name     = N'''+ CASE WHEN op.object_name &lt;> @env THEN op.object_name ELSE '' END       +''','                                                                                                   + @cr
        + @tab + @tab + '@value_type      = ''R'''                                                               + @cr
      ,[name] = op.parameter_name
    INTO #cmd2
    FROM         SSISDB.catalog.folders
      INNER JOIN SSISDB.catalog.projects              ON projects.folder_id          = folders.folder_id
      INNER JOIN SSISDB.catalog.object_parameters op  ON op.project_id               = projects.project_id
      --INNER JOIN SSISDB.catalog.environment_variables ON environment_variables.name  = op.parameter_name
      --INNER JOIN SSISDB.catalog.environments          ON 
      --                                                      environments.environment_id = environment_variables.environment_id
      --                                                  AND environments.folder_id      = folders.folder_id 
    WHERE 
            folders.name      = @folder
        --AND environments.name = @env
        AND projects.name     = @env
        AND op.referenced_variable_name IS NOT NULL


/*Print out the variable creation procs */
WHILE EXISTS (SELECT TOP 1 1 FROM #cmd2)
BEGIN
        SELECT TOP 1 @sql = cmd, @name = name FROM #cmd2 ORDER BY name;
        PRINT @sql;
               
        DELETE FROM #cmd2 WHERE name = @name;
END;


/* finsih the transaction handling */
SET @sql = 'COMMIT TRANSACTION' + @cr;
--SET @sql += 'RAISERROR(N''Complete!'', 10, 1) WITH NOWAIT;' + @cr;

SET @sql += 'RAISERROR(N'' _____                       _      _           _ _ '', 10, 1) WITH NOWAIT;' + @cr;
SET @sql += 'RAISERROR(N''/  __ \                     | |    | |         | | |'', 10, 1) WITH NOWAIT;' + @cr;
SET @sql += 'RAISERROR(N''| /  \/ ___  _ __ ___  _ __ | | ___| |_ ___  __| | |'', 10, 1) WITH NOWAIT;' + @cr;
SET @sql += 'RAISERROR(N''| |    / _ \| ''''_ ` _ \| ''''_ \| |/ _ \ __/ _ \/ _` | |'', 10, 1) WITH NOWAIT;' + @cr;
SET @sql += 'RAISERROR(N''| \__/\ (_) | | | | | | |_) | |  __/ ||  __/ (_| |_|'', 10, 1) WITH NOWAIT;' + @cr;
SET @sql += 'RAISERROR(N'' \____/\___/|_| |_| |_| .__/|_|\___|\__\___|\__,_(_)'', 10, 1) WITH NOWAIT;' + @cr;
SET @sql += 'RAISERROR(N''                      | |                           '', 10, 1) WITH NOWAIT;' + @cr;
SET @sql += 'RAISERROR(N''                      |_|                           '', 10, 1) WITH NOWAIT;' + @cr;

SET @sql += 'GOTO EndSave' + @cr + @cr;
SET @sql += 'QuitWithRollback:' + @cr;
SET @sql += 'IF (@@TRANCOUNT > 0) ROLLBACK TRANSACTION' + @cr;
SET @sql += 'RAISERROR(N''Variable creation failed'', 16,1) WITH NOWAIT;' + @cr + @cr;
SET @sql += 'EndSave:' + @cr;
SET @sql += 'GO';
       
PRINT @sql;
```
