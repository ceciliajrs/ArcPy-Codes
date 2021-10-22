# -*- coding: utf-8 -*-

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

#            LIST FEATURE CLASSES IN A GDB


def list_fcs_in_gdb(input_gdb):
    arcpy.env.workspace = input_gdb
    for feature_dataset in arcpy.ListDatasets():
        for feature_class in arcpy.ListFeatureClasses("", "", feature_dataset):
            yield(feature_class)


#############################################################

#          Dicionário variaveis


variaveis = {

    "Prec": "Precipitação",
    "OVrn": "Ocorrência de veranicos",
    "PChv": "Duração do período chuvoso",
    "DChv": "Dias chuvosos",
    "ISec": "Índice de seca",
    "TMax": "Temperatura máxima",
    "TMin": "Temperatura mínima",
    "TMed": "Temperatura média",
    "IHid": "Índice hídrico",
    "Umid": "Umidade relativa do ar",
    "Insl": "Insolação",
    "Nebl": "Nebulosidade",
    "RdSG": "Radiação solar global",
    "Evap": "Evaporação",
    "EtoR": "Evapotranspiração de referência",
    "EHid": "Excedente hídrico",
    "DHid": "Deficiência hídrica",
    "RClm": "Regionalização climática"

}

##############################################################

#           Dicionario meses do ano


periodo = {

    "M01": "em janeiro",
    "M02": "em fevereiro",
    "M03": "em março",
    "M04": "em abril",
    "M05": "em maio",
    "M06": "em junho",
    "M07": "em julho",
    "M08": "em agosto",
    "M09": "em setembro",
    "M10": "em outubro",
    "M11": "em novembro",
    "M12": "em dezembro",
    "MM01": "média em janeiro",
    "MM02": "média em fevereiro",
    "MM03": "média em março",
    "MM04": "média em abril",
    "MM05": "média em maio",
    "MM06": "média em junho",
    "MM07": "média em julho",
    "MM08": "média em agosto",
    "MM09": "média em setembro",
    "MM10": "média em outubro",
    "MM11": "média em novembro",
    "MM12": "média em dezembro",
    "MAnual": "anual",
    "Anual": "anual",
    "TAnual": "total anual",
    "Tri01": "no primeiro trimestre",
    "Tri02": "no segundo trimestre",
    "Tri03": "no terceiro trimestre",
    "Tri04": "no quarto trimestre",
    "T1990": "total em 1990",
    "T1991": "total em 1991",
    "T1992": "total em 1992",
    "T1993": "total em 1993",
    "T1994": "total em 1994",
    "T1995": "total em 1995",
    "T1996": "total em 1996",
    "T1997": "total em 1997",
    "T1998": "total em 1998",
    "T1999": "total em 1999",
    "T2000": "total em 2000",
    "T2001": "total em 2001",
    "T2002": "total em 2002",
    "T2003": "total em 2003",
    "T2004": "total em 2004",
    "T2005": "total em 2005",
    "T2006": "total em 2006",
    "T2007": "total em 2007",
    "T2008": "total em 2008",
    "T2009": "total em 2009",
    "T2010": "total em 2010",
    "T2011": "total em 2011",
    "T2012": "total em 2012",
    "T2013": "total em 2013",
    "T2014": "total em 2014",
    "T2015": "total em 2015",
    "T2016": "total em 2016",
    "T2017": "total em 2017",
    "T2018": "total em 2018",
    "T2019": "total em 2019",
    "1990a1991": "- 1990 a 1991",
    "1991a1992": "- 1991 a 1992",
    "1992a1993": "- 1992 a 1993",
    "1993a1994": "- 1993 a 1994",
    "1994a1995": "- 1994 a 1995",
    "1995a1996": "- 1995 a 1996",
    "1996a1997": "- 1996 a 1997",
    "1997a1998": "- 1997 a 1998",
    "1998a1999": "- 1998 a 1999",
    "1999a2000": "- 1999 a 2000",
    "2000a2001": "- 2000 a 2001",
    "2001a2002": "- 2001 a 2002",
    "2002a2003": "- 2002 a 2003",
    "2003a2004": "- 2003 a 2004",
    "2004a2005": "- 2004 a 2005",
    "2005a2006": "- 2005 a 2006",
    "2006a2007": "- 2006 a 2007",
    "2007a2008": "- 2007 a 2008",
    "2008a2009": "- 2008 a 2009",
    "2009a2010": "- 2009 a 2010",
    "2010a2011": "- 2010 a 2011",
    "2011a2012": "- 2011 a 2012",
    "2012a2013": "- 2012 a 2013",
    "2013a2014": "- 2013 a 2014",
    "2014a2015": "- 2014 a 2015",
    "2015a2016": "- 2015 a 2016",
    "2016a2017": "- 2016 a 2017",
    "2017a2018": "- 2017 a 2018",
    "2018a2019": "- 2018 a 2019",
    "1990": "em 1990",
    "1991": "em 1991",
    "1992": "em 1992",
    "1993": "em 1993",
    "1994": "em 1994",
    "1995": "em 1995",
    "1996": "em 1996",
    "1997": "em 1997",
    "1998": "em 1998",
    "1999": "em 1999",
    "2000": "em 2000",
    "2001": "em 2001",
    "2002": "em 2002",
    "2003": "em 2003",
    "2004": "em 2004",
    "2005": "em 2005",
    "2006": "em 2006",
    "2007": "em 2007",
    "2008": "em 2008",
    "2009": "em 2009",
    "2010": "em 2010",
    "2011": "em 2011",
    "2012": "em 2012",
    "2013": "em 2013",
    "2014": "em 2014",
    "2015": "em 2015",
    "2016": "em 2016",
    "2017": "em 2017",
    "2018": "em 2018",
    "2019": "em 2019",

}

