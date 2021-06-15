===================================
Chapter 30 Project Scoring Toolbox
===================================
.. toctree::
    :maxdepth: 1
    :caption: Overview:

	Estimate Travel Time Savings <gp-travel-time-savings>
    List Study Area Zones <gp-list-study-area-zones>
    Map Study Area <gp-map-study-area>
    Stops to Streets Connectors <gp-stops-to-streets-connectors>	
    Ch30Tools python module <Ch30Tools>

The Chapter 30 Project Scoring Tools are comprised of four separate geoprocessing script tools for use in ArcGIS. These tools include:


	1. **Estimate Travel Time Savings** - Create a table that lists all study area zones and the average and total change
	in travel time weighted by a trip table. Total trips from each zone are also reported.  The table can be summarized to 
	estimate overall changes in travel time for all trips originating in the study area.

	2. **List Study Area Zones** - Create a table that lists all MSTM Level 2 TAZs in the project study area.
	In Chapter 30 transit project scoring, the study area is defined as all zones within 45 minutes transit
	travel time from the project or within 15 minutes driving time from the project.
	
	3. **Map Study Area** -	Based on a table of study area zones, create a feature layer selecting all zones in the
	study area or a feature class showing the dissolved boundary of the study area.
	
	4. **Stops to Streets Connectors** - If working in the ArcGIS Basic license level when creating transit networks
	using the "Add GTFS to a Network Dataset" toolbox, use this alternative tool to generate required network
	features (this is a substitute for completing step 2 of that toolbox's workflow, which requires the Standard
	or Advanced license levels).