import arcpy
import os
from arcpy import metadata as md

sde = r"..."

arcpy.env.workspace = sde
fds = arcpy.ListDatasets()
for fd in fds:
    arcpy.env.workspace = os.path.join(sde, fd)
    fcs = arcpy.ListFeatureClasses()
    for fc in fcs:
        fc_metadata = md.Metadata(fc)
        # md_titulo = fc_metadata.title
        md_desc = fc_metadata.description
        if md_desc is None:
            print(fd, fc, md_desc)
