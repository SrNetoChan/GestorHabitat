# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GestorHabitatDialog
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
"""

from PyQt4 import QtCore, QtGui
from ui_gestorhabitat import Ui_GestorHabitat
# create the dialog for zoom to point


class GestorHabitatDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_GestorHabitat()
        self.ui.setupUi(self)
