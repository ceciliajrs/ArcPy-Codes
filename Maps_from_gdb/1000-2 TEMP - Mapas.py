# -*- coding: utf-8 -*-

import arcpy
import time
import os


########################################################

#         AUTOMATIZACAO PARA CARTAS 1.000.000 - TEMPERATURA

########################################################

#          Adicionar camada - Funcao


def addcamada(camada_gdb, lyr_simbol):
    updatelyr = arcpy.mapping.Layer(camada_gdb)
    sourcelyr = arcpy.mapping.ListLayers(mxd, lyr_simbol, df)[0]
    arcpy.mapping.UpdateLayer(df, updatelyr, sourcelyr, True)
    arcpy.mapping.AddLayer(df, updatelyr, "BOTTOM")


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
    "MAnual": "ANUAL",
    "Anual": "ANUAL",
    "T01": "- PRIMEIRO TRIMESTRE",
    "T02": "- SEGUNDO TRIMESTRE",
    "T03": "- TERCEIRO TRIMESTRE",
    "T04": "- QUARTO TRIMESTRE",
    "Echuva": "- ESTAÇÃO DE CHUVA",
    "Eseca": "- ESTAÇÃO DE SECA",
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
    "Prec": "PRECIPITAÇÃO PLUVIOMÉTRICA",
    "OVrn": "OCORRÊNCIA DE VERANICOS",
    "PChv": "PERÍODO DE CHUVA",
    "DChv": "NÚMERO DE DIAS DE CHUVA",
    "ISec": "ÍNDICE DE SECA",
    "IHid": "ÍNDICE HÍDRICO",
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

# Adicionar camada de Isolinhas antes de poligonos SEMPRE!
# Linha1 e Poligono1 sao camadas da carta maior. Linha2 e Poligono2 são camadas da carta menor.
# Linha1 da nome ao mapa.
# Verificar se o nome da Lyr/Simbologia esta igual ao que está no MXD base.
# Alterar local de saída conforme necessario para MXD 10.7, MXD 10.4 e PDF.

#######################################################

#           Auxiliares

path_local = os.path.join(r"")
path_to_gdb = os.path.join(r"")
log = open(os.path.join(path_local, "SAIDA", "04_LOG", time.strftime("%H-%M_%d-%m") + ".txt"), "w")

#######################################################

poligono_Lyr = "lyr_poligono"
feature_dataset = "Excedente_hidrico_GCS"

######################################################

caminho_dataset = os.path.join(path_to_gdb, feature_dataset)
arcpy.env.workspace = caminho_dataset
featureclasses = arcpy.ListFeatureClasses()
count = 0
for fc in featureclasses:
    if fc.startswith("EHid"):
        mxd = arcpy.mapping.MapDocument(os.path.join(path_local, ".mxd"))
        fc_new = fc[:-2]
        print fc
        count += 1
        sigla_carta = fc_new
        mxd.saveACopy(os.path.join(path_local, feature_dataset + str(count) + ".mxd"))
        mxd = arcpy.mapping.MapDocument(os.path.join(path_local, feature_dataset + str(count) + ".mxd"))
        mxd.relativePaths = True
        df = arcpy.mapping.ListDataFrames(mxd)[0]
        numero_layers = arcpy.mapping.ListLayers(mxd)
        print len(numero_layers)
        print >> log, len(numero_layers)
        poligono1 = fc
        addcamada(poligono1, poligono_Lyr)
        numero_layers_depois = arcpy.mapping.ListLayers(mxd)
        print len(numero_layers_depois)
        print >> log, len(numero_layers_depois)

        # Remover Lyr com Simbologia
        remover_poligono_lyr = arcpy.mapping.ListLayers(mxd, poligono_Lyr, df)[0]
        arcpy.mapping.RemoveLayer(df, remover_poligono_lyr)
        print "Removeu Lyr"

        # Titulo Variavel
        variavel_temporal = fc_new.split("_")[0][4:]
        variavel_nome = fc_new[:4]
        variavel = arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT", "titulo")[0]
        if variavel_temporal == "":
            variavel.text = "<BOL>{0}</BOL>".format(variaveis[variavel_nome])
        else:
            variavel.text = "<BOL>{0}".format(variaveis[variavel_nome]) + " {0}</BOL>".format(periodo[variavel_temporal])

        variavel2 = arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT", "titulo2")[0]
        # variavel2.text = "MÉDIA DE 1990 A 2019"
        if variavel_temporal.startswith("MAnual"):
            variavel2.text = "MÉDIA DE 1990 A 2019"
        elif variavel_temporal.startswith("M"):
            variavel2.text = "MÉDIA DE 1990 A 2019"
        # elif variavel_temporal.startswith(""):
        #     variavel2.text = "MÉDIA DE 1990 A 2019"
        else:
            variavel2.text = "MÉDIA DOS MESES DO ANO"

        # Salvar em 10.7 e 10.4
        mxd.save()
        nome_salvar = fc_new.split("_")[0] + "_1M"
        mxd.saveACopy(os.path.join(path_local, "SAIDA", "01_MXD", nome_salvar + ".mxd"), "10.4")
        mxd.saveACopy(os.path.join(path_local, "SAIDA", "03_MXD_10.7", nome_salvar + ".mxd"))
        # arcpy.mapping.ExportToPDF(mxd, os.path.join(path_local, "SAIDA", "02_PDF", nome_salvar), resolution=500)
        print "Salvou"

        del mxd
        print "Carta " + nome_salvar + " finalizada em " + time.strftime("%H-%M_%d-%m")
        print >> log, "Carta " + nome_salvar + " finalizada em " + time.strftime("%H-%M_%d-%m")
        arcpy.Delete_management(os.path.join(path_local, feature_dataset + str(count) + ".mxd"))
log.close()
