---
layout: post
title: SSIS - Log Execution time
date: 2019-03-12
categories: "SQL-Server"
tags: [other, sql-server]
comments: true
permalink: "/en/ssis-log-execution-time/"
parent: SQL Server
---
# {{ page.title }}
{: .fs-9 }


This query helps you to have a better view of your SSIS Packages executions.

When you run a "master job / package", you don't clearly see the execution time for your child packages in SSISDB Reports.

With this query, now it's possible :)

```
USE SSISDB
GO

SELECT
	 package_name
	,execution_id
	,executable_id
	,StartTime
	,EndTime
	,LastStatus
	,execution_result
	,RowIndex
	,DATEDIFF(minute, StartTime, EndTime) AS 'execution_time[min]'
FROM
(
	SELECT DISTINCT
		 executables.package_name AS package_name
		,executables.execution_id AS execution_id
		,executables.executable_id AS executable_id
		,FIRST_VALUE(start_time) OVER(PARTITION BY executables.package_name, executable_statistics.execution_id ORDER BY start_time ASC) AS StartTime
		,FIRST_VALUE(end_time) OVER(PARTITION BY executables.package_name, executable_statistics.execution_id ORDER BY end_time DESC) AS EndTime
		,FIRST_VALUE(execution_result) OVER(PARTITION BY executables.package_name ORDER BY end_time DESC) AS LastStatus
		,execution_result AS execution_result
		,ROW_NUMBER() OVER(partition by executables.package_name ORDER BY end_time DESC) AS RowIndex
  	  FROM    [catalog].[executables]
	LEFT JOIN [catalog].[executable_statistics] ON
														executable_statistics.execution_id = executables.execution_id
													AND executable_statistics.executable_id = executables.executable_id

	--WHERE executables.package_name = 'YourPackage.dtsx'
) A
 WHERE a.RowIndex = 1
 ORDER BY StartTime ASC</pre>
```