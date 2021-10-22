import arcpy
import os
import xlrd
import random
import string
import xml.etree.ElementTree as ET
from arcpy import metadata as md


####################################################################
#                   FILE IDENTIFIER

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


####################################################################

local = r""

workbook = xlrd.open_workbook(os.path.join(local, ""))
worksheet = workbook.sheet_by_name('unico')

xslt_style = r""
xslt_temp = r""

xml_base = os.path.join(local, "", "")

gdb = os.path.join(local, "")

arcpy.env.workspace = gdb
list_fd = arcpy.ListDatasets()
for fd in list_fd:
    if fd == "Cadastro_Usuarios":
        print("Dataset: ", fd)
        arcpy.env.workspace = os.path.join(gdb, fd)
        list_fc = arcpy.ListFeatureClasses()
        for fc in list_fc:

            for rows in range(1, worksheet.nrows):
                nome_fc = worksheet.cell(rows, 2).value
                if nome_fc == fc:
                    print(fc, "=", nome_fc)

                    fc_0_metadata = md.Metadata(fc)
                    fc_0_metadata.saveAsUsingCustomXSLT(os.path.join(xslt_temp, fc + ".xml"), xslt_style)
                    fc_0_temp = md.Metadata(os.path.join(xslt_temp, fc + ".xml"))
                    fc_0_metadata.copy(fc_0_temp)
                    fc_0_metadata.save()

                    # Cria identificador
                    ID_md = id_generator(8) + "-" + id_generator(4) + "-" + id_generator(4) + "-" + id_generator(4) + "-" + id_generator(12)

                    # Acessa dados das tabelas para inserir no metadado
                    descricao_md = worksheet.cell(rows, 3).value
                    creditos_md = worksheet.cell(rows, 4).value
                    ano = str(worksheet.cell(rows, 5).value)
                    if ano == "":
                        ano_md = ""
                    else:
                        ano_md = ano[:-2] + "-01-01T00:00:00"

                    escala = str(worksheet.cell(rows, 6).value)
                    if escala == "":
                        escala_md = ""
                    else:
                        escala_md = escala[:-2]

                    titulo_md = worksheet.cell(rows, 11).value
                    tag = worksheet.cell(rows, 12).value
                    if tag == "":
                        tags_md = ""
                    else:
                        tags_md = "" + tag

                    # Parser XML. Insere ID e themeKeywords no XML base.
                    tree_1 = ET.parse(xml_base)
                    root = tree_1.getroot()
                    root.find("mdFileID").text = ID_md
                    root.findall("./dataIdInfo/dataScale/equScale/rfDenom")[0].text = escala_md
                    root.findall("./dataIdInfo/idCitation/date/createDate")[0].text = ano_md
                    tree_1.write(xml_base)

                    # Importa XML base e atualiza informações do metadado de acordo com as feições da camada alvo
                    fc_metadata = md.Metadata(fc)
                    fc_metadata.importMetadata(xml_base)
                    fc_metadata.save()
                    fc_metadata.synchronize('OVERWRITE')

                    # Altera titulo, tags, sumario, descrição e créditos.
                    fc_metadata.title = titulo_md
                    fc_metadata.tags = tags_md
                    fc_metadata.summary = descricao_md
                    fc_metadata.description = descricao_md
                    fc_metadata.credits = creditos_md
                    fc_metadata.save()
                    break
