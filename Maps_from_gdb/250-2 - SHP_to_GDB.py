# -*- coding: utf-8 -*-

import arcpy
import os

########################################################

#           Dicionario cartas

carta = {

    "F172": "F172_Maraba_GCS",
    "F173": "F173_Imperatriz_GCS",
    "F199": "F199_Xambioa_GCS",
    "F200": "F200_Tocantinopolis_GCS",
    "F226": "F226_Araguaiana_GCS",
    "F227": "F227_Carolina_GCS",
    "F228": "F228_Balsas_GCS",
    "F252": "F252_Redencao_GCS",
    "F253": "F253_Conceicao_do_Araguaia_GCS",
    "F254": "F254_Itacaja_GCS",
    "F255": "F255_Passo_Fragoso_GCS",
    "F278": "F278_Santana_do_Araguaia_GCS",
    "F279": "F279_Miracema_do_Tocantins_GCS",
    "F280": "F280_Lizarda_GCS",
    "F281": "F281_Gilbues_GCS",
    "F303": "F303_Santa_Terezinha_GCS",
    "F304": "F304_Porto_Nacional_GCS",
    "F305": "F305_Ponte_Alta_do_Norte_GCS",
    "F306": "F306_Corrente_GCS",
    "F323": "F323_Sao_Felix_do_Araguaia_GCS",
    "F324": "F324_Gurupi_GCS",
    "F325": "F325_Dianopolis_GCS",
    "F326": "F326_Formosa_do_Rio_Preto_GCS",
    "F343": "F343_Araguacu_GCS",
    "F344": "F344_Alvorada_GCS",
    "F345": "F345_Arraias_GCS",
    "F346": "F346_Barreiras_GCS",
    "F360": "F360_Sao_Miguel_do_Araguaia_GCS",
    "F361": "F361_Porangatu_GCS",
    "F362": "F362_Campos_Belos_GCS"

}

########################################################

#           Dicionario cartas UTM

carta_UTM = {

    "172": "F172_Maraba_UTM22S",
    "173": "F173_Imperatriz_UTM23S",
    "199": "F199_Xambioa_UTM22S",
    "200": "F200_Tocantinopolis_UTM23S",
    "226": "F226_Araguaiana_UTM22S",
    "227": "F227_Carolina_UTM23S",
    "228": "F228_Balsas_UTM23S",
    "252": "F252_Redencao_UTM22S",
    "253": "F253_Conceicao_do_Araguaia_UTM22S",
    "254": "F254_Itacaja_UTM23S",
    "255": "F255_Passo_Fragoso_UTM23S",
    "278": "F278_Santana_do_Araguaia_UTM22S",
    "279": "F279_Miracema_do_Tocantins_UTM22S",
    "280": "F280_Lizarda_UTM23S",
    "281": "F281_Gilbues_UTM23S",
    "303": "F303_Santa_Terezinha_UTM22S",
    "304": "F304_Porto_Nacional_UTM22S",
    "305": "F305_Ponte_Alta_do_Norte_UTM23S",
    "306": "F306_Corrente_UTM23S",
    "323": "F323_Sao_Felix_do_Araguaia_UTM22S",
    "324": "F324_Gurupi_UTM22S",
    "325": "F325_Dianopolis_UTM23S",
    "326": "F326_Formosa_do_Rio_Preto_UTM23S",
    "343": "F343_Araguacu_UTM22S",
    "344": "F344_Alvorada_UTM22S",
    "345": "F345_Arraias_UTM23S",
    "346": "F346_Barreiras_UTM23S",
    "360": "F360_Sao_Miguel_do_Araguaia_UTM22S",
    "361": "F361_Porangatu_UTM22S",
    "362": "F362_Campos_Belos_UTM23S"

}

######################################################

path_local = r"..."
path_recortes_grid = os.path.join(path_local, "01_PROCESSAMENTO", "02_GDB", "TEMP")
path_gdb = r"..."

GRID = r"..."

# # Clip no Grid
# arcpy.env.workspace = os.path.join(path_gdb, "TO_250")
# shp_list1 = arcpy.ListFeatureClasses()
# for fc in shp_list1:
#     print "Variavel: " + fc
#     name_shp = fc
#     name_shp1 = name_shp.split("_")[0] + "_250_"
#     name_shp2 = "_GCS_" + name_shp.split("_")[3]
#     arcpy.env.workspace = GRID
#     grid_list = arcpy.ListFiles("*.shp")
#     for grid in grid_list:
#         print "Recorte: " + grid
#         name_grid = grid.split("_")[0][1:]
#         out_name_GCS = name_shp1 + name_grid + name_shp2
#         out_clip = os.path.join(path_recortes_grid, out_name_GCS)
#         arcpy.Clip_analysis(os.path.join(path_gdb, fc), grid, out_clip)
# print "Recortes GCS prontos!"
#
# # Salva recortes no GDB
# arcpy.env.workspace = path_recortes_grid
# shp_list2 = arcpy.ListFiles("*.shp")
# for shp2 in shp_list2:
#     print "Salvando " + shp2 + " no GDB"
#     sigla_carta = "F" + shp2.split("_")[2]
#     out_featureclass = os.path.join(path_gdb, carta[sigla_carta])
#     arcpy.FeatureClassToGeodatabase_conversion(shp2, out_featureclass)
#     arcpy.Delete_management(shp2)
# print "Tudo salvo no GDB"

# Projeta em UTM e salva em outro dataset
arcpy.env.workspace = path_gdb
featuredatasets = arcpy.ListDatasets()
print "Reprojetando e salvando em UTM..."
for dataset2 in featuredatasets:
    print "Dataset: " + dataset2
    arcpy.env.workspace = os.path.join(path_gdb, dataset2)
    if dataset2.endswith("GCS"):
        arcpy.env.workspace = os.path.join(path_gdb, dataset2)
        featureclasses = arcpy.ListFeatureClasses()
        for feature in featureclasses:
            feature_split = feature.split("_")
            num_carta = feature_split[2]
            dataset_UTM = carta_UTM[num_carta]
            print "Dataset UTM: " + dataset_UTM
            print feature
            proj_UTM = dataset_UTM.split("_")[-1]
            output_name_UTM = feature_split[0] + "_250_" + feature_split[2] + "_" + proj_UTM + "_" + feature_split[4]
            out_proj_UTM = os.path.join(path_gdb, dataset_UTM, output_name_UTM)
            if proj_UTM == "UTM22S":
                arcpy.Project_management(feature, out_proj_UTM, "PROJCS['SIRGAS_2000_UTM_Zone_22S',GEOGCS['GCS_SIRGAS_2000',DATUM['D_SIRGAS_2000',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',10000000.0],PARAMETER['Central_Meridian',-51.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]", '#', "GEOGCS['GCS_SIRGAS_2000',DATUM['D_SIRGAS_2000',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]", 'NO_PRESERVE_SHAPE', '#', 'NO_VERTICAL')
            elif proj_UTM == "UTM23S":
                arcpy.Project_management(feature, out_proj_UTM, "PROJCS['SIRGAS_2000_UTM_Zone_23S',GEOGCS['GCS_SIRGAS_2000',DATUM['D_SIRGAS_2000',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',10000000.0],PARAMETER['Central_Meridian',-45.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]", '#', "GEOGCS['GCS_SIRGAS_2000',DATUM['D_SIRGAS_2000',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]", 'NO_PRESERVE_SHAPE', '#', 'NO_VERTICAL')
print "Reprojeções salvas!"

