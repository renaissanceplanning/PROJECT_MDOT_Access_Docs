#CALCULATE CHANGE IN ACCESSIBILITY
#Author: Alex Bell, Renaissance Planning
#Last updated: Oct. 2018
"""
This is the geoprocessing interface for calculating the change in 
accessibility between two tables containing accessibility summaries
for a set of zones under two alternative conditions or scenarios. 

To understand how accessibility is modified by a project altering
the transportation system and/or land uses, for example, provide 
a `no build table` reflecting baseline accessibility scores and a 
`build` table reflecting new accessibility scores assuming the 
project is implemented.  For each zone affected by the project,
subtract the no build scores from the build scores to determine 
the changes wrought by the project.

No build table : ArcGIS Table or Table View
	The table containing accessibility scores for a set of zones
	in the "no build" or "baseline" condition.
Build table : ArcGIS Table or Table View
	The table containing accessibility scores for a set of zones
	(matching those in the `no build table`) in the "build" or 
	"change" condition.
ID field : Field
	The field - present in both the `no build table` and the `build
	table` - containing zone IDs allowing records in the two tables
	to be related to each other.
Accessibility fields : [Field,...]
	The fields containing accessibility scores for which the differences
	between the `build` and `no build` conditions will be calculated and
	stored in the `output table`.  Field names must be the same in both
	input tables and will carry over to the `output table`.
Output table : ArcGIS Table
	The output table storing the differences between the `build table`
	and the `no build table`.
	
"""

import arcpy

def tableDifference(table_1, table_2, id_field, diff_fields, output_table,
					skip_nulls=True, null_value=0):
	"""
	Given two tables of identical structure and similar content, calculate
	the differences (table_2 minus table_1) between values in a selection
	of fields for records identified by a common ID value in each table.
	
	This function assumes two tables of identical structure and similar
	content as shown in the example below. They each have an ID field with
	at least some common ID values in both tables. They also share common
	numerical fields, for which the analyst wants to know the differences
	between values in each table for each distinct ID value.  If an ID
	value is present in one table and not the other, it will be treated
	based on the provided `null_value` (default is 0). 
	
	Example table_1:
	
	===  ========  ========
	ID   Field 1   Field 2
	===  ========  ========
	1    1000      900  
	2    2000      600
	9    3000      300
	===  ========  ========
	
	Example table_2:
	
	===  ========  ========
	ID   Field 1   Field 2
	===  ========  ========
	1    1200      750  
	2    2100      1019
	3    3500      25
	===  ========  ========
	
	Example result table (table_2 minus table_1):	
	
	===  ========  ========  ===================================
	ID   Field 1   Field 2   *notes*
	===  ========  ========  ===================================
	1    200       -150      *presnt in both tables*
	2    100       419       *present in both tables*
	3    3500      25        *present in table_2, not table_1*
	9    -3000     -300      *present in table_1, not table_2*
	===  ========  ========  ===================================
	
	Parameters
	-----------
	table_1 : ArcGIS Table or TableView
		A table that organizes data by distinct values in an `id_field`
		and containing measures in one or more numerical fields.
	table_2 : ArcGIS Table or Table View
		A second table identical in structure to `table_1` with similar
		distinct values in the `id_field` and different values for 
		measures, representing an alternative condition or scenario, e.g.	
	id_field : String
		The field in `table_1` that is also in `table_2` that uniquely
		and consistently identifies records such that each table's rows
		can be directly joined and compared to each other.	
	diff_fields : [String,...]
		The list of numerical fields in `table_1` that are also in 
		`table_2`, representing measures for which the differences between
		the tables are to be calculated (by distinct values in `id_field`).	
	output_table : String
		The full path to the output table storing the differences 
		(`table_2` minus `table_1`).		
	skip_nulls : Boolean, optional
		If True, null (missing) values in each table will not be
		considered in the calculated of differences between `table_1`
		and `table_2`.  If False, null (missing) values in each 
		table will be included in the difference calculation and 
	null_value : Float, optional
		The value to assume whenever a null (missing) value is found in 
		a table.  Default is 0. Onyl applies if skip_nulls is False.

	Returns
	--------
	None
		Writes an output table with the differences between `table_1` and
		`table_2` .	
	"""
	#prep_outputs
	fields = [id_field] + diff_fields
	id_field_obj = arcpy.ListFields(table_1, id_field)[0]
	if id_field_obj.type == u"String":
		id_field_type = "|S{}".format(id_field_obj.length)
	elif id_field_obj.type in [u"Integer", u"SmallInteger"]:
		id_field_type = "<i4"
	else:
		id_field_type = "<f8"
	dt_list = [(str(id_field), id_field_type)]
	dt_list += [(str(diff_field), "<f8") for diff_field in diff_fields]
	dt = np.dtype(dt_list)
	#get data frames from tables and merge
	df_1 = pd.DataFrame(arcpy.da.TableToNumPyArray(table_1, fields,
												skip_nulls=skip_nulls, null_value=null_value))
	df_2 = pd.DataFrame(arcpy.da.TableToNumPyArray(table_2, fields,
												skip_nulls=skip_nulls, null_value=null_value))
	df_merge = df_1.merge(df_2, how='inner', on=id_field)
	#subtract parallel values    
	for diff_field in diff_fields:
		df_merge[diff_field] = df_merge["{}_y".format(diff_field)] - df_merge["{}_x".format(diff_field)]
	#output
	out_array = np.array(df_merge[fields].to_records(index=False),dt)
	arcpy.da.NumPyArrayToTable(out_array, output_table)


if __name__ == "__main__":
    table_1 = arcpy.GetParameterAsText(0) # table view
    table_2 = arcpy.GetParameterAsText(1) # table view
    id_field = arcpy.GetParameterAsText(2) # string, field in common
    diff_fields = arcpy.GetParameterAsText(3) # string, multivalue, num field in common
    output_table = arcpy.GetParameterAsText(4) # table, output

    diff_fields = diff_fields.split(';')

    mma.tableDifference(table_1, table_2, id_field, diff_fields,
                              output_table)
