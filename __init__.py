# -*- coding: utf-8 -*-
"""
/***************************************************************************
                                 Ferramentas PGHP
                                 Um plugin QGIS
            Ferramentas para o Plano de Gestão de Habitats e Paisagem
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
"""

def classFactory(iface):
    # load GestorHabitat class from file GestorHabitat.py
    from pghptools import PghpTools
    return PghpTools(iface)
