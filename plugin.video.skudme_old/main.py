# -*- coding: utf-8 -*-
# Author: Skud.ME
# Created on: 5.11.2015
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html

import sys,urllib,xbmcplugin,xbmcgui

#def addDirectoryItem(name, parameters={},pic="", pasta=True):
    #li = xbmcgui.ListItem(name,iconImage="DefaultFolder.png", thumbnailImage=pic)
    #url = sys.argv[0] + '?' + urllib.urlencode(parameters)
    #return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=li, isFolder=pasta)

def CATEGORIES():
	print "CATEGORIES"
	#Name = "One Piece"
	#Url = "http://onepiecex.com.br/episodios/online/"
	#Mode = 1
	#Imagem = "http://onepiecex.com.br/wp-content/themes/opexv2/imagens/topo/logo.png"
	#Informacao = "http://onepiecex.com.br/"
	#Pasta = True

	#addDirectoryItem(Name, {"name":Name, "url":Url, "mode":Mode}, Imagem,Pasta)

if mode==None or url==None or len(url)<1:
   print "Inicio"
   CATEGORIES()
   
#elif mode==1:
#	print "Mode: 1 - Listar Temporadas"