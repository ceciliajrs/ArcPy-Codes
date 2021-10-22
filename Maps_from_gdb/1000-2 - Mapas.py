# -*- coding: utf-8 -*-

import arcpy
import time
import os


########################################################

#         AUTOMATIZACAO PARA CARTAS 250.000

########################################################

#          Adicionar camada - Funcao


# def addcamada(camada_gdb, lyr_simbol):
#     updatelyr = arcpy.mapping.Layer(camada_gdb)
#     sourcelyr = arcpy.mapping.ListLayers(mxd, lyr_simbol, df)[0]
#     # arcpy.mapping.UpdateLayer(df, updatelyr, sourcelyr, False)
#     arcpy.mapping.AddLayer(df, updatelyr, "BOTTOM")


########################################################

#           Dicionario meses do ano


periodo = {
    "M01": "EM JANEIRO",
    "M02": "EM FEVEREIRO",
    "M03": "EM MARÇO",
    "M04": "EM ABRIL",
    "M05": "EM MAIO",
    "M06": "EM JUNHO",
    "M07": "EM JULHO",
    "M08": "EM AGOSTO",
    "M09": "EM SETEMBRO",
    "M10": "EM OUTUBRO",
    "M11": "EM NOVEMBRO",
    "M12": "EM DEZEMBRO",
    "MM01": "MÉDIA EM JANEIRO",
    "MM02": "MÉDIA EM FEVEREIRO",
    "MM03": "MÉDIA EM MARÇO",
    "MM04": "MÉDIA EM ABRIL",
    "MM05": "MÉDIA EM MAIO",
    "MM06": "MÉDIA EM JUNHO",
    "MM07": "MÉDIA EM JULHO",
    "MM08": "MÉDIA EM AGOSTO",
    "MM09": "MÉDIA EM SETEMBRO",
    "MM10": "MÉDIA EM OUTUBRO",
    "MM11": "MÉDIA EM NOVEMBRO",
    "MM12": "MÉDIA EM DEZEMBRO",
    "MAnual": "ANUAL",
    "Anual": "ANUAL",
    "TAnual": "TOTAL ANUAL",
    "Tri01": "NO PRIMEIRO TRIMESTRE",
    "Tri02": "NO SEGUNDO TRIMESTRE",
    "Tri03": "NO TERCEIRO TRIMESTRE",
    "Tri04": "NO QUARTO TRIMESTRE",
    "Echuva": "- ESTAÇÃO DE CHUVA",
    "Eseca": "- ESTAÇÃO DE SECA",
    "T1990": "TOTAL EM 1990",
    "T1991": "TOTAL EM 1991",
    "T1992": "TOTAL EM 1992",
    "T1993": "TOTAL EM 1993",
    "T1994": "TOTAL EM 1994",
    "T1995": "TOTAL EM 1995",
    "T1996": "TOTAL EM 1996",
    "T1997": "TOTAL EM 1997",
    "T1998": "TOTAL EM 1998",
    "T1999": "TOTAL EM 1999",
    "T2000": "TOTAL EM 2000",
    "T2001": "TOTAL EM 2001",
    "T2002": "TOTAL EM 2002",
    "T2003": "TOTAL EM 2003",
    "T2004": "TOTAL EM 2004",
    "T2005": "TOTAL EM 2005",
    "T2006": "TOTAL EM 2006",
    "T2007": "TOTAL EM 2007",
    "T2008": "TOTAL EM 2008",
    "T2009": "TOTAL EM 2009",
    "T2010": "TOTAL EM 2010",
    "T2011": "TOTAL EM 2011",
    "T2012": "TOTAL EM 2012",
    "T2013": "TOTAL EM 2013",
    "T2014": "TOTAL EM 2014",
    "T2015": "TOTAL EM 2015",
    "T2016": "TOTAL EM 2016",
    "T2017": "TOTAL EM 2017",
    "T2018": "TOTAL EM 2018",
    "T2019": "TOTAL EM 2019",
    "1990a1991": "- 1990 A 1991",
    "1991a1992": "- 1991 A 1992",
    "1992a1993": "- 1992 A 1993",
    "1993a1994": "- 1993 A 1994",
    "1994a1995": "- 1994 A 1995",
    "1995a1996": "- 1995 A 1996",
    "1996a1997": "- 1996 A 1997",
    "1997a1998": "- 1997 A 1998",
    "1998a1999": "- 1998 A 1999",
    "1999a2000": "- 1999 A 2000",
    "2000a2001": "- 2000 A 2001",
    "2001a2002": "- 2001 A 2002",
    "2002a2003": "- 2002 A 2003",
    "2003a2004": "- 2003 A 2004",
    "2004a2005": "- 2004 A 2005",
    "2005a2006": "- 2005 A 2006",
    "2006a2007": "- 2006 A 2007",
    "2007a2008": "- 2007 A 2008",
    "2008a2009": "- 2008 A 2009",
    "2009a2010": "- 2009 A 2010",
    "2010a2011": "- 2010 A 2011",
    "2011a2012": "- 2011 A 2012",
    "2012a2013": "- 2012 A 2013",
    "2013a2014": "- 2013 A 2014",
    "2014a2015": "- 2014 A 2015",
    "2015a2016": "- 2015 A 2016",
    "2016a2017": "- 2016 A 2017",
    "2017a2018": "- 2017 A 2018",
    "2018a2019": "- 2018 A 2019",
    "1990": "EM 1990",
    "1991": "EM 1991",
    "1992": "EM 1992",
    "1993": "EM 1993",
    "1994": "EM 1994",
    "1995": "EM 1995",
    "1996": "EM 1996",
    "1997": "EM 1997",
    "1998": "EM 1998",
    "1999": "EM 1999",
    "2000": "EM 2000",
    "2001": "EM 2001",
    "2002": "EM 2002",
    "2003": "EM 2003",
    "2004": "EM 2004",
    "2005": "EM 2005",
    "2006": "EM 2006",
    "2007": "EM 2007",
    "2008": "EM 2008",
    "2009": "EM 2009",
    "2010": "EM 2010",
    "2011": "EM 2011",
    "2012": "EM 2012",
    "2013": "EM 2013",
    "2014": "EM 2014",
    "2015": "EM 2015",
    "2016": "EM 2016",
    "2017": "EM 2017",
    "2018": "EM 2018",
    "2019": "EM 2019",
    "S": "SIMPLIFICADA",
    "K": "KOPPEN"
}

