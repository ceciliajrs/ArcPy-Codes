import arcpy
from arcpy import metadata as md
import os
import xml.etree.ElementTree as ET
import string
import random

####################################################################
#                   FILE IDENTIFIER


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


####################################################################

nomes_metadata_1M = {

    "Area_Indigena": "Area_Indigena_1M_250.shp.xml",
    "Area_Indigena_Anno": "Area_Indigena_1M_250.shp.xml",
    "Ferrovias": "Ferrovias_1M_250.shp.xml",
    "Hidreletrica": "Hidreletrica_1M_250.shp.xml",
    "Hidreletrica_Anno": "Hidreletrica_1M_250.shp.xml",
    "Hidrografia_Unifilar": "Hidrografia_1M.shp.xml",
    "Limite_Estado": "Limite_Estado_1M.shp.xml",
    "Limite_Municipal_Linha": "Limites_Mun_Linha_1M_250.shp.xml",
    "Limite_Municipal_Poligono": "Limites_Mun_1M_250.shp.xml",
    "Localidades": "Localidades_1M_250.shp.xml",
    "Localidade_Anno": "Localidades_1M_250.shp.xml",
    "Massas_Agua": "Massas_dagua_1M.shp.xml",
    "Rodovias2018": "Rodovias_1M_250.shp.xml",
    "Sedes_Municipais": "Sedes_Municipais_1M_250.shp.xml",
    "Sedes_Municipais_Anno": "Sedes_Municipais_1M_250.shp.xml",
    "Toponimia_Hidrografia":"Hidrografia_1M.shp.xml",
    "Unidades_Conservacao": "UC_1M_250.shp.xml",
    "Unidade_Conservacao_Anno": "UC_1M_250.shp.xml",
    "Ilhas": "Hidrografia_1M.shp.xml",
    "Lagos_UHE": "Lagos_UHE_1M_250.shp.xml"

}

titulos_metadados_1M = {

    "Area_Indigena": "Área Indígena",
    "Area_Indigena_Anno": "Toponímias de Área Indígena",
    #"Brasil_Estado_Linha"
    "Ferrovias": "Ferrovias",
    "Hidreletrica": "Hidrelétrica",
    "Hidreletrica_Anno": "Toponímias de Hidrelétrica",
    "Hidrografia_Unifilar": "Hidrografia Unifiliar",
    "Limite_Estado": "Limite do Estado",
    "Limite_Municipal_Linha": "Limite Municipal - Linha",
    "Limite_Municipal_Poligono": "Limite Municipal - Polígono",
    "Localidades": "Localidades",
    "Localidade_Anno": "Toponímias de Localidades",
    "Massas_Agua": "Massas D'água",
    "Rodovias2018": "Rodovias",
    "Sedes_Municipais": "Sedes Municipais",
    "Sedes_Municipais_Anno": "Toponímias de Sedes Municipais",
    "Toponimia_Hidrografia":"Toponímias de Hidrografia",
    "Unidades_Conservacao": "Unidades de Conservação",
    "Unidade_Conservacao_Anno": "Toponímias de Unidades de Conservação",
    "Ilhas": "Ilhas",
    "Lagos_UHE": "Lagos - UHE"

}

nomes_metadados_250 = {

    "Area": "Area_Indigena_1M_250.shp.xml",
    "Articulacao": "Articulacao_250.shp.xml",
    "F":"Articulacao_250.shp.xml",
    "Ferrovias": "Ferrovias_1M_250.shp.xml",
    "Hidreletrica": "Hidreletrica_1M_250.shp.xml",
    "Hidrografia": "Hidrografia_250.shp.xml",
    "Limite": "Limites_Mun_Linha_1M_250.shp.xml",
    "Localidades": "Localidades_1M_250.shp.xml",
    "Massa": "Massas_dagua_250.shp.xml",
    "Rodovias": "Rodovias_1M_250.shp.xml",
    "Sedes": "Sedes_Municipais_1M_250.shp.xml",
    "UC": "UC_1M_250.shp.xml",
    "Lagos": "Lagos_UHE_1M_250.shp.xml"

}

titulos_metadados_250 = {

    "Area": "Área Indígena",
    "Articulacao": "Articulacao_250.shp.xml",
    "F":"Articulacao_250.shp.xml",
    "Ferrovias": "Ferrovias",
    "Hidreletrica": "Hidreletrica",
    "Hidrografia": "Hidrografia - Linha",
    "Limite": "Limite Municipal - Linha",
    "Localidades": "Localidades",
    "Massa": "Massas d'água",
    "Rodovias": "Rodovias",
    "Sedes": "Sedes Municipais",
    "UC": "Unidades de Conservação",
    "Lagos": "Lagos - UHE"

}

