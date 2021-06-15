#MAP STUDY AREA
#Author: Alex Bell, Renaissance Planning
#Last updated: Oct. 2018
"""
This is the geoprocessing interface for the mapStudyArea function in the
Chapter 30 tools (Ch30Tools) module.

Study area table : ArcGIS Table or Table View
	The table listing all zones included in the project study area.
Study area zone ID field : Field
	The field in `study area table` that identifies each zone in the
	project study area.
Zones features : ArcGIS Feature Class or Feature Layer
	A polygon feature class having zones with ID values corresponding
	to those in `study area zone ID field`.
Zones features ID field : String
	The field in `zones features` that contains zone ID values.  It should
	be of the same data type as `study area zone ID field`.
Output layer name : String, optional
	A recongizable name for the feature layer to be produced.
	Default is None, indicating an auto-generated unique name
	will be applied to the output feature layer.
Create output feature class: Boolean, optional
	If checked, features in the  `output layer` are dissolved and saved
	in `Output feature class`.  If unchecked, only a feature layer
	selecting `Zones features` in the `Study area table` is returned.
Output feature class : ArcGIS Feature Class, optional
	The output feature class to be produced, outlining the project study 
	area (dissolved zonal polygons). 
	
See Also
---------
Ch30Tools.mapStudyArea
gp_listStudyAreaZones
"""

import Ch30Tools

if __name__ == "__main__":
	study_area_table = arcpy.GetParameterAsText(0)
	sa_zone_field = arcpy.GetParameterAsText(1)
	zones_fc = arcpy.GetParameterAsText(2)
	zone_id_field = arcpy.GetParameterAsText(3)
	layer_name = arcpy.GetParameterAsText(4)
	create_ouput_fc = arcpy.GetParameter(5) #boolean
	output_fc = arcpy.GetParameterAsText(6)
	
	if layer_name in ['','#', None]:
		layer_name = None
		
	if not create_ouput_fc:
		output_fc = None
	
	out_layer = Ch30Tools. mapStudyArea(study_area_table, sa_zone_field, 
								zones_fc, zone_id_field, layer_name, 
								output_fc)
	
	arcpy.SetParameter(7, out_layer)