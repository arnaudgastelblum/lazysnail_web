---
layout: post
title: SSIS - Create Environment from Packages variables
date: 2019-08-02 10:09:06.000000000 +02:00
categories: "SQL-Server"
tags: [other, sql-server]
comments: true
permalink: "/en/ssis-create-environment-from-packages-variables-2/"
parent: SQL Server
---
# {{ page.title }}
{: .fs-9 }

I created this script to automate some "not funny" tasks with our SSIS Catalog. If you have several SSIS projects configured <strong>in project mode</strong> (with a project.params file), when deploy them on your servers you unfortunately have to manually create the different environments.
After deploying SSIS packages, you can run the following query and use the generated SQL code.
the generated SQL script:
<ul>
<li><strong><em>Create the different environment (Based on the name of the projects)</em></strong></li>
<li><strong><em>Create variables with default values (value available in packages)</em></strong></li>
<li><strong><em>Assigning Environments to Projects</em></strong></li>
<li><strong><em>Assign the environment variables to the project variables.</em></strong></li>
</ul>


<h2>The following code is not clean, but it does the work! :)</h2>
<ul></ul>



```
USE SSISDB;
SET NOCOUNT ON;
-------------------
-- Configuration
-------------------
DECLARE @FolderToExport VARCHAR(50) = 'BI' 
DECLARE
    @folder_id          INT
   ,@name               VARCHAR(150)
   ,@project_id         INT
   ,@sql                VARCHAR(MAX) = ''
   ,@sqlTemp            VARCHAR(MAX) = ''
   ,@cr                 CHAR(1) = CHAR(10)
   ,@tab                CHAR(4) = SPACE(4)
   ,@ProjectName        VARCHAR(50)
   ,@VariableName       VARCHAR(150)
   ,@Value              VARCHAR(600)
SET @sql = '';
SET @sql += 'DECLARE @ReturnCode INT=0, @folder_id bigint' + @cr + @cr;
SET @sql += '-- ---------------------------------------------' + @cr;
SET @sql += '--'+ @tab + 'Variable declarations, make any changes here' + @cr;
SET @sql += '-- ---------------------------------------------' + @cr;
SET @sql += 'DECLARE '+ @cr;
SET @sql += @tab + @tab + ' @folder  sysname' + @cr;
SET @sql += @tab + @tab + ',@env     sysname' + @cr;
SET @sql += @tab + @tab + ',@project sysname;' + @cr;
-- Get Folder ID
SELECT @folder_id = folder_id FROM [internal].[folders] WHERE name = @FolderToExport
PRINT @SQL;
SET @SQL = '';
---------------------------------------------
-- Export Current package Configuration
---------------------------------------------
DECLARE db_cursor_variable CURSOR FOR
  SELECT DISTINCT
     CONVERT(NVARCHAR(50),  projects.name                    )      AS ProjectName
    ,CONVERT(NVARCHAR(150), projects.name  +'__'+ parameter_name)   AS VariableName
    ,CONVERT(NVARCHAR(600), ISNULL(design_default_value, '')             )      AS Value
    FROM        internal.object_parameters main
    INNER JOIN  internal.projects                 ON main.project_id = projects.project_id
WHERE project_version_lsn = (SELECT MAX(project_version_lsn) FROM [SSISDB].[internal].[object_parameters] s WHERE s.project_id = main.project_id)
  AND parameter_name NOT LIKE 'CM.%'
  AND projects.folder_id = @folder_id
   ORDER BY  CONVERT(NVARCHAR(50),  projects.name                    )
            ,CONVERT(NVARCHAR(150), projects.name  +'__'+ parameter_name)
            ,CONVERT(NVARCHAR(600), ISNULL(design_default_value, ''))   
OPEN db_cursor_variable
FETCH NEXT FROM db_cursor_variable
INTO
      @ProjectName
     ,@VariableName
     ,@Value
WHILE @@FETCH_STATUS = 0
BEGIN 
    PRINT 'DECLARE @'+ @VariableName +' NVARCHAR(600) = N'''+ @Value +''';';
    FETCH NEXT FROM db_cursor_variable
    INTO
          @ProjectName
         ,@VariableName
         ,@Value
END 
CLOSE db_cursor_variable
DEALLOCATE db_cursor_variable 
SET @SQL += 'SET @folder = '''+ @FolderToExport +''''+ @cr + @cr+ @cr;
-- Begin transaction
SET @sql += ';' + @cr + '/* Starting the transaction */' + @cr;
SET @sql += 'BEGIN TRANSACTION' + @cr + @cr + @cr;                  
----
---- Test if folder exist -> If not create it
--SET @sql += @tab + 'IF NOT EXISTS (SELECT 1 FROM [SSISDB].[catalog].[folders] WHERE name = @folder)' + @cr;
--SET @sql += @tab + 'BEGIN' + @cr;
--SET @sql += @tab + @tab + 'RAISERROR(''Creating folder: %s ...'', 10, 1, @folder) WITH NOWAIT;' + @cr;
--SET @sql += @tab + @tab + 'EXEC @ReturnCode = [SSISDB].[catalog].[create_folder] @folder_name=@folder, @folder_id=@folder_id OUTPUT' + @cr;
--SET @sql += @tab + @tab + 'IF (@@ERROR <> 0 OR @ReturnCode <> 0) GOTO QuitWithRollback;' + @cr;
--SET @sql += @tab + 'END' + @cr + @cr;   
---------------------------------------------
-- Create environment + variables
-----------------------------------------------
DECLARE db_cursor CURSOR FOR
  SELECT [project_id], [name] FROM [internal].[projects] WHERE folder_id = @folder_id
OPEN db_cursor
FETCH NEXT FROM db_cursor
INTO @project_id, @name  
WHILE @@FETCH_STATUS = 0
BEGIN 
    SET @sql += @tab + 'SET @env = '''+ @name +'''' + @cr;
    SET @sql += @tab + 'IF NOT EXISTS (SELECT 1 FROM [SSISDB].[catalog].[environments] WHERE name = @env)' + @cr;
    SET @sql += @tab + 'BEGIN' + @cr;
    SET @sql += @tab + @tab +'RAISERROR(''Creating Environment: %s'', 10, 1, @env) WITH NOWAIT;' + @cr;
    SET @sql += @tab + @tab +'EXEC @ReturnCode = [SSISDB].[catalog].[create_environment] @folder_name=@folder, @environment_name=@env'  + @cr;
    SET @sql += @tab + @tab +'IF (@@ERROR <> 0 OR @ReturnCode <> 0) GOTO QuitWithRollback;' + @cr + @cr;
    SET @sql += @tab + 'END' + @cr;  
        print @sql;
        SET @sql = '';               
        -- ---------------------------------------------
        -- Generate the variable creation
        -- ---------------------------------------------
        SET @sql += '  -- ProjectId => '+ CONVERT(NVARCHAR(50), @project_id) + @cr;
        SELECT DISTINCT [cmd] = @tab + 'RAISERROR(''   Creating variable: ' + parameter_name + ' ...'', 10, 1) WITH NOWAIT;'           + @cr
                                        + @tab + 'EXEC @ReturnCode = [SSISDB].[catalog].[create_environment_variable]' + @cr
                                        + @tab + @tab + '  @variable_name=N'''    + parameter_name + ''''                     + @cr
                                        + @tab + @tab + ', @sensitive='           + CONVERT(varchar(2), sensitive)  + @cr
                                        + @tab + @tab + ', @description=N'''      + [description] + ''''            + @cr
                                        + @tab + @tab + ', @environment_name=@env'                                     + @cr
                                        + @tab + @tab + ', @folder_name=@folder'                                       + @cr
                                        + @tab + @tab + ', @value=@'            + @name +'__'+ parameter_name        + @cr
                                        + @tab + @tab + ', @data_type=N'''        + parameter_data_type + ''''                     + @cr
                                        + @tab + 'IF (@@ERROR <> 0 OR @ReturnCode <> 0) GOTO QuitWithRollback;'        + @cr
                                , [name] = parameter_name
        INTO #cmd
          FROM [SSISDB].[internal].[object_parameters]
         WHERE project_id = @project_id
           AND project_version_lsn = (SELECT MAX(project_version_lsn) FROM [SSISDB].[internal].[object_parameters] WHERE project_id = @project_id)
           AND parameter_name NOT LIKE 'CM.%'
        WHILE EXISTS (SELECT TOP 1 1 FROM #cmd)
        BEGIN
                SELECT TOP 1 @sql = cmd, @name = name FROM #cmd ORDER BY name;
                PRINT @sql;
                DELETE FROM #cmd WHERE name = @name;
        END;
        DROP TABLE #cmd;
        SET @sql = '';
    FETCH NEXT FROM db_cursor INTO @project_id, @name
END 
CLOSE db_cursor
DEALLOCATE db_cursor 
---------------------------------------------
-- Set Environment on each Project
--       + Set Environment variables on each Project Variables
---------------------------------------------
DECLARE db_cursor CURSOR FOR
  SELECT [project_id], [name] FROM [internal].[projects] WHERE folder_id = @folder_id
OPEN db_cursor
FETCH NEXT FROM db_cursor
INTO @project_id, @name  
SET @sql = 'DECLARE @reference_id AS BIGINT'+ @cr;
PRINT @sql;
WHILE @@FETCH_STATUS = 0
BEGIN
        SET @sql =  @tab + 'SET @project = '''+ @name +''';'+ @cr;
        SET @sql += @tab + 'SET @env = '''+ @name +'''' + @cr;
        SET @sql += 'RAISERROR(''Configure Project: %s ...'', 10, 1, @project) WITH NOWAIT;' + @cr + @cr
        SET @sql += '-- ------------------------------------------    '+ @cr
        SET @sql += '-- Set Environment to Project  '                  + @cr
        SET @sql += '-- ------------------------------------------    '+ @cr
        SET @sql += 'RAISERROR(''   Set Environment (%s) as Reference ...'', 10, 1, @env) WITH NOWAIT;' + @cr
        SET @sql += 'EXEC SSISDB.catalog.create_environment_reference'+ @cr
        SET @sql += @tab + @tab + '@folder_name      = @folder,     -- Folder (SSIDB >> "FolderName")'+ @cr
        SET @sql += @tab + @tab + '@environment_name = @env,     -- Environment Name              '+ @cr
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
        SET @sql =  @tab + 'SET @project = '''+ @name +''';'+ @cr;
        SET @sql += @tab + 'SET @env = '''+ @name +'''' + @cr;
        PRINT @sql
        SELECT
             [cmd] =
                  'RAISERROR(''   Set Project variable ('+ parameter_name  +') ...'', 10, 1) WITH NOWAIT;' + @cr
                + 'EXECUTE [SSISDB].[catalog].set_object_parameter_value '+ @cr
                + @tab + @tab + '@object_type     = '+ CONVERT(NVARCHAR(10), object_type) +',' + @cr
                + @tab + @tab + '@folder_name     = @folder,                    -- Folder (SSIDB >> "FolderName")'+ @cr
                + @tab + @tab + '@project_name    = @project,             -- Environment Name'+ @cr
                + @tab + @tab + '@parameter_name  = N'''+ parameter_name +''',  -- Project Variable Name'+ @cr
                + @tab + @tab + '@parameter_value = N'''+ parameter_name +''',  -- Environment Variable Name'+ @cr
                + @tab + @tab + '@object_name     = N'''+ object_name +''','+ @cr
                + @tab + @tab + '@value_type      = ''R'''+ @cr
            ,[name] = parameter_name
            INTO #cmd2
              FROM [SSISDB].[internal].[object_parameters]
             WHERE project_id = @project_id
               AND project_version_lsn = (SELECT MAX(project_version_lsn) FROM [SSISDB].[internal].[object_parameters] WHERE project_id = @project_id)
               AND parameter_name NOT LIKE 'CM.%'
        /*Print out the variable creation procs */
        WHILE EXISTS (SELECT TOP 1 1 FROM #cmd2)
        BEGIN
                SELECT TOP 1 @sql = cmd, @name = name FROM #cmd2 ORDER BY name;
                PRINT @sql;
                DELETE FROM #cmd2 WHERE name = @name;
        END;
    FETCH NEXT FROM db_cursor INTO @project_id, @name
END 
CLOSE db_cursor
DEALLOCATE db_cursor 
---------------------------------------------
-- END!
---------------------------------------------
SET @sql = '';
/* finsih the transaction handling */
SET @sql += 'COMMIT TRANSACTION' + @cr;
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
