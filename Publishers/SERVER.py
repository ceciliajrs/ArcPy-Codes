import arcpy

import arcpy, json
from urllib.request import urlopen
from urllib.parse import urlencode
import xml.dom.minidom as DOM


# Function to enable extensions
def enable_extensions(sddraftPath, soe):
    # Read the sddraft xml.
    doc = DOM.parse(sddraftPath)

    # Find all elements named TypeName. This is where the server object extension
    # (SOE) names are defined.
    typeNames = doc.getElementsByTagName('TypeName')
    for typeName in typeNames:
        # Get the TypeName we want to enable.
        if typeName.firstChild.data == soe:
            extension = typeName.parentNode
            for extElement in extension.childNodes:
                # Enable Feature Access.
                if extElement.tagName == 'Enabled':
                    extElement.firstChild.data = 'true'

    # Write to sddraft.
    f = open(sddraftPath, 'w')
    doc.writexml(f)
    f.close()


# Function to configure properties of an extension
# soe = extension for which properties have to be added
def enable_configproperties(sddraftPath, soe, property_set):
    # Read the sddraft xml.
    doc = DOM.parse(sddraftPath)


# list the paths for the input aprx, output sddraft and sd files in variables
aprxPath = r""
serviceName = ""
sddraftPath = r"" % serviceName
sdPath = r"" % serviceName
arcpy.env.overwriteOutput = True

# list the AGO or enterprise url and credentials here
portalURL = r""
fed_server = r""

username = ""
password = ""

# Sign into AGO and set as active portal
arcpy.SignInToPortal(portalURL, username, password)

# Maintain a reference of an ArcGISProject object pointing to your project
aprx = arcpy.mp.ArcGISProject(aprxPath)

# Maintain a reference of a Map object pointing to your desired map
m = aprx.listMaps("Barragens")[0]

# Create MapImageSharingDraft and set service properties
sharing_draft = m.getWebLayerSharingDraft("FEDERATED_SERVER", "MAP_IMAGE", serviceName)  # Creates a MapImageSharingdraft class object
sharing_draft.federatedServerUrl = fed_server
sharing_draft.portalFolder = ""
sharing_draft.serverFolder = ""
sharing_draft.copyDataToServer = False  # Need to register db first if set to False
sharing_draft.summary = "My Summary"
sharing_draft.tags = "My Tags"
sharing_draft.description = "My Description"
sharing_draft.credits = "My Credits"
sharing_draft.useLimitations = "My Use Limitations"
sharing_draft.exportToSDDraft(sddraftPath)  # Need to crack open the sddraft to enable FS
print("Exported SDDraft")

# Enable extensions on map server
enable_extensions(sddraftPath, "FeatureServer")
# enable_extensions(sddraftPath, "WMSServer")
# enable_extensions(sddraftPath, "WFSServer")

arcpy.StageService_server(sddraftPath, sdPath)
print("Created SD")

arcpy.UploadServiceDefinition_server(sdPath, fed_server)
print("Uploaded and Shared SD")
# endregion
print("END")
# end