#######################################################

#          Dicionário variaveis


variaveis = {
    "Prec": "PRECIPITAÇÃO",
    "OVrn": "OCORRÊNCIA DE VERANICOS",
    "PChv": "DURAÇÃO DO PERÍODO CHUVOSO",
    "DChv": "DIAS CHUVOSOS",
    "ISec": "ÍNDICE DE SECA",
    "TMax": "TEMPERATURA MÁXIMA",
    "TMin": "TEMPERATURA MÍNIMA",
    "TMed": "TEMPERATURA MÉDIA",
    "Umid": "UMIDADE RELATIVA DO AR",
    "Insl": "INSOLAÇÃO",
    "Nebl": "NEBULOSIDADE",
    "RdSG": "RADIAÇÃO SOLAR GLOBAL",
    "Evap": "EVAPORAÇÃO",
    "EtoR": "EVAPOTRANSPIRAÇÃO DE REFERÊNCIA",
    "EHid": "EXCEDENTE HÍDRICO",
    "DHid": "DEFICIÊNCIA HÍDRICA",
    "RClm": "REGIONALIZAÇÃO CLIMÁTICA"

}

######################################################

#           Observacoes

# Verificar se o nome da Lyr/Simbologia esta igual ao que está no MXD base.
# Alterar local de saída conforme necessario para MXD 10.7, MXD 10.4 e PDF.

#######################################################

#           Auxiliares

path_local = os.path.join(r"")
path_to_gdb = r""
log = open(os.path.join(path_local, "SAIDA", "04_LOG", time.strftime("%H-%M_%d-%m") + ".txt"), "w")

#######################################################

linha_Lyr = "lyr_linha"
poligono_Lyr = "lyr_poligono_anual"
feature_dataset = "Insolacao_GCS"

######################################################

