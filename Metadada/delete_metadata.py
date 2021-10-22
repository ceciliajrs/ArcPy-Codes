import arcpy
import os
from arcpy import metadata as md

Base = r""
vazio = r""

arcpy.env.workspace = Base
featuredatasets = arcpy.ListDatasets()
for dataset in featuredatasets:
    arcpy.env.workspace = os.path.join(Base, dataset)
    print(dataset)
    featureclasses = arcpy.ListFeatureClasses()
    for fc in featureclasses:
        if fc.startswith("Toponimia_Grade"):
            print(fc)
            fc_metadata = md.Metadata(fc)
            fc_metadata.importMetadata(vazio)
            fc_metadata.save()
