===================
Data Preparation
===================

Maryland Statewide Transportation Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Maryland State Highway Administration (SHA) developed and maintains the `Maryland 
Statewide Transportation Model (MSTM) <http://www.roads.maryland.gov/index.aspx?PageId=254>`_. 
to support a variety of transportation planning and system operation and performance 
applications. The MSTM is a multiresolution travel demand modeling platform providing 
consistent data on land uses and travel networks across the state at multiple scales. 
Level 1 is the coarsest scale and is primarily utilized for statewide analyses; Level 
2 is an intermediate scale suitable for regional-level analyses; and Level 3 is a 
fine-grained scale supporting local area analyses.  

The following data from the MSTM are utilized for Chapter 30 transit project accessibility scoring:

	- Point (centroid) and polygon feature classes representing MSTM Level 2 zones.

	- Socio-economic and demographic data summarized to MSTM Level 2 zones for the scoring horizon year.

	- Polyline feature class representing MSTM Level 3 network features. Although the transit analysis is carried out at the Level 2 scale, the Level 3 network is utilized to model the access and egress to/from transit stops and stations at a sufficiently fine level of detail.

	- Trip table estimating number of person trips between MSTM level 2 zones.


Existing transit network GTFS feeds
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GTFS is a standard format for storing and sharing open transit data, including route
and schedule information.  GTFS feeds are collections of comma-delimited text (csv) 
files that provide sufficient information to model transit routing options by time 
of day for a selected service day (specific date or typical day of the week). 
The details of the tables included in a typical feed and the data recorded in each 
table are outlined `here <https://developers.google.com/transit/gtfs/reference/>`__.
	
For Chapter 30 transit scoring, General Transit Feed Specification (GTFS) feeds
for all transit properties in Maryland and neighboring jurisdictions (Washington,
DC and northern Virginia, e.g.) were obtained from the `Transportation Resource
Information Point website <https://github.com/mobilityequity/maryland-local-gtfs>`__.  
These feeds offer the best available representation of currently available fixed-route 
transit services across the state and serve as the basis of the “base” transit network. 
All feeds were utilized “as is,” assuming the feed developers adequately validated the 
information contained in each feed.

For 2019 Chapter 30 scoring, the latest available feeds were downloaded on April 30, 
2018 (originally downloade for the 2018 inaugural round of Chapter 30 project scoring).

EXISTING GTFS FEEDS

+----------------------------------------------------+------+------------+------------+------------------+
| Agency                                             | Name | Start      | Date       | Date             |
+====================================================+======+============+============+==================+
| Allegany County Transit                            | MD   | 2016/05/19 | 2018/01/01 | Summer/Fall 2016 |
+----------------------------------------------------+------+------------+------------+------------------+
| Annapolis Transit                                  | MD   | 2010/01/01 | 2019/12/31 | 2016/12/07       |
+----------------------------------------------------+------+------------+------------+------------------+
| BWI Thurgood Marshall Airport                      | MD   | 2016/01/01 | 2017/12/31 | 2016/12/06       |
+----------------------------------------------------+------+------------+------------+------------------+
| Calvert County Public Transportation               | MD   | 2015/09/23 | 2017/12/31 | 2016/12/08       |
+----------------------------------------------------+------+------------+------------+------------------+
| Carroll Transit System                             | MD   | 2016/04/13 | 2018/01/01 | 2016/12/27       |
+----------------------------------------------------+------+------------+------------+------------------+
| Cecil Transit                                      | MD   | 201001/01  | 2019/12/31 | 2016/06/14       |
+----------------------------------------------------+------+------------+------------+------------------+
| Charles County VanGo                               | MD   | 2015/10/06 | 2017/12/31 | 2016/12/19       |
+----------------------------------------------------+------+------------+------------+------------------+
| Charm City Circulator                              | MD   | 2016/05/06 | 2018/12/31 | 5/17/2016        |
+----------------------------------------------------+------+------------+------------+------------------+
| Delmarva Community Transit                         | MD   | 2015/09/23 | 2017/12/31 | 2016/10/20       |
+----------------------------------------------------+------+------------+------------+------------------+
| Harford Transit LINK                               | MD   | 2015/10/01 | 2017/12/31 | 2016/11/28       |
+----------------------------------------------------+------+------------+------------+------------------+
| Maryland Transit Administration                    | MD   | 2010/01/01 | 2019/12/31 | [no data]        |
+----------------------------------------------------+------+------------+------------+------------------+
| Montgomery County MD Ride On                       | MD   | 2010/01/01 | 2019/12/31 | [no data]        |
+----------------------------------------------------+------+------------+------------+------------------+
| Ocean City Transportation                          | MD   | 2016/11/24 | 2017/12/31 | 2017/07/07       |
+----------------------------------------------------+------+------------+------------+------------------+
| Queen Anne's County Ride                           | MD   | 2016/03/08 | 2017/12/31 | 2016/12/21       |
+----------------------------------------------------+------+------------+------------+------------------+
| Regional Transportation Agency of Central Maryland | MD   | 2016/06/01 | 2018/03/01 | 2016/11/15       |
+----------------------------------------------------+------+------------+------------+------------------+
| Shore Transit                                      | MD   | 2016/03/18 | 2020/01/01 | Summer 2016      |
+----------------------------------------------------+------+------------+------------+------------------+
| St. Mary's Transit System                          | MD   | 2015/09/23 | 2017/12/31 | 2016/12/21       |
+----------------------------------------------------+------+------------+------------+------------------+
| The Bus of Prince George's County                  | MD   | 2016/09/25 | 2017/12/31 | 2016/12/21       |
+----------------------------------------------------+------+------------+------------+------------------+
| TransIT Services of Frederick County               | MD   | 2010/01/01 | 2019/12/31 | 2013/01/28       |
+----------------------------------------------------+------+------------+------------+------------------+
| Washington County Transit                          | MD   | 2016/05/12 | 2018/01/01 | 2016/12/21       |
+----------------------------------------------------+------+------------+------------+------------------+
| DC Circulator                                      | DC   | 2010/01/01 | 2019/12/31 | [no data]        |
+----------------------------------------------------+------+------------+------------+------------------+
| WMATA                                              | DC   | 2010/01/01 | 2019/12/31 | [no data]        |
+----------------------------------------------------+------+------------+------------+------------------+
| Alexandria Transit Company (DASH)                  | VA   | 2010/01/01 | 2019/12/31 | [no data]        |
+----------------------------------------------------+------+------------+------------+------------------+
| Arlington Transit                                  | VA   | 2010/01/01 | 2019/12/31 | [no data]        |
+----------------------------------------------------+------+------------+------------+------------------+
| Fairfax Connector                                  | VA   | 2010/01/01 | 2019/12/31 | [no data]        |
+----------------------------------------------------+------+------------+------------+------------------+
| Fairfax CUE                                        | VA   | 2008/07/01 | 2020/01/01 | [no data]        |
+----------------------------------------------------+------+------------+------------+------------------+
| Loudon County Transit                              | VA   | 2010/01/01 | 2019/12/31 | [no data]        |
+----------------------------------------------------+------+------------+------------+------------------+
| Virginia Railway Express                           | VA   | 2010/01/01 | 2019/12/31 | [no data]        |
+----------------------------------------------------+------+------------+------------+------------------+
| Winchester Transit                                 | VA   | 2010/01/01 | 2019/12/31 | [no data]        |
+----------------------------------------------------+------+------------+------------+------------------+

