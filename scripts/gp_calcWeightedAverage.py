#CALCUALTE WEIGHTED AVERAGES
#Author: Alex Bell, Renaissance Planning
#Last updated: Oct. 2018
"""
This is the geoprocessing interface for calculating the weighted average
of value(s) of a (set of) column(s) in a table based on the distribution 
of values in another (set of) column(s) in the table.

Determine an areawide average score or value based on sub-area 
distributions of activity (population-weighted average access to jobs, 
e.g.).

Input table : ArcGIS Table/Table View/Feature Class/Feature Layer
	The table containing values for which averages are desired and weight
	fields for calculating the appropriate average values. 
Value fields : [Field,...]
	The fields in the `input table` for which the average value based on 
	values in each `weight field` will be reported.
Weight fields : [Field,...]
	The fields in the `input table` that will be applied to each `value
	field` as weights to determine the `value field's` average value 
	across all rows in the table. Weighted average values for each 
	`value field` are reported in separate rows for each `weight field`.
Select features from the input table : SQL Expression, optional
	A SQL expression applied to the `input table` to focus the weighted
	average calculation on records matching the criteria defined by the 
	expression.
Select subset : Boolean, optional
	If True, a "secondary" table or feature class may be used to select
	records from the `input table` to focus the weighted average 
	calculation on records matching criteria in the secondary table or
	having a specified spatial relationship to the secondary feature 
	class. (Default is False.)
Selection method : {"SPATIAL", "TABULAR"}, optional
	If `select subset` is True, specify whether the selection of records
	in the `input` table will be based on a spatial relationship to a 
	secondary feature class ("SPATIAL") or on a lookup relationship to
	a secondary table ("TABULAR").  If "SPATIAL", `input table` must be 
	a feature class or feature layer.
Reference layer : ArcGIS Feature Class or Feature Layer, optional
	If `selection method` is "SPATIAL," the secondary feature class or
	feature layer to use as the basis for spatial selection of features in
	`input table`.
Select features from reference layer : SQL Express, optional
	If `selection method` is "SPATIAL," optionally provide a SQL 
	expression to limit the features in `reference layer` used for the 
	spatial selection of features in `input table`.
Spatial relationship : String, optional
	If `selection method` is "SPATIAL," define the spatial relationship
	to use when selecting features in `input table`.  All ArcGIS 
	overlap_types are valid.
Search distance : Linear Unit, optional
	If `selection method` is "SPATIAL," define the search tolerance to
	guide the selection of features from the `input table` based on their
	`spatial relationship` to features in the `reference layer`.  If blank,
	a strict spatial selection is applied.
Reference table : ArcGIS Table or Table View, optional
	If `selection method` is "TABULAR," the secondary table or table view
	to use as the basis for tabular selection (through lookup) of records
	in `input table`.
Refrence table key field : Field, optional
	If `selection method` is "TABULAR," the field in `reference table` 
	containing values to lookup in `input table` (based on its values in
	the `input table lookup field`) for inclusion in the weighted average 
	calculation.
Input table lookup field : Field, optional
	If `selection method` is "TABULAR," the field in `input table` 
	containing values corresponding to those in the `reference table
	key field` (in the `reference table`). Only `input table` records
	having values in this field that match those listed in the 
	`reference table key field` will be included in the weighte average
	calculation.
Select records from reference table : SQL Expression, optional
	If `selection method` is "TABULAR," optionally provide a SQL 
	expression to limit the records in `reference table` used for the 
	tabular lookup of records in `input table`.
Output table : ArcGIS Table
	The output table storing the weighted averages.  The output table is 
	organized in to rows representing each `weight field` and columns
	containing the weighed average values for each `value field` for that
	`weight field`.
	
"""

import arcpy
import uuid
import pandas as pd

global _FIELD_TYPE_DICT

_FIELD_TYPE_DICT = {
	"String":"TEXT",
	"SmallInteger": "SHORT",
	"Integer": "LONG",
	"Single": "FLOAT",
	"Double": "DOUBLE",
	"Date": "DATE"
	}

