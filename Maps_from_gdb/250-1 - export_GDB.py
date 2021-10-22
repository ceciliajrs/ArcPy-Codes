# -*- coding: utf-8 -*-

import arcpy
import os

#  Realiza Clip no shp com o estado do TO e muda o nome das colunas na tabela de atributos.

# path_local = os.path.join(r"...")
path_shapes = r"..."
gdb_final = r"..."

TO = r"..."

# Clip no TO
arcpy.env.workspace = path_shapes
shp_list0 = arcpy.ListFiles("*.shp")
for shp in shp_list0:
    nome = shp[:-4]
    arcpy.Clip_analysis(shp, TO, os.path.join(gdb_final, nome))
    print nome
print "Recortes TO prontos!"

variaveis_3_campos = ["Prec", "PChv", "EtoR", "OVrn"]
arcpy.env.workspace = gdb_final
featureclasses = arcpy.ListFeatureClasses()
for fc in featureclasses:
    print "Camada: " + fc
    describe_fc = arcpy.Describe(fc)
    if describe_fc.shapeType == "Polygon":
        fc_new = fc[:4]
        if fc_new in variaveis_3_campos:
            arcpy.AlterField_management(fc, "low_cont", "Min")
            arcpy.AlterField_management(fc, "high_cont", "Max")
            arcpy.AlterField_management(fc, "range_cont", "Classe")
            print "Poligono Count: " + fc
        else:
            arcpy.AlterField_management(fc, "GRIDCode", "Valor")
            print "Poligono Valor: " + fc
    else:
        arcpy.AlterField_management(fc, "Contour", "Valor")
        print "Linha: " + fc
    # Deleta fields desnecessarios
    if len(arcpy.ListFields(fc, "Shape_Leng")) > 0:
        arcpy.DeleteField_management(fc, "Shape_Leng")
    elif len(arcpy.ListFields(fc, "Type")) > 0:
        arcpy.DeleteField_management(fc, "Type")

print "Campos prontos!"