xslt_temp = r""
xslt_style = r".\remove geoprocessing history.xslt"

Base = r""

metadado_local = r""


arcpy.env.workspace = Base
featuredatasets = arcpy.ListDatasets()
for dataset in featuredatasets:
    arcpy.env.workspace = os.path.join(Base, dataset)
    print(dataset)
    sist_ref1 = dataset.split("_")[-1]
    featureclasses = arcpy.ListFeatureClasses()
    for fc in featureclasses:
        if len(fc.split("_")) >= 3:
            if fc.split("_")[-3] != "Toponimia":
                if fc.startswith(""):
                    print(fc)
                    fc_metadata = md.Metadata(fc)
                    metadado_base_path = os.path.join(metadado_local, ".shp.xml")

                    # IDENTIFICADOR
                    new_ID = id_generator(8) + "-" + id_generator(4) + "-" + id_generator(4) + "-" + id_generator(4) + "-" + id_generator(12)
                    tree_1 = ET.parse(metadado_base_path)
                    root5 = tree_1.getroot()
                    root5.find("mdFileID").text = new_ID
                    tree_1.write(metadado_base_path)

                    fc_metadata.importMetadata(metadado_base_path)
                    fc_metadata.save()
                    temp_path = os.path.join(xslt_temp, fc + ".xml")
                    fc_metadata.saveAsUsingCustomXSLT(temp_path, xslt_style)
                    fc_0_temp = md.Metadata(temp_path)
                    fc_metadata.copy(fc_0_temp)
                    fc_metadata.save()
                    folha1 = fc.split("_")[-2]
                    fc_metadata.title = "F" + folha1 + " - Unidades de Conservação (" + sist_ref1 + ")"
                    fc_metadata.save()

