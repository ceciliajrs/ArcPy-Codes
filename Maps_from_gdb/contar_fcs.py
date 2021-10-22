import arcpy
import os

gdb = r""


arcpy.env.workspace = gdb
featuredatasets = arcpy.ListDatasets()
for dataset in featuredatasets:
    arcpy.env.workspace = os.path.join(gdb, dataset)
    featureclasses = arcpy.ListFeatureClasses()
    for fc in featureclasses:
        print fc
        arcpy.Delete_management(fc)



