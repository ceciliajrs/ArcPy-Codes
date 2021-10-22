# -*- coding: utf-8 -*-

import arcpy
import os
import time

#####################################################

#              Juntar GDBs


path_local_1000 = "" 
path_local_250 = ""

path_to_gdb_base_1000 = r""
path_to_gdb_base_250 = r""

gdb_path_1000 = [

    # os.path.join(path_local_1000, "06-INSOLACAO", "01_PROCESSAMENTO", "02_GDB", "ANUAL", "1.000.000.gdb"),
    # os.path.join(path_local_1000, "16-VERANICO", "01_PROCESSAMENTO", "02_GDB", "1.000.000.gdb")

]

gdb_path_250 = [

    # os.path.join(path_local_250, "07-PRECIPITACAO", "01_PROCESSAMENTO", "02_GDB", "ANUAL", "250.000.gdb"),
    # os.path.join(path_local_250, "07-PRECIPITACAO", "01_PROCESSAMENTO", "02_GDB", "MENSAL", "250.000.gdb"),
    # os.path.join(path_local_250, "07-PRECIPITACAO", "01_PROCESSAMENTO", "02_GDB", "TRIMESTRAL", "250.000.gdb"),
    # os.path.join(path_local_250, "08-DIAS_CHUVA", "01_PROCESSAMENTO", "02_GDB", "ANUAL", "250.000.gdb"),
    # os.path.join(path_local_250, "08-DIAS_CHUVA", "01_PROCESSAMENTO", "02_GDB", "MENSAL", "250.000.gdb"),
    # os.path.join(path_local_250, "09-EVAPOTRANSPIRACAO", "01_PROCESSAMENTO", "02_GDB", "ANUAL", "250.000.gdb"),
    # os.path.join(path_local_250, "09-EVAPOTRANSPIRACAO", "01_PROCESSAMENTO", "02_GDB", "MENSAL", "250.000.gdb"),
    #
    #
    #
    #

]

# for gdb in gdb_path_1000:
#     print gdb
#     arcpy.env.workspace = gdb
#     featuredatasets = arcpy.ListDatasets()
#     for dataset in featuredatasets:
#         arcpy.env.workspace = os.path.join(gdb, dataset)
#         featureclasses = arcpy.ListFeatureClasses()
#         for fc in featureclasses:
#             arcpy.Copy_management(fc, os.path.join(path_to_gdb_base_1000, dataset, fc))
#             print fc + " copiado!"

for gdb in gdb_path_250:
    print gdb
    arcpy.env.workspace = gdb
    featuredatasets = arcpy.ListDatasets()
    for dataset in featuredatasets:
        if dataset.endswith("GCS"):
            pass
        elif dataset == "TO_250":
            pass
        else:
            arcpy.env.workspace = os.path.join(gdb, dataset)
            print dataset
            featureclasses = arcpy.ListFeatureClasses()
            for fc in featureclasses:
                arcpy.Copy_management(fc, os.path.join(path_to_gdb_base_250, dataset, fc))
                print fc + " copiado!"

print time.strftime("%H-%M_%d-%m")
