#Generate street-stop connectors
#Author: Alex Bell, Renaissance Planning
#Last udpated : June 2018

"""
This is the geoprocessing interface for the createStopsToStreetsConnectors function in the
Chapter 30 tools (Ch30Tools) module.

Stops features : ArcGIS Feature Class or Feature Layer
	Point features representing GTFS stop locations.
Streets features : ArcGIS Feature Class or Feature Layer
	Line features representing the pedestrian network from which 
	`stops features` will be accessed.
Search query : SQL Expression, optional
	Criteria to apply to `streets features` to limit which 
	streets stops will snap to.
Search tolerance : Linear Unit
	The distance from `stops features` to search for potential
	`streets features` to snap stops to streets.
Output geodatabase : Geodatabase
	The file or personal geodatabase in which output tables and 
	will be stored.
Feature dataset : ArcGIS Feature Dataset
	The feature dataset within `output_ws` in which output
	feature classes will be stored.
	
Nothing is returned by the function.  Several tables and feature
classes are generated in the `output_ws` and `feature_dataset`
workspaces:

- Connectors_Stops2StreetsTable (Table, interim)
- Connectors_Stops2Streets (Feature class, final)
- Stops_Snapped2Streets (Feature class, final)
"""

import Ch30Tools


if __name__ == "__main__":
    stops_fc = arcpy.GetParameterAsText(0) #feature layer
    streets_fc = arcpy.GetParameterAsText(1) #feature layer
    search_query = arcpy.GetParameterAsText(2) #SQL expression, optional
    search_tolerance = arcpy.GetParameterAsText(3) #linear unit
    output_ws = arcpy.GetParameterAsText(4) #workspace
    feature_dataset = arcpy.GetParameterAsText(5) #feature dataset 


    stops_layer = Ch30Tools.arcpy.MakeFeatureLayer_management(stops_fc, "stops_layer")
    streets_layer = Ch30Tools.arcpy.MakeFeatureLayer_management(streets_fc, "streets_layer", search_query)
    
    Ch30Tools.createStopToStreetConnectors(stops_layer, streets_layer, search_tolerance, output_ws, feature_dataset)
