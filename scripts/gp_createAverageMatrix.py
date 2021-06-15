#CREATE AVERAGE MATRIX
#Author: Alex Bell, Renaissance PLanning
#Last updated: Oct. 2018
"""
This is the geoprocessing interface for the createAverageMatrix function
in the mma module.

If multiple skims are developed representing a consistent set of potential
O-D pairs (using a travel time window or alternative network parameters, 
e.g.), it may be desirable to summarize the average impedance between each
O-D pair describing a single "typical" impedance.  The `createAverageMatrix`
function facilitates such an analysis.
  
Workspace : ArcGIS workspace
	ArcGIS Workspace object (file folder, geodatabase, etc.) or 
	string representing the path to the workspace location where
	input skim tables are stored.
Skims tables : [String...]
	A selection of file names within `workspace` to reference in
	developing average impedance values	between each potential O-D 
	pair listed in `zones_table`.
Name field : Field
	The name of the field in each `skims table` file containing O-D zone 
	ID information. The field must by a string field formatted as 
	"{origin_id} - {destiantion_id}". It must be present in all `skims 
	table` files to be analyzed.
Impedance field : Field
	The name of the field in each `skims table` file containing impedance 
	information. The field must have a numeric type. The field must
	have the same name in all `skims table` files to be analyzed.
Zones table : String
	Path to an ArcGIS table or name of an ArcGIS table view
	in the active data frame containing the set of zones expected to
	be found in the `skims tables` files.
Zone ID field : String
	The name of the field in `zones table` containing zone ID 
	information.  Unique values in this field are used to construct
	an O-D matrix that is used to calculated average travel times.
Output table : String
	Full path to an ArcGIS table where the average O-D impedances
	will be stored.
		
See Also
---------
mma.createAverageMatrix
"""

import arcpy
import mma

	
if __name__ == "__main__":        
        skims_folder = arcpy.GetParameterAsText(0) #workspace
        skims_files = arcpy.GetParameter(1) #string, multivalue
        name_field = arcpy.GetParameterAsText(2) #field, from skims_file[0]
        impedance_field = arcpy.GetParameterAsText(3) #field, from skims_file[0], numeric
        zones_table = arcpy.GetParameterAsText(4) #table view
        zones_table_id = arcpy.GetParameterAsText(5) #field, from table view
        output_table = arcpy.GetParameterAsText(6) #table

        mma.createAverageMatrix(skims_folder, skims_files, name_field, 
						impedance_field, zones_table, zones_table_id, 
						output_table)