caminho_dataset = os.path.join(path_to_gdb, feature_dataset)
arcpy.env.workspace = caminho_dataset
featureclasses = arcpy.ListFeatureClasses()
for fc in featureclasses:
    if fc.startswith("InslT"):
    # if fc[4:].startswith("RdSGM"):
        mxd = arcpy.mapping.MapDocument(os.path.join(path_local, ".mxd"))
        fc_new = fc[:-2]
        sigla_carta = fc_new
        mxd.saveACopy(os.path.join(path_local, feature_dataset + ".mxd"))
        mxd = arcpy.mapping.MapDocument(os.path.join(path_local, feature_dataset + ".mxd"))
        mxd.relativePaths = True
        df = arcpy.mapping.ListDataFrames(mxd)[0]
        if fc.endswith("a"):
            continue
        else:
            matching = [s for s in featureclasses if fc_new in s]
            if matching[0].endswith("l"):
                linha1 = matching[0]
                poligono1 = matching[1]
            else:
                poligono1 = matching[0]
                linha1 = matching[1]
            print linha1, poligono1

            # Set Data Source
            updateLayer_lin = arcpy.mapping.ListLayers(mxd, linha_Lyr, df)[0]
            updateLayer_lin.replaceDataSource(path_to_gdb, "FILEGDB_WORKSPACE", linha1)
            updateLayer_lin.name = linha1
            updateLayer_pol = arcpy.mapping.ListLayers(mxd, poligono_Lyr, df)[0]
            updateLayer_pol.replaceDataSource(path_to_gdb, "FILEGDB_WORKSPACE", poligono1)
            updateLayer_pol.name = poligono1

        # Titulos
        variavel_temporal = fc_new[4:].split("_")[0]
        variavel_nome = fc_new[:4]
        variavel = arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT", "titulo")[0]
        variavel.text = "<BOL>{0}".format(variaveis[variavel_nome]) + " {0}</BOL>".format(periodo[variavel_temporal])
        variavel2 = arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT", "titulo2")[0]
        if variavel_temporal.startswith("TAnual"):
            variavel2.text = "MÉDIA DE 1990 A 2017"
        elif variavel_temporal.startswith("M"):
            variavel2.text = "MÉDIA DE 1990 A 2017"
        else:
            variavel2.text = "SOMA DOS MESES DO ANO"

        # Salvar em 10.7 e 10.4
        mxd.save()
        nome_salvar = fc_new.split("_")[0] + "_1M"
        print nome_salvar
        mxd.saveACopy(os.path.join(path_local, "SAIDA", "01_MXD", nome_salvar + ".mxd"), "10.4")
        mxd.saveACopy(os.path.join(path_local, "SAIDA", "03_MXD_10.7", nome_salvar + ".mxd"))

        # PDF, Log, Deleta MXD atual
        pdf_nome = os.path.join(path_local, "SAIDA", "02_PDF", nome_salvar)
        # arcpy.mapping.ExportToPDF(mxd, pdf_nome, resolution=500)
        del mxd
        print "Carta " + nome_salvar + " finalizada em " + time.strftime("%H-%M_%d-%m")
        print >> log, "Carta " + nome_salvar + " finalizada em " + time.strftime("%H-%M_%d-%m")
        arcpy.Delete_management(os.path.join(path_local, feature_dataset + ".mxd"))
log.close()


# # Label Isolinha
# layer_label = arcpy.mapping.ListLayers(mxd, linha1)[0]
# if layer_label.supports("LABELCLASSES"):
#     layer_label.showLabels = True

# # Remover Lyr com Simbologia
# remover_linha_lyr = arcpy.mapping.ListLayers(mxd, linha_Lyr, df)[0]
# arcpy.mapping.RemoveLayer(df, remover_linha_lyr)
# remover_poligono_lyr = arcpy.mapping.ListLayers(mxd, poligono_Lyr, df)[0]
# arcpy.mapping.RemoveLayer(df, remover_poligono_lyr)

# numero_layers = arcpy.mapping.ListLayers(mxd)
# print len(numero_layers)
# print >> log, len(numero_layers)
# addcamada(linha1, linha_Lyr)
# sourceLayer = arcpy.mapping.ListLayers(mxd, linha_Lyr, df)[0]
# arcpy.mapping.UpdateLayer(df, updateLayer, sourceLayer, True)
# addcamada(poligono1, poligono_Lyr)
# sourceLayer_pol = arcpy.mapping.ListLayers(mxd, poligono_Lyr, df)[0]
# arcpy.mapping.UpdateLayer(df, updateLayer_pol, sourceLayer_pol, True)
# numero_layers_depois = arcpy.mapping.ListLayers(mxd)
# print len(numero_layers_depois)
# print >> log, len(numero_layers_depois)