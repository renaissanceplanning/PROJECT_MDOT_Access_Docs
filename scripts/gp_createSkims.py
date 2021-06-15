#CREATE SKIMS 
#Author: Alex Bell, Renaissance Planning
#Last updated: Oct. 2018
"""
This is the geoprocessing interface for the summarizeAccessibility 
function in the mma module.

Network dataset : ArcGIS Network Dataset or Network Dataset Layer
	The network dataset used to find shortest paths between `origin 
	locations` and `destination locations.`
Impedance attribute : String
	The name of the impedance attribute in `network dataset` to be used in
	determining shortest paths between `origin locations` and `destination
	locations` (options are shown with units listed alongside each
	impedance attribute's name).
Cutoff value : Float, optional
	The maximum `impedance attribute` value from `origin locations` beyond 
	which `destination locations` will not be tabulated in the skim.
	If no value is provided, no cutoff is applied.  Applying a cutoff can
	reduce run times and focus the skim content on relevant destinations.
Number of destinations to find : Integer, Optional
	The maximum number of `destination locations` to find for each `origin
	location.` If no value is provided, all destinations (within the
	`cutoff value`) will be found.
Apply restrictions : [String,...]
	The restriction attributes in `network dataset` to honor when finding 
	shortest paths ("Oneway;PedesetrianOnly" e.g.).  If no restriction 
	attributes exist in the `network dataset` this field in the 
	geoprocessing interface will be empty.
U-turn policy : {"ALLOW_UTURNS", "NO_UTURNS", "ALLOW_DEAD_ENDS_ONLY", "ALLOW_DEAD_ENDS_AND_INTERSECTIONS_ONLY"}
	The u-turn policy to honor when	finding shortest paths.
Origin locations : ArcGIS Feature Class or Feature Layer
	An ArcGIS point feature class or point feature layer in the active 
	data frame representing origin locations to be recorded in the 
	skim(s).
Origin ID field : Field
	Field in `origin locations` to use as the origin ID value when 
	tabulating travel times in the skim(s).
Group Origins : Boolean, optional
	(Default is False.)  If checked (true), origins will be grouped for 
	processing.  Grouping limits the number of features included in a 
	given OD matrix tabulation to manage memory and output file sizes. If
	unchecked (false), all origins will be evaluated as a single group.
Reference layer for grouping origins : ArcGIS Feature Class or Feature Layer, optional  
	If `group origins` is checked (true), origins will be grouped based 
	on the spatial relationship of features in `origin features` to 
	features in this layer.	
Origin group ID field : Field, optional
	Name of the field in `reference layer for grouping origins` that
	organizes the grouping of `origin locations`. Distinct values in 
	this field will be included in output file names to relate each skim 
	table to its origin group.
Selection method : String, optional
	The spatial relationship to apply when grouping `origin locations` 
	based on `reference layer for grouping origins`. All ArcGIS	
	overlap_types are valid.	
Selection radius : Linear Unit, optional
	The distance to search around `reference layer for grouping origins`
	for testing their spatial relationship to `origin locations`. If no
	value is provided a strict spatial relationship among featues will be
	applied (i.e., no search radius).	
Destination features : ArcGIS Feature Class or Feature Layer
	An ArcGIS point feature class or point feature layer in the active 
	data frame representing destination locations to be recorded in the 
	skim(s).
Destination ID field : Field
	Field in `destination locations` to use as the destination ID value 
	when tabulating travel times in the skim(s).
Use network locations : Boolean, optional
	If checked (true), `origin locations` and `destination locations` will
	load on to the `network dataset` using pre-calculated values stored
	in various fields stored in their respective attribute tables. If 
	unchecked (false), `origin locations` and `destination locations` will
	load on to the `network dataset` based on spatial criteria (this takes
	longer and can lead to inconsistencies in loading locations).
Origin SourceID/SourceOID/PosAlong/SideOfEdge/SnapX/SnapY/Distance field : Field, optional
	If `use network locations` is checked (true), provide the names of the
	network location fields in the `origin locations` layer's attributes
	table.  Each field specifies a portion of the pre-calculated network
	location.
Destination SourceID/SourceOID/PosAlong/SideOfEdge/SnapX/SnapY/Distance field : Field, optional
	If `use network locations` is checked (true), provide the names of the
	network location fields in the `destination locations` layer's 
	attributes table.  Each field specifies a portion of the pre-calculated
	network	location.
Search tolerance units : Linear unit, optional
	If `use network locations` is unchecked (false), specify the maximum
	distance from a `network dataset` source listed in `network location 
	search criteria` to search for `origin locations` and `destination
	locations` for loading.  Features beyond the `search tolerance units`
	will be ignored during loading. (Default is "5000 Meters".)
Network location search criteria : [String,...]
	If `use network locations` is unchecked (false), list the network 
	sources and snapping points on which `origin locations` and 
	`destination locations` may load. 
Match to closest : Boolean, optional
	If `use network locations` is unchecked (false), specify how to select
	loading locations based on `network dataset` sources listed in `network
	location search criteria`. If `match to closest` is checked (true), 
	features will load on the closest valid source.
	If `match to closest` is unchecked (false), features will honor the 
	priority of `network dataset` sources implied by the order in which they
	are listed in `network location search criteria`, loading on the closest
	in a given priority group.
Exclude restricted portions of the network : Boolean, optional
	If `use network locations` is unchecked (false), specify whether 
	`origin locations` and `destination locations` can be loaded on 
	excluded `network` features.  Excluded features are those honored as 
	restricted as listed in `apply restrictions`.
	If `exclude restricted portions...` is checked (true), excluded 
	features will be ignored during network loading.
	If `exclude restricted portions...` is unchecked (false), some 
	locations may load on restricted features.
Additional criteria for loading on edges : String (edge source feature), optional
	If `use network locations` is unchecked (false), optionally specify 
	which `network dataset` features are available for loading.  This field
	points to a particular edge source feature class for additional querying
	(see `search criteria` below).
Search criteria : SQL Expression, optional
	If `use network locations` is unchecked (false), optionally specify 
	which `network dataset` features are available for loading.  This is an
	expression string to be applied to `additional criteria...` above that 
	further constrains loading beyond the limits set by `network location 
	search criteria`, `match to closest`, and `exclude restricted...` 
	parameters.
Output workspace : ArcGIS workspace
	ArcGIS Workspace (file folder, geodatabase, etc.) where output skim 
	tables will be stored.
Analysis name : String
	A string of characters to include in the names of output files to
	differentiate them from other files produced in the same `output 
	workspace.`  Short strings of 7 characters or fewer are recommended.
Use time of day : Boolean, optional
	If checked (true) the `network dataset` is time-enabled and the user 
	desires skims for a specific day and time(s).  If unchecked (false), no
	differentiation by time of day will be considered.
Day of week : {"Today", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}, optional
	If `use_time_of_day` is checked (true), time of day differences will
	be based on the day of week specified here.
Time window start : Date/time, optional
	If `use time of day` is checked (true), the first time on `day of week` 
	to be analyzed. Multiple skims can be produced based on the `time 
	window end` and	`time window increment...` values.
Time window end : Date/time, optional
	If `use time of day` is checked (true), the last time on `day of week` 
	to be analyzed. Multiple skims can be produced based on the `time 
	window end` and	`time window increment...` values. If only a single
	time of day skim is required, set `time window end` equal to `time
	window start`.	
Time window increment in minutes : Float, optional
	If `use time of day` is checked (true), the interval at which to
	increment the time so that multiple skims will be produced for
	every interval of `time window increment` between `time window start`
	and `time window end`.


See Also
---------
mma.createSkims
mma.Skim
"""
import arcpy
import mma


