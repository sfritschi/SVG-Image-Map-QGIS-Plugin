# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SVGImageMap
                                 A QGIS plugin
 Based on HTML Image Map Plugin
                             -------------------
        begin                : 2017-05-01
        copyright            : (C) 2017 by sfritschi
        email                : severin.fritschi@hsr.ch
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

from svg_image_map import SVGImageMap

def name():
    return "SVG Image Map Plugin"

def description():
    return "This plugin generates a svg-image map file+img from the active point or polygon layer"

def qgisMinimumVersion():
    return "2.0"

def version():
    return "2.0.1"

def author():
    return "Richard Duivenvoorde"

def email():
    return "richard@duif.net"

def category():
  return "Web"

def classFactory(iface):
    return SVGImageMap(iface)
