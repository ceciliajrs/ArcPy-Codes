# -*- coding: utf-8 -*-

import arcpy
import os

########################################################

#          Dicionario variaveis


variaveis = {
    "Prec": "Precipitacao_GCS",
    "OVrn": "Veranicos_GCS",
    "PChv": "Precipitacao_GCS",
    "DChv": "Precipitacao_GCS",
    "ISec": "Indice_Seca_GCS",
    "IHid": "Indice_Hidrico_GCS",
    "TMax": "Temperatura_GCS",
    "TMin": "Temperatura_GCS",
    "TMed": "Temperatura_GCS",
    "Umid": "Umidade_GCS",
    "Insl": "Insolacao_GCS",
    "Nebl": "Nebulosidade_GCS",
    "RdSG": "Radiacao_Solar_Global_GCS",
    "Evap": "Evaporacao_GCS",
    "EtoR": "Evapotranspiracao_GCS",
    "EHid": "Excedente_hidrico_GCS",
    "DHid": "Deficiencia_hidrica_GCS",
    "RClm": "Regionalizacao_climatica_GCS"

}

########################################################

shapes = r""
gdb = r""
TO = r""
variaveis_3_campos = ["Prec", "PChv", "Insl", "RdSG", "Evap", "EtoR", "RClm", "Umid", "Nebl", "DChv", "DHid", "ISec", "EHid", "IHid"]
# temperatura = ["TMax", "TMin", "TMed"]

# Realiza Clip e salva no GDB
arcpy.env.workspace = shapes
for root, dirs, files in os.walk(shapes):
    for shp in files:
        if shp.endswith(".shp"):
            nome = shp[:-4]
            arcpy.Clip_analysis(shp, TO, os.path.join(gdb, variaveis[shp[:4]], nome))
            print nome
        else:
            pass
print "Recortes prontos!"

# Altera o nome dos campos
arcpy.env.workspace = gdb
featuredatasets = arcpy.ListDatasets()
for dataset in featuredatasets:
    arcpy.env.workspace = os.path.join(gdb, dataset)
    featureclasses = arcpy.ListFeatureClasses()
    for fc in featureclasses:
        describe_fc = arcpy.Describe(fc)
        fc_new = fc[:4]
        if describe_fc.shapeType == "Polygon":
            if fc_new in variaveis_3_campos:
                #arcpy.AlterField_management(fc, "low_cont", "Min")
                #arcpy.AlterField_management(fc, "high_cont", "Max")
                arcpy.AlterField_management(fc, "range_cont", "Classe")
                print fc
            else:
                arcpy.AlterField_management(fc, "GRIDCode", "Valor")
                print fc
        else:
            arcpy.AlterField_management(fc, "Contour", "Valor")
            print fc
        # Deleta fields desnecessarios
        if len(arcpy.ListFields(fc, "Shape_Leng")) > 0:
            arcpy.DeleteField_management(fc, "Shape_Leng")
        elif len(arcpy.ListFields(fc, "Type")) > 0:
            arcpy.DeleteField_management(fc, "Type")
        elif len(arcpy.ListFields(fc, "gridcode")) > 0:
           arcpy.DeleteField_management(fc, "gridcode")