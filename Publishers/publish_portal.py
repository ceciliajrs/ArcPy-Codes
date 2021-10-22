import arcpy
import os
import xlrd

portal = ""
usuario = ""
senha = ""

# Sign in to portal
arcpy.SignInToPortal(portal, usuario, senha)

infos_publicacao = xlrd.open_workbook(r"")
worksheet = infos_publicacao.sheet_by_name('Planilha1')

outdir = r""

for rows in range(1, worksheet.nrows):
    service = worksheet.cell(rows, 2).value
    sddraft_filename = service + ".sddraft"
    sddraft_output_filename = os.path.join(outdir, sddraft_filename)

    # Reference map to publish
    aprx = arcpy.mp.ArcGISProject(worksheet.cell(rows, 1).value)
    m = aprx.listMaps(service)[0]
    arcpy.env.overwriteOutput = True

    # Create FeatureSharingDraft and set service properties
    sharing_draft = m.getWebLayerSharingDraft("HOSTING_SERVER", "FEATURE", service)
    sharing_draft.portalFolder = "P"
    sharing_draft.summary = worksheet.cell(rows, 4).value
    sharing_draft.tags = worksheet.cell(rows, 3).value
    sharing_draft.description = worksheet.cell(rows, 5).value
    sharing_draft.credits = worksheet.cell(rows, 6).value

    print(service)

    # Create Service Definition Draft file
    sharing_draft.exportToSDDraft(sddraft_output_filename)

    # Stage Service
    sd_filename = service + ".sd"
    sd_output_filename = os.path.join(outdir, sd_filename)
    arcpy.StageService_server(sddraft_output_filename, sd_output_filename)

    # Share to portal
    print("Uploading Service Definition...")
    arcpy.UploadServiceDefinition_server(sd_output_filename, "My Hosted Services", in_override = "OVERRIDE_DEFINITION", in_public = "PUBLIC", in_organization = "SHARE_ORGANIZATION")
    print("Successfully Uploaded service.")


