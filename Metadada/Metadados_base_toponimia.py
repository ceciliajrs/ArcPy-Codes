import arcpy
from arcpy import metadata as md
import os
import xml.etree.ElementTree as ET
import string
import random


nomes_metadados_250 = {

    "Area": "Area_Indigena_1M_250.shp.xml",
    "Hidreletrica": "Hidreletrica_1M_250.shp.xml",
    "Hidrografia": "Hidrografia_250.shp.xml",
    "Localidades": "Localidades_1M_250.shp.xml",
    "Rodovias": "Rodovias_1M_250.shp.xml",
    "Sedes": "Sedes_Municipais_1M_250.shp.xml",
    "Unidades": "UC_1M_250.shp.xml",

}

titulos_metadados_250 = {

    "Area": "Toponímias de Área Indígena",
    "Hidreletrica": "Toponímias de Hidreletrica",
    "Hidrografia": "Toponímias de Hidrografia",
    "Localidades": "Toponímias de Localidades",
    "Rodovias": "Toponímias de Rodovias",
    "Sedes": "Toponímias de Sedes Municipais",
    "Unidades": "Toponímias de Unidades de Conservação",

}

xslt_temp = r""
xslt_style = r".\remove geoprocessing history.xslt"

Base = r""

metadado_local = r""


####################################################################
#                   FILE IDENTIFIER


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


####################################################################


arcpy.env.workspace = Base
featuredatasets = arcpy.ListDatasets()
for dataset in featuredatasets:
    if dataset != "Bases":
        if dataset.endswith("GCS"):
            arcpy.env.workspace = os.path.join(Base, dataset)
            featureclasses = arcpy.ListFeatureClasses()
            for fc in featureclasses:
                if len(fc.split("_")) >= 3:
                    if fc.split("_")[-3] == "Toponimia":
                        if fc.startswith("Grade"):
                            pass
                        elif fc.startswith("Hidrografia"):
                            # if fc == "Hidrografia_Toponimia_362_UTM23S":
                            #     pass
                            # else:
                            print(fc)
                            fc_metadata = md.Metadata(fc)
                            fc_1 = fc.split("_")[0]
                            metadado_base_path = os.path.join(metadado_local, nomes_metadados_250[fc_1])
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
                            if len(dataset.split("_")) == 3:
                                num_dataset1 = fc.split("_")[-2]
                                num_dataset2 = fc.split("_")[-3]
                                proj = fc.split("_")[-1]
                                title_metadado = "F" + num_dataset2 + " e " + num_dataset1 + " - " + titulos_metadados_250[fc_1] + " (" + proj + ")"
                                fc_metadata.title = title_metadado
                                print(title_metadado)
                            elif len(dataset.split("_")) == 2:
                                num_dataset1 = fc.split("_")[-2]
                                proj = fc.split("_")[-1]
                                title_metadado = "F" + num_dataset1 + " - " + titulos_metadados_250[fc_1] + " (" + proj + ")"
                                fc_metadata.title = title_metadado
                                print(title_metadado)
                            fc_metadata.save()
                        else:
                            print(fc)
                            fc_metadata = md.Metadata(fc)
                            fc_2 = fc.split("_")[0]
                            metadado_base_path = os.path.join(metadado_local, nomes_metadados_250[fc_2])
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
                            num_dataset = fc.split("_")[-2]
                            proj = fc.split("_")[-1]
                            title_metadado = "F" + num_dataset + " - " + titulos_metadados_250[fc_2] + " (" + proj + ")"
                            fc_metadata.title = title_metadado
                            print(title_metadado)
                            fc_metadata.save()
