---
layout: post
title: Handling Data Type Conflicts in SQL for Merging Tables
date: 2024-09-20
categories: "fabric"
tags: [powerbi, tips]
comments: true
parent: Fabric
permalink: /fabric/handling-data-type-conflicts-in-sql-for-merging-tables
---
# {{ page.title }}
{: .fs-9 }


{:refdef: style="text-align: center;"}
  ![image](../../assets/2024/handling-data-type-conflicts-in-sql-for-merging-tables/FeaturedImage.png)
{: refdef .image50 }


## Handling Data Type Conflicts in SQL Queries

In this post, I’m sharing a SQL query designed to help you merge two tables that might have similar columns but different data types. This is especially useful when you’re comparing tables from different schemas where column data types don’t always match. The query automates the conversion and comparison process, saving you the hassle of handling type conflicts manually.

### Goal of the Query

The goal is to merge two tables (**Source1** and **Source2**) by aligning their columns, even if the data types differ. For example, if one table has a `varchar` column and the other has a `bigint`, the query will convert them into a common type (like `varchar`). This lets you easily combine the data without errors.

### How It Works

1. **Setting Up**: 
   Replace the schema and table names in the query with your actual table names. The query works for any two tables you want to compare.

2. **Data Type Mapping**: 
   The query includes a list of data types that can be automatically converted. This ensures that different types like `varchar` and `bigint` are unified into a compatible data type.

3. **Table Comparison**: 
   The query extracts column details (like names and data types) from both tables. Then, it checks if the columns match or need to be converted.

4. **Merging the Data**: 
   Finally, the query merges the data from both tables into a single result set using `UNION ALL`, handling any differences in column data types.

This method is useful for data migrations, ETL processes, or simply when you need to compare data across different systems.




