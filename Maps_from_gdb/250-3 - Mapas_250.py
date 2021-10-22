# -*- coding: utf-8 -*-

import arcpy
import os
import time


########################################################

#         AUTOMATIZACAO PARA CARTAS 250.000

########################################################

#          Adicionar camada - Funcao


def addcamada(camada_gdb, lyr_simbol):
    updatelyr = arcpy.mapping.Layer(camada_gdb)
    sourcelyr = arcpy.mapping.ListLayers(mxd, lyr_simbol, df)[0]
    arcpy.mapping.UpdateLayer(df, updatelyr, sourcelyr, True)
    arcpy.mapping.AddLayer(df, updatelyr, "BOTTOM")


########################################################

#           Dicionario meses do ano


temporal = {
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
    "Tri01": "- PRIMEIRO TRIMESTRE",
    "Tri02": "- SEGUNDO TRIMESTRE",
    "Tri03": "- TERCEIRO TRIMESTRE",
    "Tri04": "- QUARTO TRIMESTRE",
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
    "2018a2019": "- 2018 A 2019"

}

#######################################################

#          Dicionário variaveis


variaveis = {
    "Prec": "PRECIPITAÇÃO",
    "OVrn": "OCORRÊNCIA DE VERANICOS",
    "PChv": "DURAÇÃO DO PERÍODO CHUVOSO",
    "DChv": "DIAS CHUVOSOS",
    "ISec": "ÍNDICE DE SECA",
    "EtoR": "EVAPOTRANSPIRAÇÃO DE REFERÊNCIA"
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

# per_tempo = ""
sigla_var = "PREC_MENSAL_V2"
linha_Lyr = "lyr_linha"
poligono_Lyr = "lyr_poligono_mensal"

path_local = os.path.join(r"")
path_to_gdb = r""
log = open(os.path.join(path_local, "SAIDA", "04_LOG", time.strftime("%H-%M_%d-%m") + ".txt"), "w")

#######################################################

#           Modificar conforme demanda

# MATRIX = [Nome carta, path dataset, path dataset duplicadas, path MXD base, duplicada]

matrix_workspaces = [

    #["F172_Maraba", os.path.join(path_to_gdb, "F172_Maraba_GCS"), None, os.path.join(path_local, "LAYOUT_250_172_" + sigla_var + ".mxd"), False],
    #["F173_Imperatriz", os.path.join(path_to_gdb, "F173_Imperatriz_GCS"), None, os.path.join(path_local, "LAYOUT_250_173_" + sigla_var + ".mxd"), False],
    #["F199_Xambioa", os.path.join(path_to_gdb, "F199_Xambioa_GCS"), None, os.path.join(path_local, "LAYOUT_250_199_" + sigla_var + ".mxd"), False],
    #["F200_Tocantinopolis", os.path.join(path_to_gdb, "F200_Tocantinopolis_GCS"), None, os.path.join(path_local, "LAYOUT_250_200_" + sigla_var + ".mxd"), False],
    #["F226_Araguaiana", os.path.join(path_to_gdb, "F226_Araguaiana_GCS"), None, os.path.join(path_local, "LAYOUT_250_226_" + sigla_var + ".mxd"), False],
    #["F227_Carolina", os.path.join(path_to_gdb, "F227_Carolina_GCS"), os.path.join(path_to_gdb, "F228_Balsas_GCS"), os.path.join(path_local, "LAYOUT_250_227_228_" + sigla_var + ".mxd"), True],
    #["F253_Conceicao_do_Araguaia", os.path.join(path_to_gdb, "F253_Conceicao_do_Araguaia_GCS"), os.path.join(path_to_gdb, "F252_Redencao_GCS"), os.path.join(path_local, "LAYOUT_250_252_253_" + sigla_var + ".mxd"), True],
    #["F254_Itacaja", os.path.join(path_to_gdb, "F254_Itacaja_GCS"), os.path.join(path_to_gdb, "F255_Passo_Fragoso_GCS"), os.path.join(path_local, "LAYOUT_250_254_255_" + sigla_var + ".mxd"), True],
    #["F278_Santana_do_Araguaia", os.path.join(path_to_gdb, "F278_Santana_do_Araguaia_GCS"), None, os.path.join(path_local, "LAYOUT_250_278_" + sigla_var + ".mxd"), False],
    #["F279_Miracema_do_Tocantins", os.path.join(path_to_gdb, "F279_Miracema_do_Tocantins_GCS"), None, os.path.join(path_local, "LAYOUT_250_279_" + sigla_var + ".mxd"), False],
    #["F280_Lizarda", os.path.join(path_to_gdb, "F280_Lizarda_GCS"), os.path.join(path_to_gdb, "F281_Gilbues_GCS"), os.path.join(path_local, "LAYOUT_250_280_281_" + sigla_var + ".mxd"), True],
    #["F303_Santa_Terezinha", os.path.join(path_to_gdb, "F303_Santa_Terezinha_GCS"), None, os.path.join(path_local, "LAYOUT_250_303_" + sigla_var + ".mxd"), False],
    #["F304_Porto_Nacional", os.path.join(path_to_gdb, "F304_Porto_Nacional_GCS"), None, os.path.join(path_local, "LAYOUT_250_304_" + sigla_var + ".mxd"), False],
    #["F305_Ponte_Alta_do_Norte", os.path.join(path_to_gdb, "F305_Ponte_Alta_do_Norte_GCS"), None, os.path.join(path_local, "LAYOUT_250_305_" + sigla_var + ".mxd"), False],
    #["F306_Corrente", os.path.join(path_to_gdb, "F306_Corrente_GCS"), None, os.path.join(path_local, "LAYOUT_250_306_" + sigla_var + ".mxd"), False],
    #["F323_Sao_Felix_do_Araguaia", os.path.join(path_to_gdb, "F323_Sao_Felix_do_Araguaia_GCS"), None, os.path.join(path_local, "LAYOUT_250_323_" + sigla_var + ".mxd"), False],
    #["F324_Gurupi", os.path.join(path_to_gdb, "F324_Gurupi_GCS"), None, os.path.join(path_local, "LAYOUT_250_324_" + sigla_var + ".mxd"), False],
    #["F325_Dianopolis", os.path.join(path_to_gdb, "F325_Dianopolis_GCS"), None, os.path.join(path_local, "LAYOUT_250_325_" + sigla_var + ".mxd"), False],
    #["F326_Formosa_do_Rio_Preto", os.path.join(path_to_gdb, "F326_Formosa_do_Rio_Preto_GCS"), None, os.path.join(path_local, "LAYOUT_250_326_" + sigla_var + ".mxd"), False],
    #["F343_Araguacu", os.path.join(path_to_gdb, "F343_Araguacu_GCS"), os.path.join(path_to_gdb, "F360_Sao_Miguel_do_Araguaia_GCS"), os.path.join(path_local, "LAYOUT_250_343_360_" + sigla_var + ".mxd"), True],
    #["F344_Alvorada", os.path.join(path_to_gdb, "F344_Alvorada_GCS"), None, os.path.join(path_local, "LAYOUT_250_344_" + sigla_var + ".mxd"), False],
    #["F345_Arraias", os.path.join(path_to_gdb, "F345_Arraias_GCS"), None, os.path.join(path_local, "LAYOUT_250_345_" + sigla_var + ".mxd"), False],
    #["F346_Barreiras", os.path.join(path_to_gdb, "F346_Barreiras_GCS"), None, os.path.join(path_local, "LAYOUT_250_346_" + sigla_var + ".mxd"), False],
    #["F361_Porangatu", os.path.join(path_to_gdb, "F361_Porangatu_GCS"), None, os.path.join(path_local, "LAYOUT_250_361_" + sigla_var + ".mxd"), False],
    ["F362_Campos_Belos", os.path.join(path_to_gdb, "F362_Campos_Belos_GCS"), None, os.path.join(path_local, "LAYOUT_250_362_" + sigla_var + ".mxd"), False]

]

######################################################

for rows in matrix_workspaces:
    path_to_save = rows[0]
    print "CENA: " + path_to_save.upper()
    print >>log, "CENA: " + path_to_save.upper()
    sigla_carta = rows[0].split("_")[0]
    arcpy.env.workspace = rows[1]
    featureclasses = arcpy.ListFeatureClasses()
    for fc in featureclasses:
        if fc.startswith("PrecM"):
            mxd = arcpy.mapping.MapDocument(rows[3])
            cena_carta = rows[0][5:].upper()
            mxd.saveACopy(os.path.join(path_local, sigla_carta + ".mxd"))
            mxd = arcpy.mapping.MapDocument(os.path.join(path_local, sigla_carta + ".mxd"))
            mxd.relativePaths = True
            df = arcpy.mapping.ListDataFrames(mxd)[0]
            if fc.endswith("a"):
                continue
            else:
                # numero_layers = arcpy.mapping.ListLayers(mxd)
                # print len(numero_layers)
                # print >> log, len(numero_layers)
                arcpy.env.workspace = rows[1]
                fc_new = fc[:-12]
                matching = [s for s in featureclasses if fc_new in s]
                if matching[0].endswith("l"):
                    linha1 = matching[0]
                    poligono1 = matching[1]
                else:
                    poligono1 = matching[0]
                    linha1 = matching[1]

                    # Set Data Source
                    updateLayer_lin = arcpy.mapping.ListLayers(mxd, linha_Lyr, df)[0]
                    updateLayer_lin.replaceDataSource(path_to_gdb, "FILEGDB_WORKSPACE", linha1)
                    updateLayer_lin.name = linha1
                    updateLayer_pol = arcpy.mapping.ListLayers(mxd, poligono_Lyr, df)[0]
                    updateLayer_pol.replaceDataSource(path_to_gdb, "FILEGDB_WORKSPACE", poligono1)
                    updateLayer_pol.name = poligono1

                if rows[4] is True:
                    arcpy.env.workspace = rows[2]
                    featureclasses2 = arcpy.ListFeatureClasses()
                    matching2 = [s for s in featureclasses2 if fc_new in s]
                    if matching2[0].endswith("l"):
                        linha2 = matching2[0]
                        poligono2 = matching2[1]
                    else:
                        poligono2 = matching2[0]
                        linha2 = matching2[1]
                    updateLayer_lin = arcpy.mapping.ListLayers(mxd, linha_Lyr, df)[0]
                    updateLayer_lin.replaceDataSource(path_to_gdb, "FILEGDB_WORKSPACE", linha2)
                    updateLayer_lin.name = linha2
                    updateLayer_pol = arcpy.mapping.ListLayers(mxd, poligono_Lyr, df)[0]
                    updateLayer_pol.replaceDataSource(path_to_gdb, "FILEGDB_WORKSPACE", poligono2)
                    updateLayer_pol.name = poligono2

                # numero_layers_depois = arcpy.mapping.ListLayers(mxd)
                # print len(numero_layers_depois)
                # print >> log, len(numero_layers_depois)

            # # Remover Lyr com Simbologia
            # remover_linha_lyr = arcpy.mapping.ListLayers(mxd, linha_Lyr, df)[0]
            # arcpy.mapping.RemoveLayer(df, remover_linha_lyr)
            # remover_poligono_lyr = arcpy.mapping.ListLayers(mxd, poligono_Lyr, df)[0]
            # arcpy.mapping.RemoveLayer(df, remover_poligono_lyr)

            # Titulo Variavel
            variavel_temporal = matching[0].split("_")[0][4:]
            variavel_nome = matching[0].split("_")[0][0:4]
            if variavel_temporal.startswith("TAnual"):
                variavel2 = "MÉDIA DE 1990 A 2019"
            elif variavel_temporal.startswith("M"):
                variavel2 = "1990 A 2019"
            else:
                variavel2 = "SOMA DOS MESES DO ANO"
            variavel = arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT", "titulo")[0]
            variavel.text = "<BOL>{0}".format(variaveis[variavel_nome]) + " {0} - ".format(temporal[variavel_temporal]) + variavel2 + "</BOL>"

            # Salvar em 10.7 e 10.4
            mxd.save()
            camada_nome1 = matching[0].split("_")[0]
            camada_nome2 = matching[0].split("_")[1]
            caminho2 = sigla_carta + "_" + camada_nome1 + "_" + camada_nome2
            mxd.saveACopy(os.path.join(path_local, "SAIDA", "01_MXD", caminho2 + ".mxd"), "10.4")
            mxd.saveACopy(os.path.join(path_local, "SAIDA", "03_MXD_10.7", caminho2 + ".mxd"))

            # PDF, Log, Deleta MXD atual
            nome_pdf = os.path.join(path_local, "SAIDA", "02_PDF", caminho2)
            #exportar = ["F227_Carolina", "F278_Santana_do_Araguaia", "F323_Sao_Felix_do_Araguaia"]
            #if rows[0] in exportar:
            arcpy.mapping.ExportToPDF(mxd, nome_pdf, resolution=500)
            #    print "Exportou PDF"
            del mxd
            print "Carta " + caminho2 + " finalizada em " + time.strftime("%H-%M_%d-%m")
            print >> log, "Carta " + caminho2 + " finalizada em " + time.strftime("%H-%M_%d-%m")

            arcpy.Delete_management(os.path.join(path_local, sigla_carta + ".mxd"))

log.close()
