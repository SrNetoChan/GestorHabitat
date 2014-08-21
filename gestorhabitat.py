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
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
# from gestorhabitatdialog import GestorHabitatDialog

# Import my plugin tools
from gestorhabitattools import *

class GestorHabitat:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface

        # initialize plugin directory
        self.plugin_dir = QFileInfo(QgsApplication.qgisUserDbFilePath()).path() + "/python/plugins/GestorHabitat"

        # defining global variables
        self.mc = self.iface.mapCanvas()

    def initGui(self):
        # Add Toolbar
        self.toolbar = self.iface.addToolBar("Gestor de Habitat")
        self.toolbar.setObjectName("GestorHabitat")
        
        # Add actions to Toolbar
        self.btadicionaracao = QAction(QIcon(":/plugins/GestorHabitat/icons/adicionaracoes.png"),
                                       u"Adicionar ações", self.iface.mainWindow())
        self.toolbar.addActions([self.btadicionaracao])
        
        self.btadicionaracao.setCheckable(True)
        self.btadicionaracao.setEnabled(True)
        
        # self.tooBar.addSeparator() #<-- para colocar um separador na toolbar
        
        # Connect to signals for button behavior
        QObject.connect(self.btadicionaracao, SIGNAL("triggered()"), self.adicionaracao)

        ### connect the action to the run method
        ###QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        # Add toolbar button and menu item
        self.iface.addPluginToMenu(u"&Gestor de Habitat", self.btadicionaracao)
        
    def unload(self):
        # Remove the plugin menu item and icon
        self.toolbar.removeAction(self.btadicionaracao)
        del self.toolbar

    # Method that creates new accoes (RUN)
    def adicionaracao(self):
        # Define "acções" and "unidades de gestão" Layers from project
        l_acao = QgsMapLayerRegistry.instance().mapLayer(u'acoes20140213101202661')
        l_uni_ges= self.mc.currentLayer()
        #l_uni_ges = QgsMapLayerRegistry.instance().mapLayer(u'unidadesdegestao20130312143304288')
        
        # Get layer default values from provider
        # (this avoids problems with unique keys)
        provider = l_acao.dataProvider()
        temp_feature = QgsFeature()
        attributes = []

        for j in l_acao.pendingAllAttributesList():
            if provider.defaultValue(j):
                attributes.append(provider.defaultValue(j))
            else:
                attributes.append(None)

        temp_feature.setAttributes(attributes)

        # open feature form and waits for edits
        if self.iface.openFeatureForm(l_acao, temp_feature, True):
            
            # start edit command to allow undo\redo
            l_acao.beginEditCommand("Add new actions")
            
            new_attributes = temp_feature.attributes()
            
            # replicate "acção" record for each
            # of the selected "Unidades de gestão"
            uniges_ids = [feature.attributes()[1] for feature in l_uni_ges.selectedFeatures()]
            print uniges_ids

            for uniges_id in uniges_ids:
                new_attributes[3] = uniges_id
                temp_feature.setAttributes(new_attributes)
                new_feature = QgsFeature(temp_feature)
                l_acao.addFeature( new_feature )

            l_acao.endEditCommand()
        else:
            pass
            # print "Cancelled"
            # l_acao.destroyEditCommand()
