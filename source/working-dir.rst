=======================================================================
Recommended Working Directory Structure for Chapter 30 Transit Scoring
=======================================================================
To organize the process of scoring multiple projects and streamline the workflow, 
it is helpful to follow a specific directory structure while shepherding Chapter 
30 projects through the accessibility scoring process. The recommended directory 
structure consists of the following folders:

**Decay_rates**
	Contains one or more `decay rate configuration files <gp-decay-rates.html>`_ (.JSON) to pass 
	to the `Summarize Accessibility <gp-summarize-accessibility.html>`_ tool in the MMA
	MMA geoprocessing toolbox.  The `decay rates <key-terms.html#decay-rates>`_ define how 
	the value of a destination diminishes as travel `impedance <key-terms.html#impedance>`_
	to it increases. Decay rate configuration files are provided as an a priori 
	input to the Chapter 30 accessibility scoring process. They should not be edited during 
	project scoring.

**GTFS**
	Contains all `GTFS <https://developers.google.com/transit/gtfs/reference/>`_ feeds to be 
	used in the development of the statewide base transit network as well as updated/additional 
	feeds representing specific projects.  All feeds should be stored in this folder and appropriate 
	feeds selected for the development of the base and project networks during the network 
	development phases of analysis. Each base or project feed should be included in a separate 
	subfolder to avoid confusion among feeds.

**Land_use**
	Contains feature classes representing `zone <key-terms.html#zones>`_ and 
	`centroid <key-terms.html#centroids>`_ features across the study area. For Chapter 30 scoring, 
	the study area is the entire state of Maryland and portions of neighboring states.  Level 2 zones from the 
	`Maryland Statewide Transportation Model (MSTM) <https://www.roads.maryland.gov/Index.aspx?PageId=254>`_ 
	and accompanying socio-economic/demographic data are utilized as the standard set of zones for Chapter 30 
	scoring. They are provided as a priori inputs to the Chapter 30 accessibility scoring process. 
	Demographic and employment data generally should not be edited, unless a project application 
	is accompanied by a project-specific land use forecast. 

**MMA_scores**
	Contains tables that represent summarized MMA scores generated using the 
	`Summarize Accessibility <gp-summarize-accessibility.html>`_	geoprocessing tool. 

**Networks**
	Contains base and project Network Datasets as developed following the 
	`Add GTFS to a Network Dataset Toolbox <https://esri.github.io/public-transit-tools/AddGTFStoaNetworkDataset.html>`_. 
	See the "Network Setup" section below.

**Project_specs**
	Contains shape files for each project network that include proposed route alignment and stops.

**Skims**
	Contains skim tables and skim reference files (.JSON) generated by the `Create Skims <gp-create-skim.html>`_ tool 
	(and the `Manage Skim References <gp-manage-skims.html>`_ tool when working with exogenous skims - this is generally
	not necessary for Chapter 30 scoring purposes). 

**Tools**
	Contains georpocessing toolboxes for use in ArcGIS???.
	- `MMA Geoprocessing Toolbox <mma-toolbox-main.html>`_ 
	- Chapter 30 Project Scoring Toolbox 