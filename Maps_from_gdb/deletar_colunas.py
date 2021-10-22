import arcpy
import os

gdb_path_250 = r""

# i = 0
# arcpy.env.workspace = gdb_path_250
# featuredatasets = arcpy.ListDatasets()
# for dataset in featuredatasets:
#     arcpy.env.workspace = os.path.join(gdb_path_250, dataset)
#     featureclasses = arcpy.ListFeatureClasses()
#     print(i, "datasets prontos de 60")
#     i = i + 1
#     for fc in featureclasses:
#         print fc
#         if len(arcpy.ListFields(fc, "Shape_Leng")) > 0:
#             arcpy.DeleteField_management(fc, "Shape_Leng")

arcpy.env.workspace = gdb_path_250
featuredatasets = arcpy.ListDatasets()
for dataset in featuredatasets:
    if dataset != "Bases":
        print "Dataset: " + dataset
        arcpy.env.workspace = os.path.join(gdb_path_250, dataset)
        featureclasses = arcpy.ListFeatureClasses()
        for fc in featureclasses:
            if fc.startswith("F"):
                pass
            else:
                if fc.split("_")[-3] != "Toponimia":
                    if fc.startswith("Unidades_Conservacao"):
                        print fc
                        arcpy.Delete_management(fc)
                    elif fc.startswith("Area_Indigena"):
                        print fc
                        arcpy.Delete_management(fc)



# if len(dataset.split("_")) == 2:
#     p1 = fc.split("_")[-1]
#     p2 = fc.split("_")[-2]
#     nome = "Grade_Toponimia_" + p2 + "_" + p1
#     print nome
#     arcpy.Rename_management(fc, nome)
# elif len(dataset.split("_")) == 3:
#     p1 = fc.split("_")[-1]
#     p2 = fc.split("_")[-2]
#     p3 = fc.split("_")[-3]
#     nome = "Grade_Toponimia_" + p3 + "_" + p2 + "_" + p1
#     print nome
#     arcpy.Rename_management(fc, nome)





