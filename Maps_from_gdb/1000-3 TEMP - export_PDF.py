import arcpy
import os


local = os.path.join(r"")
local_mxd = os.path.join(local, "03_MXD_10.7")
local_pdf = os.path.join(local, "02_PDF")

arcpy.env.workspace = local_mxd
mxdlist = arcpy.ListFiles("*.mxd")
for mxd in mxdlist:
    if mxd.startswith("TMin"):
        caminho = os.path.join(local_mxd, mxd)
        name = mxd[:-4]
        print name
        mxd = arcpy.mapping.MapDocument(caminho)
        pdf_name = os.path.join(local_pdf, name)
        arcpy.mapping.ExportToPDF(mxd, pdf_name, resolution=500)
        print "Done"







