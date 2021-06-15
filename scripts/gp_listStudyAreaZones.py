#LIST STUDY AREA ZONES
#Author: Alex Bell, Renaissance Planning
#Last updated: Oct. 2018
"""
This is the geoprocessing interface for the listStudyAreaZones
function in the Chapter 30 tools (Ch30Tools) module.

Transit skim references : File (.json)
	A (list of) skim reference configuration file(s) to search for
	study area zones reachable within `transit time cutoff` from
	zones included in `select zones`.
Transit travel time cutoff : Double
	The transit travel time tolerance used to determine a zone's 
	inclusion in the project study area.
Auto skim references : File (.json)
	A (list of) skim reference configuration file(s) to search for
	study area zones reachable within `auto time cutoff` from
	zones included in `select zones`.
Auto travel time cutoff : Double
	The auto (highway) travel time tolerance used to determine a  
	zone's inclusion in the project study area.
Select zones : [Variant,...]
	A list of values corresponding to Zone IDs.  The list includes 
	all zones considered to be "within the project limits."
Output table : ArcGIS Table 
	The output table to be produced by the tool, listing all zones
	in the project area.  The table includes zones in `select zones`
	as well as those reachable by transit within `transit time cutoff`
	and by auto within `auto time cutoff`.

See Also
---------
Ch30Tools.listStudyAreaZones
gp_mapStudyArea
"""

import Ch30Tools

if __name__ == "__main__":
	transit_skim_references = arcpy.GetParameterAsText(0) #file, .json, multivalue
	transit_cutoff = arcpy.GetParameterAsText(1) #double
	auto_skim_references = arcpy.GetParameterAsText(2) #file, .json, multivalue
	auto_cutoff = arcpy.GetParameterAsText(3) #double
	select_zones = arcpy.GetParameter(4) #string, multivalue
	output_table = arcpy.GetParameterAsText(5)
	
	transit_skim_references = transit_skim_references.split(';')
	auto_skim_references = auto_skim_references.split(';')
	select_zones_unpack = []
	for sz in select_zones:
		select_zones_unpack += [z.strip() for z in sz.split(';')]
	
	Ch30Tools.defineProjectStudyArea(transit_skim_references, transit_cutoff, auto_skim_references, auto_cutoff,
							select_zones_unpack, output_table)