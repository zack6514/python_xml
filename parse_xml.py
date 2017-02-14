#!/usr/bin/env python
# -*- coding:utf8 -*-
#created by Zack2017-02-14 23:21:53

import xml.etree.ElementTree as ET
import os
import sys

xml_file = os.path.join(sys.argv[1])

tree = ET.parse(xml_file)
root = tree.getroot()

width = []
height = []
names = []
coords =[]

for w in root.iter("width"):
    width.append(w.text)

for h in root.iter("height"):
    height.append(h.text)

for name in root.iter("name"):
    names.append(name.text)

for bndbox in root.iter("bndbox"):
    xmin = bndbox.find("xmin").text
    ymin = bndbox.find("ymin").text
    xmax = bndbox.find("xmax").text
    ymax = bndbox.find("ymax").text
    coord = (xmin, ymin, xmax, ymax)
    coords.append(coord)

print width
print height
print names
print coords