#######################################################

#          Dicionário dataset


datasets = {

    "Prec": "Precipitacao",
    "OVrn": "Veranicos",
    "PChv": "Precipitacao",
    "DChv": "Precipitacao",
    "ISec": "Indice_Seca",
    "TMax": "Temperatura",
    "TMin": "Temperatura",
    "TMed": "Temperatura",
    "Umid": "Umidade",
    "Insl": "Insolacao",
    "Nebl": "Nebulosidade",
    "IHid": "Indice_Hidrico",
    "RdSG": "Radiacao_Solar_Global",
    "Evap": "Evaporacao",
    "EtoR": "Evapotranspiracao",
    "EHid": "Excedente_hidrico",
    "DHid": "Deficiencia_hidrica",
    "RClm": "Regionalizacao_climatica"

}

###############################################

#          Dicionário geometria


geometrias = {

    "a": "polígono",
    "l": "linha",

}

###############################################

nome_base = ".shp"

tags_texto = ""

summary_texto = ""

xslt_temp = r""
xslt_style = r"C:\..\remove geoprocessing history.xslt"

gdb = r""
gdb_escala = gdb.split("\\")[-1]

caminho_base = r""

if gdb_escala.startswith("2"):
    variavel_nome = nome_base.split("_")[0]
    #dataset = os.path.join(gdb, datasets[variavel_nome] + "_GCS")
    #print(dataset)
    arcpy.env.workspace = gdb
    fds = arcpy.ListDatasets()
    for fd in fds:
        arcpy.env.workspace = os.path.join(gdb, fd)
        featureclasses = arcpy.ListFeatureClasses()
        for fc in featureclasses:
            if fc[:4] == variavel_nome:
                xml_base_1 = os.path.join(caminho_base, nome_base + ".xml")

                fc_0_metadata = md.Metadata(fc)
                fc_0_metadata.saveAsUsingCustomXSLT(os.path.join(xslt_temp, fc + ".xml"), xslt_style)
                fc_0_temp = md.Metadata(xslt_temp)
                fc_0_metadata.copy(fc_0_temp)
                fc_0_metadata.save()

                # nome do metadado
                fc_split = fc.split("_")
                nome_variavel = fc_split[0][:4]
                nome_temporal = fc_split[0][4:]
                nome_geometria = fc_split[-1]
                if nome_variavel == "RClm":
                    nome_metadado_sem_geom = variaveis[nome_variavel]
                    nome_metadado_com_geom = variaveis[nome_variavel] + " - " + geometrias[nome_geometria] + " (1.000.000)"
                else:
                    nome_metadado_sem_geom = variaveis[nome_variavel] + " " + periodo[nome_temporal]
                    nome_metadado_com_geom = variaveis[nome_variavel] + " " + periodo[nome_temporal] + " - " + geometrias[nome_geometria] + " (1.000.000)"

                # gerador do ID
                new_ID = id_generator(8) + "-" + id_generator(4) + "-" + id_generator(4) + "-" + id_generator(4) + "-" + id_generator(12)
                tree_1 = ET.parse(xml_base_1)
                root = tree_1.getroot()
                root.find("mdFileID").text = new_ID
                root.findall("./dataIdInfo/searchKeys/keyword")[0].text = "1. " + nome_metadado_sem_geom + ". " + tags_texto
                root.findall("./dataIdInfo/idPurp")[0].text = "" + nome_metadado_sem_geom.lower() + "" + summary_texto
                tree_1.write(xml_base_1)

                # importando metadado
                fc_metadata = md.Metadata(fc)
                fc_metadata.importMetadata(os.path.join(caminho_base, nome_base))
                fc_metadata.save()
                fc_metadata.synchronize('OVERWRITE')
                fc_metadata.title = nome_metadado_com_geom
                fc_metadata.save()
                print(fc, new_ID)
