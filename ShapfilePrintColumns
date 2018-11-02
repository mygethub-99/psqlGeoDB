# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 15:49:19 2018
Useful script to see what's inside a shapefile.
@author: ow4253
"""
import osgeo.ogr

shapefile = osgeo.ogr.Open("C:\\Path\shapefile.shp")
layer = shapefile.GetLayer(0)

#Get Field Names
layerDefinition = layer.GetLayerDefn()
print ("Name  -  Type  Width  Precision")
for i in range(layerDefinition.GetFieldCount()):
    fieldName =  layerDefinition.GetFieldDefn(i).GetName()
    fieldTypeCode = layerDefinition.GetFieldDefn(i).GetType()
    fieldType = layerDefinition.GetFieldDefn(i).GetFieldTypeName(fieldTypeCode)
    fieldWidth = layerDefinition.GetFieldDefn(i).GetWidth()
    GetPrecision = layerDefinition.GetFieldDefn(i).GetPrecision()

    print (fieldName + " - " + fieldType+ " " + str(fieldWidth) + " " + str(GetPrecision))