def _getFieldTypeName(table, field_name):
	field = arcpy.ListFields(table, field_name)[0]
	ftype = field.type
	return _FIELD_TYPE_DICT[ftype]

	
def weightedAverage(table, value_fields, weight_fields):
	"""
	Calculate the average value(s) of a (list of) column(s) in a table,
	weighted by the values in another column or list of columns in the
	table.
	
	Parameters
	-----------
	table : ArcGIS Table or ArcGIS Table View
		The table with `value_fields` and `weight_fields` from which to 
		calculate and tabulate weighted averages.
	value_fields : [String,...]
		A list of field names whose values will be averaged.
	weight_fields : [String,...]
		A list of field names whose values will provide weights that
		influence the averages calculated from `value_fields`.
	
	Returns
	--------
	out_array : Numpy array
		Returns an output array with weighted averages reported such that
		each `weight_field` is in its own row and each column provides the
		weighted average of each `value_field` as weighted by the
		`weight_field` reflected in that row.
		
	Notes
	------
	When values in a table are recorded in an aggregated manner such that 
	a single record may represent a common condition or value for a 
	collective, a simple average of column values for that table offers
	limited insight into typical conditions for members of that 
	collective.  In these cases, a weighted average is needed to describe
	the average value for the collective.

	An example of this is geographic aggregation into zones.  Each zone 
	may have multiple people and different population groups residing 
	within it.  For measures calculated at the zone level, a simple 
	average of those measures across zones will not reflect typical 
	conditions for the people living in those zones.  A weighted average
	takes into account the conditions as they apply on a *per person* 
	basis rather than on a *per zone* basis.  

	See the example below showing commute times and distaces for male and
	female populations in three zones. The average commute time for males
	in the combined three-zone area cannot be calculated as the sum of the
	"commute_time" column divided by 3 (the zonal average commute time) 
	because the distribution of the male population is not uniform across 
	all zones.  Most males live in Zone 1 with an estimated commute time of
	26 minutes.  Thus, the average for all males in the three-zone area 
	will be closer to 26 minutes than to the 16 minutes shown for zone 2, 
	where only 5 males reside. The weighted average commute time for males
	is actually 24.2, as shown in the example result array.  

	The average commute time for females differs from that for males 
	because the distribution of females across the zones differs from the 
	male population distribution.

	Example input table

	========  =========  ===========  =============  =============
	Zone_ID   Male_pop   Female_pop   Commute_time   Commute_dist
	========  =========  ===========  =============  =============
	1         100        90           26             8.5
	2         5          9            16             5.3
	3         27         40           19             7.1
	========  =========  ===========  =============  =============

	Example result array	

	============  =============  =============
	WeightField   Commute_time   Commute_dist
	============  =============  =============
	Male_pop      24.2           8.1
	Female_pop    23.3           7.9
	============  =============  =============
	
	"""
	#prepare outputs
	out_rows = [] #weight_field, weight sum, wtd_val1, wtd_val2, ... wtd_valn
	out_dt = [("weight_field", "|S50"), ("SUM", "<f8")]
	out_dt += [(str(vf), "<f8") for vf in value_fields]

	#create the processing array
	fields = value_fields + weight_fields
	processing_df = pd.DataFrame(arcpy.da.TableToNumPyArray(table, fields))
	#arcpy.AddMessage(processing_df.head())

	#summarize weighted values
	for weight_field in weight_fields:
		columns = [weight_field] + value_fields
		df = processing_df[columns]
		weight_sum = sum(df[weight_field])
		out_row = [weight_field, weight_sum]
		for value_field in value_fields:
			wtd_field = "wtd_{}".format(value_field)
			df[wtd_field] = df[weight_field] * df[value_field]
			prodsum = sum(df[wtd_field])
			wtd_value = prodsum/float(weight_sum)
			out_row.append(wtd_value)
		out_rows.append(tuple(out_row))
	
	out_array = np.array(out_rows, out_dt)
	return out_array
	

