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
SDE_final = r"..."

# CAMINHO PLANILHA
workbook = xlrd.open_workbook(r"...")
worksheet = workbook.sheet_by_name('Planilha1')

arcpy.env.workspace = SDE_final

for rows in range(1, worksheet.nrows):
    camada = worksheet.cell(rows, 1).value
    dataset = worksheet.cell(rows, 0).value
    caminho_camada = os.path.join(SDE_final,dataset, camada)
    print(camada)
    xml1 = worksheet.cell(rows, 3).value
    xml2 = worksheet.cell(rows, 2).value
    xml_base = os.path.join(xml1, xml2)
    # Cria identificador
    ID_md = id_generator(8) + "-" + id_generator(4) + "-" + id_generator(4) + "-" + id_generator(4) + "-" + id_generator(12)

    # # Acessa dados da tabela para inserir no metadado
    # tags_md = worksheet.cell(rows, 2).value + " , " + worksheet.cell(rows, 5).value
    # titulo_md = worksheet.cell(rows, 3).value
    # creditos_md = worksheet.cell(rows, 4).value

    # # Parser XML. Insere ID e themeKeywords no XML base.
    # tree_1 = ET.parse(xml_base)
    # root = tree_1.getroot()
    # root.find("mdFileID").text = ID_md
    # root.findall("./dataIdInfo/themeKeys/keyword")[0].text = tags_md
    # tree_1.write(xml_base)

    # Importa XML base e atualiza informações do metadado de acordo com as feições da camada alvo
    fc_metadata = md.Metadata(caminho_camada)
    fc_metadata.importMetadata(xml_base)
    fc_metadata.save()
    fc_metadata.synchronize('OVERWRITE')

    # # Altera titulo, tags, sumario, descrição e créditos.
    # fc_metadata.title = titulo_md
    # fc_metadata.tags = tags_md
    # fc_metadata.summary = titulo_md
    # fc_metadata.description = titulo_md
    # fc_metadata.credits = creditos_md
    fc_metadata.save()

