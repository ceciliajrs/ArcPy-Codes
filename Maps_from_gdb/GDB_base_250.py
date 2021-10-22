# -*- coding: utf-8 -*-

import arcpy
import os

########################################################

#           Dicionario cartas

carta = {

    "172": "F172_GCS",
    "173": "F173_GCS",
    "199": "F199_GCS",
    "200": "F200_GCS",
    "226": "F226_GCS",
    "227": "F227_228_GCS",
    "228": "F227_228_GCS",
    "252": "F252_253_GCS",
    "253": "F252_253_GCS",
    "254": "F254_255_GCS",
    "255": "F254_255_GCS",
    "278": "F278_GCS",
    "279": "F279_GCS",
    "280": "F280_281_GCS",
    "281": "F280_281_GCS",
    "303": "F303_GCS",
    "304": "F304_GCS",
    "305": "F305_GCS",
    "306": "F306_GCS",
    "323": "F323_GCS",
    "324": "F324_GCS",
    "325": "F325_GCS",
    "326": "F326_GCS",
    "343": "F343_360_GCS",
    "360": "F343_360_GCS",
    "344": "F344_GCS",
    "345": "F345_GCS",
    "346": "F346_GCS",
    "361": "F361_GCS",
    "362": "F362_GCS"

}

########################################################

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

######################################################

path_local = r""
path_recortes_grid = r""
camada_gdb = r""

GRID = r""

arcpy.env.workspace = GRID
grid_list = arcpy.ListFiles("*.shp")
for grid in grid_list:
    print "Recorte: " + grid
    dataset_num = grid.split("_")[0][1:]
    dataset = carta[dataset_num]
    end_name1 = grid[:-4]
    end_name2 = end_name1[1:]
    out_name_GCS = "Unidades_Conservacao_" + end_name2
    print out_name_GCS
    out_clip = os.path.join(path_local, dataset, out_name_GCS)
    arcpy.Clip_analysis(camada_gdb, grid, out_clip)
print "Recortes GCS prontos!"


arcpy.env.workspace = path_local
featuredatasets = arcpy.ListDatasets()
for dataset in featuredatasets:
    if dataset.endswith("GCS"):
        print dataset
        arcpy.env.workspace = os.path.join(path_local, dataset)
        fcs = arcpy.ListFeatureClasses()
        for fc in fcs:
            if fc.startswith("F"):
                pass
            else:
                if fc.split("_")[-3] != "Toponimia":
                    if fc.startswith("Unidades_Conservacao_"):
                        # print fc
                        result = arcpy.GetCount_management(fc)
                        count = int(result.getOutput(0))
                        print count
                        if count == 0:
                            print fc
                            arcpy.Delete_management(fc)

        # dataset_nome = dataset[1:]
        # nome_fc = "Area_Indigena_" + dataset_nome
        # print(nome_fc)
        # if arcpy.Exists(nome_fc):
        #     print("EXISTE")
        # else:
        #     if len(dataset.split("_")) == 2:
        #         nome_fc_toponimia0 = "Unidades_Conservacao_Toponimia_" + dataset_nome
        #         print nome_fc_toponimia0
        #         arcpy.Delete_management(nome_fc_toponimia0)
        #     elif len(dataset.split("_")) == 3:
        #         folha1 = dataset.split("_")[0][1:]
        #         folha2 = dataset.split("_")[1]
        #         nome_fc_toponimia1 = "Unidades_Conservacao_Toponimia_" + folha1 + "_GCS"
        #         nome_fc_toponimia2 = "Unidades_Conservacao_Toponimia_" + folha2 + "_GCS"
        #         print nome_fc_toponimia1
        #         print nome_fc_toponimia2
        #         arcpy.Delete_management(nome_fc_toponimia1)
        #         arcpy.Delete_management(nome_fc_toponimia2)



gdb_250 = r""
arcpy.env.workspace = gdb_250
featuredatasets = arcpy.ListDatasets()
for dataset in featuredatasets:
    if dataset.endswith("GCS"):
        arcpy.env.workspace = os.path.join(gdb_250, dataset)
        featureclasses = arcpy.ListFeatureClasses()
        for fc in featureclasses:
            if fc.startswith("F"):
                pass
            else:
                if fc.split("_")[-3] != "Toponimia":
                    if fc.startswith("Unidades_Conservacao_"):
                        carta = fc.split("_")[-2]
                        # carta2 = fc.split("_")[-3]
                        print carta
                        dataset_UTM = carta_UTM[carta]
                        proj_UTM = dataset_UTM.split("_")[-1]
                        out_name_UTM = "Unidades_Conservacao_" + carta + "_" + proj_UTM
                        print out_name_UTM
                        out_proj_UTM = os.path.join(path_local, dataset_UTM, out_name_UTM)
                        if proj_UTM == "UTM22S":
                            arcpy.Project_management(fc, out_proj_UTM, "PROJCS['SIRGAS_2000_UTM_Zone_22S',GEOGCS['GCS_SIRGAS_2000',DATUM['D_SIRGAS_2000',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',10000000.0],PARAMETER['Central_Meridian',-51.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]", '#', "GEOGCS['GCS_SIRGAS_2000',DATUM['D_SIRGAS_2000',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]", 'NO_PRESERVE_SHAPE', '#', 'NO_VERTICAL')
                        elif proj_UTM == "UTM23S":
                            arcpy.Project_management(fc, out_proj_UTM, "PROJCS['SIRGAS_2000_UTM_Zone_23S',GEOGCS['GCS_SIRGAS_2000',DATUM['D_SIRGAS_2000',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',10000000.0],PARAMETER['Central_Meridian',-45.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]", '#', "GEOGCS['GCS_SIRGAS_2000',DATUM['D_SIRGAS_2000',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]", 'NO_PRESERVE_SHAPE', '#', 'NO_VERTICAL')