if __name__ == "__main__":
    #GET PARAMS  
    #   network
    network = arcpy.GetParameterAsText(0) # network dataset
    impedance_attribute = arcpy.GetParameterAsText(1) # string, impedance evaluator
    cutoff = arcpy.GetParameter(2) # double
    number_of_ds = arcpy.GetParameterAsText(3) # long, OPTIONAL
    restrictions = arcpy.GetParameterAsText(4) # string, multi-value, restriction evaluators
    u_turns = arcpy.GetParameterAsText(5) #string [ALLOW_UTURNS, NO_UTURNS, ALLOW_DEAD_ENDS_ONLY, ALLOW_DEAD_ENDS_AND_INTERSECTIONS_ONLY]

    #   origins
    o_features = arcpy.GetParameterAsText(6) #feature layer
    o_name = arcpy.GetParameterAsText(7) #field
    group_origins = arcpy.GetParameter(8) #boolean
    group_features = arcpy.GetParameterAsText(9) #feature layer, disabled if groupOrigins = false
    group_id_field = arcpy.GetParameterAsText(10) #field disabled if grouOrigins = false
    group_selection_method = arcpy.GetParameterAsText(11) # string
    group_selection_radius = arcpy.GetParameterAsText(12) # linear unit

    #   destinations
    d_features = arcpy.GetParameterAsText(13) #feature layer
    d_name = arcpy.GetParameterAsText (14) #field

    #   loading preferences
    use_network_locations = arcpy.GetParameter(15)

    o_SourceID =arcpy.GetParameterAsText(16)
    o_SourceOID = arcpy.GetParameterAsText(17)
    o_PosAlong =arcpy.GetParameterAsText(18)
    o_SideOfEdge =arcpy.GetParameterAsText(19)
    o_SnapX =arcpy.GetParameterAsText(20)
    o_SnapY = arcpy.GetParameterAsText(21)
    o_Distance = arcpy.GetParameterAsText(22)

    d_SourceID =arcpy.GetParameterAsText(23)
    d_SourceOID = arcpy.GetParameterAsText(24)
    d_PosAlong =arcpy.GetParameterAsText(25)
    d_SideOfEdge =arcpy.GetParameterAsText(26)
    d_SnapX =arcpy.GetParameterAsText(27)
    d_SnapY = arcpy.GetParameterAsText(28)
    d_Distance = arcpy.GetParameterAsText(29)

    tolerance = arcpy.GetParameterAsText(30) #linear unit
    search_criteria = arcpy.GetParameterAsText(31) #string
    match = arcpy.GetParameter(32) #boolean
    exclude_restricted = arcpy.GetParameter(33) # string [EXCLUDE, INCLUDE]
    query_edges = arcpy.GetParameterAsText(34) #feature class, from edges
    search_query = arcpy.GetParameterAsText(35) # sql expression(s) derived from network sources

    #output
    output_workspace = arcpy.GetParameterAsText(36) # workspace
    analysis_name = arcpy.GetParameterAsText(37) # string

    #time of day
    use_time_of_day = arcpy.GetParameter(39) #boolean
    day_of_week = arcpy.GetParameterAsText(40) #string [Use specific date, Today, Monday, Tuesday, ... Sunday]
    time_window_start = arcpy.GetParameter(41) #date/time
    time_window_end = arcpy.GetParameter(42) #date/time
    time_window_increment = arcpy.GetParameter(43) #double (minutes)

    #---------------------------------
    impedance_attribute = impedance_attribute.rsplit(',', 1)[0]
    if cutoff is None:
        cutoff = ""
    if number_of_ds is None:
        number_of_ds = ""
    if restrictions is None:
        restrictions = ""
    if tolerance is None:
        tolerance = "#"
    if search_criteria is None and use_network_locations == False:
        raise ValueError("use network locations or specify search criteria for loading origins and destinations on th network")
    if query_edges is None or search_query is None:
        query_edges = ""
        search_query = "#"

    mma.createSkims(network, impedance_attribute, o_features, o_name, d_features, d_name,
                    output_workspace, analysis_name,
                    cutoff=cutoff, number_of_ds=number_of_ds, restrictions=restrictions,
                    u_turns=u_turns, group_origins=group_origins, group_features=group_features,
                    group_id_field=group_id_field, group_selection_method=group_selection_method,
                    group_selection_radius=group_selection_radius,
                    use_network_locations=use_network_locations,
                    o_SourceID=o_SourceID, o_SourceOID=o_SourceOID, o_PosAlong=o_PosAlong,
                    o_SideOfEdge=o_SideOfEdge, o_SnapX=o_SnapX, o_SnapY=o_SnapY, o_Distance=o_Distance,
                    d_SourceID=d_SourceID, d_SourceOID=d_SourceOID, d_PosAlong=d_PosAlong,
                    d_SideOfEdge=d_SideOfEdge, d_SnapX=d_SnapX, d_SnapY=d_SnapY, d_Distance=d_Distance,
					search_criteria=search_criteria,
                    tolerance=tolerance, match=match, exclude_restricted=exclude_restricted,
                    query_layer=query_edges, search_query=search_query, use_time_of_day=use_time_of_day, 
                    day_of_week=day_of_week, time_window_start=time_window_start, time_window_end=time_window_end, 
                    time_window_increment=time_window_increment)




