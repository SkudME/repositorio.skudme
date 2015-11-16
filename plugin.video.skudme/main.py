# -*- coding: utf-8 -*-
# Module: Video
# Author: Skud.ME
# Created on: 5.11.2015
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html

import sys
from urlparse import parse_qsl
import xbmcgui
import xbmcplugin
import urllib, urllib2
import xbmcaddon
import xbmc
import re

# Get the plugin handle as an integer number.
__handle__ = int(sys.argv[1])

versao = '0.7'
addon_id = 'plugin.video.skudme'
selfAddon = xbmcaddon.Addon(id=addon_id)
addonfolder = selfAddon.getAddonInfo('path')
artfolder = addonfolder + '/resources/img/'
fanart = addonfolder + '/fanart.jpg'
oneURL = 'https://onepiece.zlx.com.br'
oneEP = 'http://st01hd.animesproject.com.br/vod/O/one-piece/MQ/episodios/'

def addDir(name,url,mode,iconimage,infolabels):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setProperty('fanart_image', fanart)
	liz.setInfo( type="video", infoLabels=infolabels)
	ok=xbmcplugin.addDirectoryItem(__handle__,url=u,listitem=liz,isFolder=True)
	return ok
	
def addLink(name,url,iconimage):
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
	liz.setProperty('fanart_image', fanart)
	liz.setInfo( type="Video", infoLabels={ "Title": name } )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
	return ok


def MenuPrincipal():
	addDir('One Piece','https://onepiece.zlx.com.br/midia/episodios/sagas',1,'http://www.aliancaproject.com.br/imgs_index/bg_pp.jpg',{'title': 'One Piece'}) #https://onepiece.zlx.com.br/ piecePROJECT
	addDir('Naruto','',2,'http://www.aliancaproject.com.br/imgs_index/bg_np.jpg',{'title': 'Naruto'})
	addDir('Fairy Tail','',3,'http://www.aliancaproject.com.br/imgs_index/bg_fyp.jpg',{'title': 'Fairy Tail'})
	
#http://onepiecex.com.br/ onepiecex ou https://onepiece.zlx.com.br/ piecePROJECT
#http://boruto.com.br/ narutoPROJECT
#http://fairytail.blog.br/ fairyPROJECT
	
def onepiece():
#	addDir('East Blue[1 ao 60]','',1,'https://onepiece.zlx.com.br/images/sagas/east.png',{'title': 'East Blue[1 ao 60]'})
#	addDir('Baroque Works[61 ao 130]','',2,'https://onepiece.zlx.com.br/images/sagas/baroque.png',{'title': 'Baroque Works[61 ao 130]'})
	print"Sagas One Piece"
	lista_sagas_onepiece()

def goto_onepiece():
	keyb = xbmc.Keyboard('', 'Ir para o Episodio')
	keyb.doModal()
	if (keyb.isConfirmed()):
		search = keyb.getText()
		parametro_pesquisa=urllib.quote(search)
		url = oneEP + str(parametro_pesquisa)
		addLink('Episodio - ' +str(parametro_pesquisa),url,artfolder +"goto.png")
	
def lista_sagas_onepiece():
	codigo_fonte = obterURL(url)
	
	match = re.compile('<a href="http://onepieceproject.xpg.uol.com.br/episodios/episodio-(.+?)/" target="_blank"><img src="(.+?)" alt="latest episode" /></a>').findall(obterURL(oneURL)) #https://onepiece.zlx.com.br/ piecePROJECT
	print match
	
	addDir('Ir para o Episodio','',100,artfolder +"goto.png",{'title': 'Ir para o Episodio'})
	
	for ep, img in match:
		addLink('Ultimo Episodio - ' +ep,'' +ep +'.mp4',img)
	
	#<a href="/midia/episodios/sagas/east-blue"><img alt="East Blue" src="/images/sagas/east.png"></a> #https://onepiece.zlx.com.br/ piecePROJECT
	match = re.compile('<a href="(.+?)"><img alt="(.+?)" src="(.+?)" /></a>').findall(codigo_fonte) #https://onepiece.zlx.com.br/ piecePROJECT
	
	for urlAux, titulo, img in match:
		addDir(titulo,str(oneURL+urlAux),10,str(oneURL+img),{'title': titulo}) #https://onepiece.zlx.com.br/ piecePROJECT
	
		
def listar_episodios_onepiece(url):
	codigo_fonte = obterURL(url)
	
	#<div class="new_release_screen"><img src="/images/screens/onepiece001lan.jpg" alt="screen" style="margin-top:-7px;"/></div>
	#<div class="new_release_titulo"><h1>Episódio<b>001</b></h1></div>
	#<a href="/assistir-online/001/shxmq/files/6376353644/PP-E_001_MQ.mp4" target=_blank><img src="/release/online.png" width="212" height="65" border="0" class="download_but" /></a>

	img = '<div class="new_release_screen"><img src="(.+?)" alt="screen" style="margin-top:-7px;"/></div>'
	titulo = '<div class="new_release_titulo"><h1>(.+?)</h1></div>'
	urlAux = '<a href="(.+?)" target=_blank><img src="/release/online.png" width="212" height="65" border="0" class="download_but" /></a>'
	
	TotalItems = 0
	imgs = []
	titulos = []
	urls = []
	
	for match in re.findall(img, codigo_fonte):
		imgs.append(match)
		TotalItems+=1
		
	for match in re.findall(titulo, codigo_fonte):
		titulos.append(match)
		
	for match in re.findall(urlAux, codigo_fonte):
		urls.append(match)
	
	for x in xrange(0, TotalItems):
		addLink(titulos[x].replace('<b>',' ').replace('</b>',''),str('http://st01hd.animesproject.com.br/vod/O/one-piece/MQ/episodios/' +titulos[x].replace('Episódio<b>','').replace('</b>','') +'.mp4'),str(oneURL+imgs[x]))

		
def obterURL(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
	return link
		
def get_params():
	param=[]
	paramstring=sys.argv[2]
	if len(paramstring)>=2:
		params=sys.argv[2]
		cleanedparams=params.replace('?','')
		if (params[len(params)-1]=='/'):
			params=params[0:len(params)-2]
		pairsofparams=cleanedparams.split('&')
		param={}
		for i in range(len(pairsofparams)):
			splitparams={}
			splitparams=pairsofparams[i].split('=')
			if (len(splitparams))==2:
				param[splitparams[0]]=splitparams[1]
							
	return param


params=get_params()
url=None
name=None
mode=None
iconimage=None
plot=None

try: url=urllib.unquote_plus(params["url"])
except: pass
try: name=urllib.unquote_plus(params["name"])
except: pass
try: mode=int(params["mode"])
except:
	try: 
		mode=params["mode"]
	except: pass
try: iconimage=urllib.unquote_plus(params["iconimage"])
except: pass
try: plot=urllib.unquote_plus(params["plot"])
except: pass

print ("Mode: "+str(mode))
print ("URL: "+str(url))
print ("Name: "+str(name))
print ("iconimage: "+str(iconimage))


if mode==None: 
	print "MenuPrincipal"
	MenuPrincipal()
   
elif mode==1:
	print "Menu One Piece"
	onepiece()
elif mode==10:
	listar_episodios_onepiece(url)
elif mode==100:
	goto_onepiece(url)
	
xbmcplugin.endOfDirectory(__handle__)