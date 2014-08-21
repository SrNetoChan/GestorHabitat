# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GestorHabitat
                                 A QGIS plugin
 Ferramentas para gestão de habitats
                             -------------------
        begin                : 2013-04-03
        copyright            : (C) 2013 by Alexandre Neto - Cascais Ambiente
        email                : alexandre.neto@cascaisambiente
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

def classFactory(iface):
    # load GestorHabitat class from file GestorHabitat.py
    from gestorhabitat import GestorHabitat
    return GestorHabitat(iface)