if __name__ == "__main__":
	table = arcpy.GetParameterAsText(0) # table view
	value_fields = arcpy.GetParameterAsText(1) # field, multivalue, derived from table
	weight_fields = arcpy.GetParameterAsText(2) # field, multivalue, derived from table
	table_expr = arcpy.GetParameterAsText(3) #SQL expression, derived from table, optional
	select_subset = arcpy.GetParameter(4) #boolean, optional
	selection_method = arcpy.GetParameterAsText(5) # string, SPATIAL, TABULAR
	reference_layer = arcpy.GetParameterAsText(6) # feature layer, enabled if selection_method=SPATIAL
	ref_lyr_expr = arcpy.GetParameterAsText(7) #SQL expression, derived from reference_layer, optional
	spatial_relationship = arcpy.GetParameterAsText(8) # string, enabled if selection_method=SPATIAL
	search_distance = arcpy.GetParameterAsText(9) #linear unit, optional
	reference_table = arcpy.GetParameterAsText(10) # table view, enabled if selection_method=TABULAR
	ref_tab_id_field = arcpy.GetParameterAsText(11) #field, derived from reference table
	table_lookup_field = arcpy.GetParameterAsText(12) #field, derived from table (parameter 0)
	ref_tab_expr = arcpy.GetParameterAsText(13) #SQL expression, derived from reference table, optional
	out_table = arcpy.GetParameterAsText(14) # table, output

	value_fields = value_fields.split(';')
	weight_fields = weight_fields.split(';')
	
	ds_type = arcpy.Describe(table).datasetType
	uuid_obj = uuid.uuid1()
	_uuid = str(uuid_obj).replace('-','_')
	
	if select_subset:
		if selection_method == "SPATIAL":
			if ds_type == u'FeatureClass':				
				_table_layer = arcpy.MakeFeatureLayer_management(table, "{}_table".format(_uuid), where_clause=table_expr)
				_ref_layer = arcpy.MakeFeatureLayer_management(reference_layer, "{}_ref".format(_uuid), where_clause=ref_lyr_expr)
				arcpy.SelectLayerByLocation_management(_table_layer, spatial_relationship, _ref_layer, selection_type="NEW_SELECTION")
			else:
				arcpy.AddWarning("Input table {} is not a feature class.  Spatial selection based on features in {} not available".format(table, reference_layer))
				_table_layer = arcpy.MakeTableView_management(table, "{}_table".format(_uuid), where_clause=table_expr)
		elif selection_method == "TABULAR":
			with arcpy.da.SearchCursor(reference_table, ref_tab_id_field, where_clause=ref_tab_expr) as c:
				ref_records = list({r[0] for r in c})			
			field_delim = arcpy.AddFieldDelimiters(table, table_lookup_field)
			quotes = ""
			if _getFieldTypeName(table, table_lookup_field) == "TEXT":
				quotes = "'"			
			lookup_expr = " OR ".join(["{}={}{}{}".format(field_delim, quotes, rec, quotes) for rec in ref_records])
			if table_expr:
				where_clause = "({}) AND ({})".format(table_expr, lookup_expr)
			else:
				where_clause = lookup_expr
			_table_layer = arcpy.MakeTableView_management(table, "{}_table".format(_uuid), where_clause=where_clause)
			result = arcpy.GetCount_management(_table_layer)
			arcpy.AddMessage('selected {} records'.format(result[0]))
		else:
			_table_layer = arcpy.MakeTableView_management(table, "{}_table".format(_uuid), where_clause=table_expr)
	else:
		_table_layer = arcpy.MakeTableView_management(table, "{}_table".format(_uuid), where_clause=table_expr)
	
	out_array = weightedAverage(_table_layer, value_fields, weight_fields)
	arcpy.da.NumPyArrayToTable(out_array, out_table)
