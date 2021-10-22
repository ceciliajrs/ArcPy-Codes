import arcpy
import os

gdb_path_250 = r''


arcpy.env.workspace = gdb_path_250
featuredatasets = arcpy.ListDatasets()
for dataset in featuredatasets:
    arcpy.env.workspace = os.path.join(gdb_path_250, dataset)
    featureclasses = arcpy.ListFeatureClasses()
    for fc in featureclasses:
        if fc.startswith("DChvMAnual"):
            print fc
            fc_end = fc[10:]
            new_name = "DChvTAnual" + fc_end
            print new_name
            arcpy.Rename_management(fc, new_name)