# arcpy.env.workspace = Base
# featuredatasets = arcpy.ListDatasets()
# for dataset in featuredatasets:
#     arcpy.env.workspace = os.path.join(Base, dataset)
#     print(dataset)
#     check_dataset = dataset.split("_")
#     if len(check_dataset) == 2:
#         featureclasses = arcpy.ListFeatureClasses()
#         for fc in featureclasses:
#             if fc.startswith("Toponimia_Grade"):
#                 pass
#             elif fc.startswith("Grade_Coordenadas"):
#                 pass
#             elif fc.startswith("F"):
#                 pass
#             elif fc.startswith("Hidrografia_Toponimia"):
#                 pass
#             else:
#                 print("Feature Class: " + fc)
#                 nome_fc = fc.split("_")[0]
#                 if nome_fc.startswith("F"):
#                     fc_metadata0 = md.Metadata(fc)
#                     metadado_base_path0 = os.path.join(metadado_local, "Articulacao_250.shp.xml")
#
#                     # IDENTIFICADOR
#                     new_ID0 = id_generator(8) + "-" + id_generator(4) + "-" + id_generator(4) + "-" + id_generator(4) + "-" + id_generator(12)
#                     tree_10 = ET.parse(metadado_base_path0)
#                     root0 = tree_10.getroot()
#                     root0.find("mdFileID").text = new_ID0
#                     tree_10.write(metadado_base_path0)
#
#                     fc_metadata0.importMetadata(metadado_base_path0)
#                     fc_metadata0.save()
#                     temp_path0 = os.path.join(xslt_temp, fc + ".xml")
#                     fc_metadata0.saveAsUsingCustomXSLT(temp_path0, xslt_style)
#                     fc_0_temp0 = md.Metadata(temp_path0)
#                     fc_metadata0.copy(fc_0_temp0)
#                     fc_metadata0.save()
#                     folha0 = dataset.split("_")[0]
#                     sist_ref0 = dataset.split("_")[-1]
#                     if fc.split("_")[1] == "Buffer":
#                         fc_metadata0.title = folha0 + " - " + "Articulação Buffer" + " (" + sist_ref0 + ")"
#                     else:
#                         fc_metadata0.title = folha0 + " - " + "Articulação" + " (" + sist_ref0 + ")"
#                     fc_metadata0.save()
#                 else:
#                     fc_metadata1 = md.Metadata(fc)
#                     metadado_base_path1 = os.path.join(metadado_local, nomes_metadados_250[nome_fc])
#
#                 # IDENTIFICADOR
#                 new_ID1 = id_generator(8) + "-" + id_generator(4) + "-" + id_generator(4) + "-" + id_generator(4) + "-" + id_generator(12)
#                 tree_11 = ET.parse(metadado_base_path1)
#                 root1 = tree_11.getroot()
#                 root1.find("mdFileID").text = new_ID1
#                 tree_11.write(metadado_base_path1)
#
#                 fc_metadata1.importMetadata(metadado_base_path1)
#                 fc_metadata1.save()
#                 temp_path1 = os.path.join(xslt_temp, fc + ".xml")
#                 fc_metadata1.saveAsUsingCustomXSLT(temp_path1, xslt_style)
#                 fc_0_temp1 = md.Metadata(temp_path1)
#                 fc_metadata1.copy(fc_0_temp1)
#                 fc_metadata1.save()
#                 folha1 = dataset.split("_")[0]
#                 sist_ref1 = dataset.split("_")[-1]
#                 check_toponimia = fc.split("_")[1]
#                 if check_toponimia == "Toponimia":
#                     fc_metadata1.title = folha1 + " - Toponímias de " + titulos_metadados_250[nome_fc] + " (" + sist_ref1 + ")"
#                 else:
#                     fc_metadata1.title = folha1 + " - " + titulos_metadados_250[nome_fc] + " (" + sist_ref1 + ")"
#                 fc_metadata1.save()
#
#     # DATASET FOLHAS DUPLAS
#     elif len(check_dataset) == 3:
#         featureclasses = arcpy.ListFeatureClasses()
#         for fc in featureclasses:
#             if fc.startswith("Toponimia_Grade"):
#                 pass
#             elif fc.startswith("Grade_Coordenadas"):
#                 pass
#             elif fc.startswith("F"):
#                 pass
#             elif fc.startswith("Hidrografia_Toponimia"):
#                 pass
#             else:
#                 print("Feature Class: " + fc)
#                 nome_fc = fc.split("_")[0]
#                 if nome_fc.startswith("F"):
#                     fc_metadata2 = md.Metadata(fc)
#                     metadado_base_path2 = os.path.join(metadado_local, "Articulacao_250.shp.xml")
#
#                     # IDENTIFICADOR
#                     new_ID2 = id_generator(8) + "-" + id_generator(4) + "-" + id_generator(4) + "-" + id_generator(4) + "-" + id_generator(12)
#                     tree_12 = ET.parse(metadado_base_path2)
#                     root2 = tree_12.getroot()
#                     root2.find("mdFileID").text = new_ID2
#                     tree_12.write(metadado_base_path2)
#
#                     fc_metadata2.importMetadata(metadado_base_path2)
#                     fc_metadata2.save()
#                     temp_path2 = os.path.join(xslt_temp, fc + ".xml")
#                     fc_metadata2.saveAsUsingCustomXSLT(temp_path2, xslt_style)
#                     fc_0_temp2 = md.Metadata(temp_path2)
#                     fc_metadata2.copy(fc_0_temp2)
#                     fc_metadata2.save()
#                     folha12 = dataset.split("_")[0]
#                     folha22 = dataset.split("_")[1]
#                     sist_ref2 = dataset.split("_")[-1]
#                     if fc.split("_")[1] == "Buffer":
#                         fc_metadata2.title = folha12 + " e " + folha22 + " - " + "Articulação Buffer" + " (" + sist_ref2 + ")"
#                     else:
#                         fc_metadata2.title = folha12 + " e " + folha22 + " - " + "Articulação" + " (" + sist_ref2 + ")"
#                     fc_metadata2.save()
#
#                 elif nome_fc == "Massa_Agua":
#                     fc_metadata3 = md.Metadata(fc)
#                     metadado_base_path3 = os.path.join(metadado_local, nomes_metadados_250[nome_fc])
#
#                     # IDENTIFICADOR
#                     new_ID3 = id_generator(8) + "-" + id_generator(4) + "-" + id_generator(4) + "-" + id_generator(4) + "-" + id_generator(12)
#                     tree_13 = ET.parse(metadado_base_path3)
#                     root3 = tree_13.getroot()
#                     root3.find("mdFileID").text = new_ID3
#                     tree_13.write(metadado_base_path3)
#
#                     fc_metadata3.importMetadata(metadado_base_path3)
#                     fc_metadata3.save()
#                     temp_path3 = os.path.join(xslt_temp, fc + ".xml")
#                     fc_metadata3.saveAsUsingCustomXSLT(temp_path3, xslt_style)
#                     fc_0_temp3 = md.Metadata(temp_path3)
#                     fc_metadata3.copy(fc_0_temp3)
#                     fc_metadata3.save()
#                     folha3 = fc.split("_")[-2]
#                     sist_ref3 = dataset.split("_")[-1]
#                     fc_metadata3.title = "F" + folha3 + " - " + titulos_metadados_250[nome_fc] + " (" + sist_ref3 + ")"
#                     fc_metadata3.save()
#
#                 elif nome_fc == "Hidrografia_Linha":
#                     fc_metadata3 = md.Metadata(fc)
#                     metadado_base_path3 = os.path.join(metadado_local, nomes_metadados_250[nome_fc])
#
#                     # IDENTIFICADOR
#                     new_ID3 = id_generator(8) + "-" + id_generator(4) + "-" + id_generator(4) + "-" + id_generator(4) + "-" + id_generator(12)
#                     tree_13 = ET.parse(metadado_base_path3)
#                     root3 = tree_13.getroot()
#                     root3.find("mdFileID").text = new_ID3
#                     tree_13.write(metadado_base_path3)
#
#                     fc_metadata3.importMetadata(metadado_base_path3)
#                     fc_metadata3.save()
#                     temp_path3 = os.path.join(xslt_temp, fc + ".xml")
#                     fc_metadata3.saveAsUsingCustomXSLT(temp_path3, xslt_style)
#                     fc_0_temp3 = md.Metadata(temp_path3)
#                     fc_metadata3.copy(fc_0_temp3)
#                     fc_metadata3.save()
#                     folha3 = fc.split("_")[-2]
#                     sist_ref3 = dataset.split("_")[-1]
#                     check_toponimia = fc.split("_")[1]
#                     if check_toponimia == "Toponimia":
#                         fc_metadata3.title = "F" + folha3 + " - Toponímias de " + titulos_metadados_250[nome_fc] + " (" + sist_ref3 + ")"
#                     else:
#                         fc_metadata3.title = "F" + folha3 + " - " + titulos_metadados_250[nome_fc] + " (" + sist_ref3 + ")"
#                     fc_metadata3.save()
#
#                 else:
#                     fc_metadata4 = md.Metadata(fc)
#                     metadado_base_path4 = os.path.join(metadado_local, nomes_metadados_250[nome_fc])
#
#                     # IDENTIFICADOR
#                     new_ID4 = id_generator(8) + "-" + id_generator(4) + "-" + id_generator(4) + "-" + id_generator(4) + "-" + id_generator(12)
#                     tree_14 = ET.parse(metadado_base_path4)
#                     root4 = tree_14.getroot()
#                     root4.find("mdFileID").text = new_ID4
#                     tree_14.write(metadado_base_path4)
#
#                     fc_metadata4.importMetadata(metadado_base_path4)
#                     fc_metadata4.save()
#                     temp_path4 = os.path.join(xslt_temp, fc + ".xml")
#                     fc_metadata4.saveAsUsingCustomXSLT(temp_path4, xslt_style)
#                     fc_0_temp4 = md.Metadata(temp_path4)
#                     fc_metadata4.copy(fc_0_temp4)
#                     fc_metadata4.save()
#                     folha14 = dataset.split("_")[0]
#                     folha24 = dataset.split("_")[1]
#                     sist_ref4 = dataset.split("_")[-1]
#                     fc_metadata4.title = folha14 + " e " + folha24 + " - " + titulos_metadados_250[nome_fc] + " (" + sist_ref4 + ")"
#                     fc_metadata4.save()

    # elif dataset == "Bases":
    #     featureclasses = arcpy.ListFeatureClasses()
    #     for fc in featureclasses:
    #         print("Feature Class: " + fc)
    #         fc_metadata5 = md.Metadata(fc)
    #         metadado_base_path5 = os.path.join(metadado_local, "Articulacao_250.shp.xml")
    #
    #         # IDENTIFICADOR
    #         new_ID5 = id_generator(8) + "-" + id_generator(4) + "-" + id_generator(4) + "-" + id_generator(4) + "-" + id_generator(12)
    #         tree_15 = ET.parse(metadado_base_path5)
    #         root5 = tree_15.getroot()
    #         root5.find("mdFileID").text = new_ID5
    #         tree_15.write(metadado_base_path5)
    #
    #         fc_metadata5.importMetadata(metadado_base_path5)
    #         fc_metadata5.save()
    #         temp_path5 = os.path.join(xslt_temp, fc + ".xml")
    #         fc_metadata5.saveAsUsingCustomXSLT(temp_path5, xslt_style)
    #         fc_0_temp5 = md.Metadata(temp_path5)
    #         fc_metadata5.copy(fc_0_temp5)
    #         fc_metadata5.save()
    #         if fc == "Articulacao_250mi":
    #             fc_metadata5.title = "Mapa Índice - Brasil"
    #         elif fc == "Articulacao_250mi_TO":
    #             fc_metadata5.title = "Mapa Índice - Tocantins"
    #         elif fc == "Articulacao_Folha":
    #             fc_metadata5.title = "Mapa Índice - Folha"
    #         fc_metadata5.save()