```sql
DECLARE @Source1SchemaName   NVARCHAR(128) = 'YourFirstSchemaNameHere';
DECLARE @Source1TableName    NVARCHAR(128) = 'YourFirstTableHere';
DECLARE @Source2SchemaName   NVARCHAR(128) = 'YourSecondSchemaNameHere';
DECLARE @Source2TableName    NVARCHAR(128) = 'YourSecondTableHere';

WITH 
DataTypeSelection AS
(
	SELECT 'bigint' AS DataType1, 'varchar' AS DataType2, 'varchar' AS TargetDataType
	UNION ALL
	SELECT 'varchar' AS DataType1, 'bigint' AS DataType2, 'varchar' AS TargetDataType
	UNION ALL
	SELECT 'binary' AS DataType1, 'varbinary' AS DataType2, 'varbinary' AS TargetDataType
	UNION ALL
	SELECT 'varbinary' AS DataType1, 'binary' AS DataType2, 'varbinary' AS TargetDataType
	UNION ALL
	SELECT 'bit' AS DataType1, 'int' AS DataType2, 'int' AS TargetDataType
	UNION ALL
	SELECT 'int' AS DataType1, 'bit' AS DataType2, 'int' AS TargetDataType
	UNION ALL
	SELECT 'char' AS DataType1, 'varchar' AS DataType2, 'varchar' AS TargetDataType
	UNION ALL
	SELECT 'varchar' AS DataType1, 'char' AS DataType2, 'varchar' AS TargetDataType
	UNION ALL
	SELECT 'nchar' AS DataType1, 'nvarchar' AS DataType2, 'nvarchar' AS TargetDataType
	UNION ALL
	SELECT 'nvarchar' AS DataType1, 'nchar' AS DataType2, 'nvarchar' AS TargetDataType
	UNION ALL
	SELECT 'char' AS DataType1, 'nvarchar' AS DataType2, 'nvarchar' AS TargetDataType
	UNION ALL
	SELECT 'nvarchar' AS DataType1, 'char' AS DataType2, 'nvarchar' AS TargetDataType
	UNION ALL
	SELECT 'nchar' AS DataType1, 'varchar' AS DataType2, 'nvarchar' AS TargetDataType
	UNION ALL
	SELECT 'varchar' AS DataType1, 'nchar' AS DataType2, 'nvarchar' AS TargetDataType
	UNION ALL
	SELECT 'date' AS DataType1, 'datetime' AS DataType2, 'datetime2' AS TargetDataType
	UNION ALL
	SELECT 'datetime' AS DataType1, 'date' AS DataType2, 'datetime2' AS TargetDataType
	UNION ALL
	SELECT 'datetime2' AS DataType1, 'datetime' AS DataType2, 'datetime2' AS TargetDataType
	UNION ALL
	SELECT 'datetime' AS DataType1, 'datetime2' AS DataType2, 'datetime2' AS TargetDataType
	UNION ALL
	SELECT 'datetimeoffset' AS DataType1, 'datetime' AS DataType2, 'datetimeoffset' AS TargetDataType
	UNION ALL
	SELECT 'datetime' AS DataType1, 'datetimeoffset' AS DataType2, 'datetimeoffset' AS TargetDataType
	UNION ALL
	SELECT 'decimal' AS DataType1, 'numeric' AS DataType2, 'decimal' AS TargetDataType
	UNION ALL
	SELECT 'numeric' AS DataType1, 'decimal' AS DataType2, 'decimal' AS TargetDataType
	UNION ALL
	SELECT 'decimal' AS DataType1, 'float' AS DataType2, 'float' AS TargetDataType
	UNION ALL
	SELECT 'float' AS DataType1, 'decimal' AS DataType2, 'float' AS TargetDataType
	UNION ALL
	SELECT 'numeric' AS DataType1, 'float' AS DataType2, 'float' AS TargetDataType
	UNION ALL
	SELECT 'float' AS DataType1, 'numeric' AS DataType2, 'float' AS TargetDataType
	UNION ALL
	SELECT 'sysname' AS DataType1, 'varchar' AS DataType2, 'varchar' AS TargetDataType
	UNION ALL
	SELECT 'varchar' AS DataType1, 'sysname' AS DataType2, 'varchar' AS TargetDataType
	UNION ALL
	SELECT 'uniqueidentifier' AS DataType1, 'varchar' AS DataType2, 'varchar' AS TargetDataType
	UNION ALL
	SELECT 'varchar' AS DataType1, 'uniqueidentifier' AS DataType2, 'varchar' AS TargetDataType
	UNION ALL
	SELECT 'binary' AS DataType1, 'varbinary' AS DataType2, 'varbinary' AS TargetDataType
	UNION ALL
	SELECT 'varbinary' AS DataType1, 'binary' AS DataType2, 'varbinary' AS TargetDataType
	UNION ALL

	--
	-- Perfect Match
	--
	SELECT 'bigint' AS DataType1, 'bigint' AS DataType2, 'bigint' AS TargetDataType
	UNION ALL
	SELECT 'binary' AS DataType1, 'binary' AS DataType2, 'binary' AS TargetDataType
	UNION ALL
	SELECT 'bit' AS DataType1, 'bit' AS DataType2, 'bit' AS TargetDataType
	UNION ALL
	SELECT 'char' AS DataType1, 'char' AS DataType2, 'char' AS TargetDataType
	UNION ALL
	SELECT 'date' AS DataType1, 'date' AS DataType2, 'date' AS TargetDataType
	UNION ALL
	SELECT 'datetime' AS DataType1, 'datetime' AS DataType2, 'datetime' AS TargetDataType
	UNION ALL
	SELECT 'datetime2' AS DataType1, 'datetime2' AS DataType2, 'datetime2' AS TargetDataType
	UNION ALL
	SELECT 'datetimeoffset' AS DataType1, 'datetimeoffset' AS DataType2, 'datetimeoffset' AS TargetDataType
	UNION ALL
	SELECT 'decimal' AS DataType1, 'decimal' AS DataType2, 'decimal' AS TargetDataType
	UNION ALL
	SELECT 'float' AS DataType1, 'float' AS DataType2, 'float' AS TargetDataType
	UNION ALL
	SELECT 'int' AS DataType1, 'int' AS DataType2, 'int' AS TargetDataType
	UNION ALL
	SELECT 'nchar' AS DataType1, 'nchar' AS DataType2, 'nchar' AS TargetDataType
	UNION ALL
	SELECT 'numeric' AS DataType1, 'numeric' AS DataType2, 'numeric' AS TargetDataType
	UNION ALL
	SELECT 'nvarchar' AS DataType1, 'nvarchar' AS DataType2, 'nvarchar' AS TargetDataType
	UNION ALL
	SELECT 'smallint' AS DataType1, 'smallint' AS DataType2, 'smallint' AS TargetDataType
	UNION ALL
	SELECT 'sql_variant' AS DataType1, 'sql_variant' AS DataType2, 'sql_variant' AS TargetDataType
	UNION ALL
	SELECT 'sysname' AS DataType1, 'sysname' AS DataType2, 'sysname' AS TargetDataType
	UNION ALL
	SELECT 'tinyint' AS DataType1, 'tinyint' AS DataType2, 'tinyint' AS TargetDataType
	UNION ALL
	SELECT 'uniqueidentifier' AS DataType1, 'uniqueidentifier' AS DataType2, 'uniqueidentifier' AS TargetDataType
	UNION ALL
	SELECT 'varbinary' AS DataType1, 'varbinary' AS DataType2, 'varbinary' AS TargetDataType
	UNION ALL
	SELECT 'varchar' AS DataType1, 'varchar' AS DataType2, 'varchar' AS TargetDataType

)


,Source1 AS
(
	SELECT 
		c.name AS ColumnName,
		t.Name AS DataType,
		c.max_length AS MaxLength,
		c.precision,
		c.scale,
		c.is_nullable,
		ISNULL(i.is_primary_key, 0) AS PrimaryKey
	FROM    	    sys.columns       c
	INNER JOIN      sys.types         t  ON c.user_type_id = t.user_type_id
	LEFT OUTER JOIN sys.index_columns ic ON ic.object_id   = c.object_id AND ic.column_id = c.column_id
	LEFT OUTER JOIN sys.indexes       i ON ic.object_id    = i.object_id AND ic.index_id = i.index_id
	WHERE c.object_id = OBJECT_ID(@Source1SchemaName + '.' + @Source1TableName)
)
,Source2 AS
(
	SELECT 
		c.name AS ColumnName,
		t.Name AS DataType,
		c.max_length AS MaxLength,
		c.precision,
		c.scale,
		c.is_nullable,
		ISNULL(i.is_primary_key, 0) AS PrimaryKey
	FROM    	    sys.columns       c
	INNER JOIN      sys.types         t  ON c.user_type_id = t.user_type_id
	LEFT OUTER JOIN sys.index_columns ic ON ic.object_id   = c.object_id AND ic.column_id = c.column_id
	LEFT OUTER JOIN sys.indexes       i ON ic.object_id    = i.object_id AND ic.index_id = i.index_id
	WHERE c.object_id = OBJECT_ID(@Source2SchemaName + '.' + @Source2TableName)
)





SELECT 'WITH Source1 AS '
UNION ALL
SELECT '('
UNION ALL
SELECT 'SELECT ''Source1'' AS SourceSystem'
UNION ALL

--
-- Source1 section
--
SELECT
		'	,'+
		CASE WHEN  DataTypeSelection.TargetDataType IS NOT NULL THEN
			'CONVERT(' + DataTypeSelection.TargetDataType + 
						CASE 
							WHEN DataTypeSelection.TargetDataType IN ('char', 'varchar', 'nchar', 'nvarchar') THEN '(' + 
								CONVERT(
									VARCHAR(10)
									,CASE WHEN Source1.MaxLength > Source2.MaxLength 
										THEN Source1.MaxLength
										ELSE Source2.MaxLength
									END
								) + ')'
							WHEN DataTypeSelection.TargetDataType IN ('decimal', 'numeric') THEN '(' + 
								CONVERT(
									VARCHAR(10)
									,CASE WHEN Source1.precision > Source2.precision 
										THEN Source1.precision
										ELSE Source2.precision
									END
								) + ',' + 
								CONVERT(
									VARCHAR(10)
									,CASE WHEN Source1.scale > Source2.scale 
										THEN Source1.scale
										ELSE Source2.scale
									END
								) + ')'
							ELSE ''
							END
				+', '+ Source1.ColumnName +') AS '+  Source1.ColumnName 
			ELSE Source1.ColumnName +' AS '+ Source1.ColumnName 
			END
		--,Source1.ColumnName
		--,Source1.DataType
		--,Source2.DataType
		--,DataTypeSelection.TargetDataType
		--,Source1.MaxLength
		--,Source2.MaxLength

  FROM      Source1   Source1
  LEFT JOIN Source2     Source2 ON Source2.ColumnName = Source1.ColumnName
  LEFT JOIN DataTypeSelection  ON
	    DataTypeSelection.DataType1 = Source1.DataType
	AND DataTypeSelection.DataType2 = Source2.DataType
UNION ALL
SELECT '----- Attributes only present in Source2 result'
UNION ALL

SELECT '   ,'+
		'CONVERT('+ Source2.DataType +
			CASE 
				WHEN Source2.DataType IN ('char', 'varchar', 'nchar', 'nvarchar') THEN '(' + CONVERT(VARCHAR(10), Source2.MaxLength) +')'
				WHEN Source2.DataType IN ('decimal', 'numeric')                   THEN '(' + CONVERT(VARCHAR(10), Source2.precision) +', '+ CONVERT(VARCHAR(10), Source2.scale) +')'
				ELSE ''
			END
		 +', NULL) AS '+ Source2.ColumnName 
  FROM      Source2 
  LEFT JOIN Source1 ON Source1.ColumnName = Source2.ColumnName
 WHERE Source1.ColumnName IS NULL


UNION ALL
SELECT 'FROM '+ @Source1SchemaName + '.' + @Source1TableName
UNION ALL
SELECT ')'
UNION ALL
SELECT ''
UNION ALL
SELECT ',Source2 AS'
UNION ALL
SELECT '('
UNION ALL
SELECT 'SELECT ''Source2'' AS SourceSystem'
UNION ALL
SELECT
		'	,'+
		CASE WHEN  DataTypeSelection.TargetDataType IS NOT NULL THEN
			'CONVERT(' + DataTypeSelection.TargetDataType + 
						CASE 
							WHEN DataTypeSelection.TargetDataType IN ('char', 'varchar', 'nchar', 'nvarchar') THEN '(' + 
								CONVERT(
									VARCHAR(10)
									,CASE WHEN Source1.MaxLength > Source2.MaxLength 
										THEN Source1.MaxLength
										ELSE Source2.MaxLength
									END
								) + ')'
							WHEN DataTypeSelection.TargetDataType IN ('decimal', 'numeric') THEN '(' + 
								CONVERT(
									VARCHAR(10)
									,CASE WHEN Source1.precision > Source2.precision 
										THEN Source1.precision
										ELSE Source2.precision
									END
								) + ',' + 
								CONVERT(
									VARCHAR(10)
									,CASE WHEN Source1.scale > Source2.scale 
										THEN Source1.scale
										ELSE Source2.scale
									END
								) + ')'
							ELSE ''
							END
				+', '+ Source1.ColumnName +') AS '+ Source1.ColumnName 
			ELSE 'NULL AS '+ Source1.ColumnName 
			END
		--,Source1.ColumnName
		--,Source1.DataType
		--,Source2.ColumnName
		--,Source2.DataType
		--,DataTypeSelection.TargetDataType
		--,Source1.MaxLength
		--,Source2.MaxLength

  FROM      Source1   Source1
  LEFT JOIN Source2     Source2 ON Source2.ColumnName = Source1.ColumnName
  LEFT JOIN DataTypeSelection  ON
	    DataTypeSelection.DataType1 = Source1.DataType
	AND DataTypeSelection.DataType2 = Source2.DataType
UNION ALL
SELECT '----- Attributes only present in Source2 result'
UNION ALL

SELECT '   ,'+ Source2.ColumnName 
  FROM      Source2 
  LEFT JOIN Source1 ON Source1.ColumnName = Source2.ColumnName
 WHERE Source1.ColumnName IS NULL


UNION ALL
SELECT 'FROM ' + @Source2SchemaName + '.' + @Source2TableName
UNION ALL
SELECT ')'
UNION ALL
SELECT ''
UNION ALL
SELECT ',MergeSourceSystem AS'
UNION ALL
SELECT '('
UNION ALL
SELECT '	SELECT * FROM Source1'
UNION ALL
SELECT '	UNION ALL'
UNION ALL
SELECT '	SELECT * FROM Source2'
UNION ALL
SELECT ')'
UNION ALL
SELECT 'SELECT '
UNION ALL
SELECT '*'
UNION ALL
SELECT ' FROM MergeSourceSystem'

```

