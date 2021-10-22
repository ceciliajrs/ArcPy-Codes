import arcpy
import os

#           Dicionario cartas UTM


carta_UTM = {

    "172": "F172_UTM22S",
    "173": "F173_UTM23S",
    "199": "F199_UTM22S",
    "200": "F200_UTM23S",
    "226": "F226_UTM22S",
    "227": "F227_228_UTM23S",
    "228": "F227_228_UTM23S",
    "252": "F252_253_UTM22S",
    "253": "F252_253_UTM22S",
    "254": "F254_255_UTM23S",
    "255": "F254_255_UTM23S",
    "278": "F278_UTM22S",
    "279": "F279_UTM22S",
    "280": "F280_281_UTM23S",
    "281": "F280_281_UTM23S",
    "303": "F303_UTM22S",
    "304": "F304_UTM22S",
    "305": "F305_UTM23S",
    "306": "F306_UTM23S",
    "323": "F323_UTM22S",
    "324": "F324_UTM22S",
    "325": "F325_UTM23S",
    "326": "F326_UTM23S",
    "343": "F343_360_UTM22S",
    "360": "F343_360_UTM22S",
    "344": "F344_UTM22S",
    "345": "F345_UTM23S",
    "346": "F346_UTM23S",
    "361": "F361_UTM22S",
    "362": "F362_UTM23S"

}


path_local = r""
path_recortes_grid = r""
camada_gdb = r""

GRID = r""

gdb_250 = r""

arcpy.env.workspace = gdb_250
featuredatasets = arcpy.ListDatasets()
for dataset in featuredatasets:
    if dataset.endswith("GCS"):
        arcpy.env.workspace = os.path.join(gdb_250, dataset)
        featureclasses = arcpy.ListFeatureClasses()
        for fc in featureclasses:
            if fc.startswith("Localidades"):
                carta = dataset.split("_")[0][1:]
                print carta
                dataset_UTM = carta_UTM[carta]
                proj_UTM = dataset_UTM.split("_")[-1]
                out_name_UTM = "Localidades_" + carta + "_" + proj_UTM
                print out_name_UTM
                out_proj_UTM = os.path.join(path_local, dataset_UTM, out_name_UTM)
                if proj_UTM == "UTM22S":
                    arcpy.Project_management(fc, out_proj_UTM, "PROJCS['SIRGAS_2000_UTM_Zone_22S',GEOGCS['GCS_SIRGAS_2000',DATUM['D_SIRGAS_2000',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',10000000.0],PARAMETER['Central_Meridian',-51.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]", '#', "GEOGCS['GCS_SIRGAS_2000',DATUM['D_SIRGAS_2000',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]", 'NO_PRESERVE_SHAPE', '#', 'NO_VERTICAL')
                elif proj_UTM == "UTM23S":
                    arcpy.Project_management(fc, out_proj_UTM, "PROJCS['SIRGAS_2000_UTM_Zone_23S',GEOGCS['GCS_SIRGAS_2000',DATUM['D_SIRGAS_2000',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',10000000.0],PARAMETER['Central_Meridian',-45.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]", '#', "GEOGCS['GCS_SIRGAS_2000',DATUM['D_SIRGAS_2000',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]", 'NO_PRESERVE_SHAPE', '#', 'NO_VERTICAL')