Project Transit Network
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Descriptive information on the proposed service changes are needed for all projects. The most recent 
and authoritative planning documents should be identified for the development of these GTFS feeds. 
Attributes needed to code new or changed service include: mode (including dedicated right of way), 
transit stop locations, estimated departure times, service hours, frequency of service, and travel times. 
If one or more pieces of information is unavailable, reasonable assumptions should be made and documented.

After proposed service documentation is identified, GTFS files need to be developed to represent the 
proposed service. The matrix below outlines possible proposed infrastructure projects and the associated 
actions required for a GTFS feed to represent this project. Recommended best practice is to create a copy o
f the base GTFS feed to edit separately, or if new routes are proposed a new GTFS feed containing only the 
new route should be developed. 

SCENARIOS FOR UPDATING GTFS 

+---------------------+--------------------------+-----------+
| Improvement         | GTFS attributes affected | Action    |
+=====================+==========================+===========+
| Alignment change    | Stops, Stop Times        | Update    |
+---------------------+--------------------------+-----------+
| Service change      | Calendar                 | Update    |
+---------------------+--------------------------+-----------+
| Headway improvement | Stop Times, Frequencies  | Update    |
+---------------------+--------------------------+-----------+
| New route           | All                      | Build new |
+---------------------+--------------------------+-----------+
| Route deviation     | All                      | Build new |
+---------------------+--------------------------+-----------+


The 2019 Chapter 30 scoring included two transit projects. These projects are described 
below and links to the final project reports submitted to MDOT are included for reference. 
These project reports include detailed information on how the projects were coded into GTFS 
to create the project transit network GTFS feed and will provide examples of how to create 
these project transit feeds. 

+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------+
| Project Name                     | Description                                                                                                                                                                                                                        | Report Link                            |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------+
| South Side Transit               | A proposed light rail line between Alexandria, Va., and the Washington, D.C. suburb of Oxon Hill in Prince George’s County that would connect two existing Washington Metro stations serving the Green, Blue, and Yellow lines.    | `Report <citiesthatwork hosted link>`_ |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------+
| US 29 Bus Rapid Transit          | A potential BRT line with an alignment between Burtonsville and Mount Hebron in Maryland with four intermediate stops. The project would connect with the planned US 29 Flash BRT corridor in Burtonsville                         | `Report <citiesthatwork hosted link>`_ |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------+


Standard GTFS Tables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
The example tables above focus on the GTFS files that provide the richest details in modeling the
specific service characteristics of new and/or improved transit services. 
A standards-compliant GTFS feed rquires a series of files that meet validation requirements. 
In developing a new GTFS feed, it can be helpful to begin with standard tables provided by 
`Google Developer Resources website <https://developers.google.com/transit/gtfs/examples/gtfs-feed>`__.
All required files not shown in this user guide must be included in the project GTFS feed using
simplisitc coding (assuming a new route will operate on all days of the week in the calendar.txt file, 
e.g.).

These tables can form the basis for coding in a new build scenario network. Variables in the 
standard feed can be modified as needed to represent the proposed service. The standard tables 
are availabe at this link. 


.. note:: Before proceeding it is necessary to validate GTFS feeds. See "`GTFS Feed Validation </en/latest/quality-assurance.html#gtfs-feed-validation>`_" in "Chapter 30 Quality Assurance" for information on performing this step.