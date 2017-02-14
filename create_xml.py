#!/usr/bin/env python
# -*- coding:utf8 -*-
#created by Zack2017-02-13 23:28:42

import os
import sys
from xml.dom.minidom import Document 

def create_xml(w_value, h_value , d, xml_name):
    doc = Document()
    annotation = doc.createElement("annotation")
    doc.appendChild(annotation)

    size = doc.createElement("size")
    width = doc.createElement("width")
    width.appendChild(doc.createTextNode(str(w_value)))
    size.appendChild(width)
    height = doc.createElement("height")
    height.appendChild(doc.createTextNode(str(h_value)))
    size.appendChild(height)
    annotation.appendChild(size)
    for category in d.keys():
        coords = d[category]
        for coord in coords:
            object_ = doc.createElement("object")
            name =  doc.createElement("name")
            name.appendChild(doc.createTextNode(category))
            object_.appendChild(name)
            difficult = doc.createElement("difficult")
            difficult.appendChild(doc.createTextNode(str(0)))
            object_.appendChild(difficult)
            bndbox = doc.createElement("bndbox")
            xmin = doc.createElement("xmin")
            xmin.appendChild(doc.createTextNode(str(int(round(coord[0]*w_value, 2)))))
            bndbox.appendChild(xmin)
            ymin = doc.createElement("ymin")
            ymin.appendChild(doc.createTextNode(str(int(round(coord[1]*h_value, 2)))))
            bndbox.appendChild(ymin)
            xmax = doc.createElement("xmax")
            xmax.appendChild(doc.createTextNode(str(int(round(coord[2]*w_value, 2)))))
            bndbox.appendChild(xmax)
            ymax = doc.createElement("ymax")
            ymax.appendChild(doc.createTextNode(str(int(round(coord[3]*h_value, 2)))))
            bndbox.appendChild(ymax)
            object_.appendChild(bndbox)
            annotation.appendChild(object_)
    save_xml = os.path.join(sys.argv[1], xml_name)
    f = open(save_xml, 'w')
    f.write(doc.toprettyxml(indent = '  ', encoding="utf-8"))
    f.close()


d = {"car":[(20,30,40,50)], "people":[(27,39,40,90), (1,10,30,50)]}
width = 1920
height = 1280
xml_name = "test.xml"
create_xml(width, height, d, xml_name)

#json_files = os.listdir(sys.argv[1]) 
#image_path = sys.argv[2]
#all_category = set()
#for json_file in json_files:
#    print json_file
#    f = open(os.path.join(sys.argv[2], json_file))
#    json_dist = json.load(f)
#    f.close()
#    d = dict()
#    for key in json_dict.keys():
#        if not d.has_keys():
#            d[key] = set()
#        xmin, ymin, xmax, ymax = json_dict[key].split(",")
#        coord = (xmin, ymin, xmax, ymax)
#        d[key].add(coord)
#    xml_name = json_file[:-4] + "xml"
#    image_name = json_file[:-4] + ".jpg"
#    image_name = os.path.join(image_path, image_name)
#    if os.path.exists(image_name):
#        img = cv2.imread(image_name)
#        width = img.shape[1]
#        height = img.shape[0]
#    create_xml(height, width, d, xml_name)

             

    
		
