# -*- coding: utf-8 -*-

import arcpy
from arcpy import metadata as md
import os
import xlrd
import xml.etree.ElementTree as ET
import string
import random
import time


####################################################################
#                   FILE IDENTIFIER

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


####################################################################

# CAMINHO PARA BANCOS
V03 = r"..."
SDE_final = r"..."

# CAMINHO PLANILHA
workbook = xlrd.open_workbook(r"...")
worksheet = workbook.sheet_by_name('Planilha1')

# CAMINHO .shp.xml BASE
xml_base = r"..."

arcpy.env.workspace = SDE_final

# Trocar o valor inicial do Range conforme a linha que quer começar na planilha
for rows in range(88, worksheet.nrows):
    erro = worksheet.cell(rows, 10).value
    tabela_v03_nome = worksheet.cell(rows, 0).value

    # Seleciona apenas linhas que não estão com erro
    if erro == "carregar":
        arcpy.env.workspace = V03
        for fc_v03 in arcpy.ListFeatureClasses():
            fc_v03_banco = fc_v03.split(".")[1]
            fc_v03_nome = fc_v03.split(".")[-1]

            # Seleciona apenas camadas no V03
            if fc_v03_banco == "v03":

                # Check if nome tabela no v03 é igual ao nome na planilha
                if tabela_v03_nome == fc_v03_nome:
                    print(tabela_v03_nome)
                    dataset = worksheet.cell(rows, 7).value
                    nome_novo = worksheet.cell(rows, 1).value
                    caminho_novo = os.path.join(SDE_final, dataset, nome_novo)

                    # Delete arquivo pré existente
                    if arcpy.Exists(caminho_novo):
                        arcpy.Delete_management(caminho_novo)

                    # Copia do v03 pro banco
                    arcpy.Copy_management(fc_v03, caminho_novo)
                    print(rows, "NOME: ", nome_novo, "DATASET: ", dataset)

                    # Cria identificador
                    ID_md = id_generator(8) + "-" + id_generator(4) + "-" + id_generator(4) + "-" + id_generator(4) + "-" + id_generator(12)

                    # Acessa dados da tabela para inserir no metadado
                    tags_md = worksheet.cell(rows, 2).value + " , " + worksheet.cell(rows, 5).value
                    titulo_md = worksheet.cell(rows, 3).value
                    creditos_md = worksheet.cell(rows, 4).value

                    # Parser XML. Insere ID e themeKeywords no XML base.
                    tree_1 = ET.parse(xml_base)
                    root = tree_1.getroot()
                    root.find("mdFileID").text = ID_md
                    root.findall("./dataIdInfo/themeKeys/keyword")[0].text = tags_md
                    tree_1.write(xml_base)

                    # Importa XML base e atualiza informações do metadado de acordo com as feições da camada alvo
                    fc_metadata = md.Metadata(caminho_novo)
                    fc_metadata.importMetadata(xml_base)
                    fc_metadata.save()
                    fc_metadata.synchronize('OVERWRITE')

                    # Altera titulo, tags, sumario, descrição e créditos.
                    fc_metadata.title = titulo_md
                    fc_metadata.tags = tags_md
                    fc_metadata.summary = titulo_md
                    fc_metadata.description = titulo_md
                    fc_metadata.credits = creditos_md
                    fc_metadata.save()
                    break
    else:
        print("CAMADA NAO CARREGADA: ", tabela_v03_nome)
print(time.strftime("%H-%M_%d-%m"))


# root.findall("./dataIdInfo/searchKeys/keyword")[0].text = tags_md
# root.findall("./dataIdInfo/idAbs")[0].text = "TESTE_PYTHON"
# root.findall("./dataIdInfo/idPurp")[0].text = "TESTE_PYTHON"
