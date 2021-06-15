#SUMMARIZE ACCESSIBILITY
#Author: Alex Bell, Renaissance Planning
#Last updated: Oct. 2018
"""
This is the geoprocessing interface for the summarizeAccessibility 
function in the mma module.

This is the final step in developing accessibility scores by zone 
using a skim file (or set of skim files) and a table of land use data.

Skims reference files : File (.json)
	A (list of) skim reference file(s)
Run in series : Boolean, optional 
	If checked, the accessibility results for each `skim reference file`
	will be saved to a distinct output table  bearing that `skim 
	reference file`'s name in the `output workspace`.  If unchecked, 
	accessibility results for all `skim reference files` will be 
	consolidated in a single `output table`
Land use table : ArcGIS Table or Table View
	A table that organizes land use data by zones with an ID field
	that corresponds to values in each skim table's (`skim reference
	file`'s) destination ID values.
Land use table ID field : Field
	The field in `Land use table` that identifies each zone.  Values in 
	this field should correspond to values in each skim table's (`skim 
	reference file`'s) destination ID values.
Land use table activity fields : [Field,...]
	A list of field names representing the activities at each 
	(destination) zone to summarize in the accessibility tabulation.
Apply decay rates : File (.json)
	A (list of) decay file(s) defining decay rates to be applied in the 
	summarization of activities in `lu_table_activity_fields`. Decay rates
	define how destination-end activities should be discounted based on the 
	impedance from the origin.
Output table : ArcGIS Table, optional
	If `Run in series` is unchecked, a single `Output table` will be 
	generated summarizing accessibility from all origins listed in 
	the `skim reference files` based on the travel times recorded in 
	the skims, the `land use activity table fields`, and any `decay
	rates` applied.
Output workspace : ArcGIS workspace, optional
	If `Run in series` is checked, an `Output table` will be 
	generated for each `skim refernce file`, summarizing accessibility 
	from all origines listed in that skim based on the travel times 
	recorded in the skim, the `land use activity table fields`, and any
	`decay rates` applied.
	
See Also
---------
mma.summarizeAccessibility
mma.Skim
mma.Decay
"""

import arcpy
import mma


if __name__ == "__main__":
    skims_ref_files = arcpy.GetParameterAsText(0) # file, .json, multivalue
    run_in_series = arcpy.GetParameter(1) # boolean
    lu_table = arcpy.GetParameterAsText(2) # table view
    lu_table_id = arcpy.GetParameterAsText(3) # field, derived from lu_table
    lu_table_activity_fields = arcpy.GetParameterAsText(4) # field, numeric, multivalue, derived from lu_table
    decays_files = arcpy.GetParameterAsText(5) # file, .json, multivalue
    out_table = arcpy.GetParameterAsText(6) # table, output
    out_workspace = arcpy.GetParameterAsText(7) # workspace

    #create lists of values for multivalue params
    skims_ref_files = skims_ref_files.split(';')
    lu_table_activity_fields = lu_table_activity_fields.split(';')
    decays_files = decays_files.strip("'")
    decays_files = decays_files.split(';')

    #create list of decays from decays_files
    decays = [mma.jsonToDecay(decay_file) for decay_file in decays_files]

    #create skim set object and add skims from skims_ref_files
    if run_in_series:
        #name output table
        out_ws_type = arcpy.Describe(out_workspace).workspaceType
        if out_ws_type == u'FileSystem':
            f_ext = '.dbf'
        else:
            f_ext = ''
        #summarize accessibility for each skim object
        for skims_ref_file in skims_ref_files:
            skim_obj = mma.jsonToSkim(skims_ref_file)
            table_name = skim_obj.table.rsplit('.dbf',1)[0]
            skim_set_obj = mma.SkimSet(table_name)
            skim_set_obj.addSkim(skim_obj)
            out_table = "{}\\{}{}".format(out_workspace, table_name, f_ext)
            #run
            mma.summarizeAccessibility(skim_set_obj, lu_table, lu_table_id,
                                lu_table_activity_fields, out_table,
                                decays=decays)
    else:
        #summarize accessibility for all skim objects together
        skim_set_obj = mma.SkimSet()
        for skims_ref_file in skims_ref_files:
            skim_set_obj.addSkim(mma.jsonToSkim(skims_ref_file))
        #run
        mma.summarizeAccessibility(skim_set_obj, lu_table, lu_table_id,
                               lu_table_activity_fields, out_table,
                               decays=decays)
    
