#ESTIMATE TRAVEL TIME SAVINGS
#Author: Alex Bell, Renaissance Planning
#Last updated: Aug. 2019
"""
This is the geoprocessing interface for the travelTimeSavings function 
in the Chapter 30 tools (Ch30Tools) module.

Zones table : ArcGIS Table or Table View
	A table listing all distinct zones in the skims and trip tables (usually 
	all level 2 zones in the MSTM).
Zones table ID field : Field
	The field in `zones table` that uniquely identifies each zone. 
Base skim reference : File (.json)
	The skim reference file reflecting travel times in the base condition.
Build skim reference : File (.json)
	The skim reference file reflecting travel times in the build condition.
Trip table : ArcGIS Table or Table View
	The O-D table that records trips between OD pairs.
Trip table O field : Field
	The field in the `trip table` that identifies the origin zone in each row.
Trip table D field : Field
	The field in the `trip table` that identifies the destination zone in each
	row.
Trip table trip count field : Field
	The field in the `trip table` that identifies the number of trips between
	each O-D pair.
Study area zones table : ArcGIS Table or TableView
	The table listing all zones in a project study area.
Study area zones ID field : Field
	The field in `study area zones table` that identifies each unique zone
	in the project study area.
Output table: ArcGIS Table
	The output table to be produced, listing average travel time savings
	from each origin zone in the `study are zones table` in the "AvgTTChg"
	field. It will also list the total number of trips from each zone 
	("SumTrips"), and the total travel time savings from each zone ("SumTTChg"). 
	For study-area-wide average travel time savings, the column sum of "SumTTChg" 
	may be divided by the column sum of "SumTrips".
	
See Also
--------
Ch30Tools.travelTimeSavings
mma.skimReference

"""
import Ch30Tools
import arcpy

if __name__ == "__main__":
	zone_table = arcpy.GetParameterAsText(0)
	zone_id_field = arcpy.GetParameterAsText(1)
	base_skim_ref = arcpy.GetParameterAsText(2)
	build_skim_ref = arcpy.GetParameterAsText(3)
	trip_table = arcpy.GetParameterAsText(4)
	trip_o_field = arcpy.GetParameterAsText(5)
	trip_d_field = arcpy.GetParameterAsText(6)
	trip_val_fields = arcpy.GetParameterAsText(7)
	o_zone_table = arcpy.GetParameterAsText(8)
	o_zone_field = arcpy.GetParameterAsText(9)
	out_table = arcpy.GetParameterAsText(10)
	
	trip_val_fields = [trip_val_fields]
	
	Ch30Tools.travelTimeSavings(zone_table, zone_id_field,
							base_skim_ref, build_skim_ref,
							trip_table, trip_o_field, 
							trip_d_field, trip_val_fields,
							o_zone_table, o_zone_field, 
							out_table)