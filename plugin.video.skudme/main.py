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

versao = '1.0'
addon_id = 'plugin.video.skudme'
selfAddon = xbmcaddon.Addon(id=addon_id)
addonfolder = selfAddon.getAddonInfo('path')
artfolder = addonfolder + '/resources/img/'
fanart = addonfolder + '/fanart.jpg'
oneURL = 'https://onepiece.zlx.com.br'
oneEP = 'http://st01hd.animesproject.com.br:81/O/one-piece/MQ/episodios/'
narEP = 'http://st01hd.animesproject.com.br:81/N/naruto-shippuuden/MQ/episodios/'
fairEP = 'http://st01hd.animesproject.com.br:81/F/fairy-tail-2014/MQ/episodios/'
geralURL = 'http://st01hd.animesproject.com.br:81/'


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
	print"Sagas One Piece"
	lista_sagas_onepiece()

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

def listar_naruto():
	addDir('Naruto','',21,'http://animes.zlx.com.br/imgs/series/small/4cb6174c3ef8bfb.jpg',{'title': 'Naruto'})
	addDir('Naruto: Shippuuden','',22,'http://animes.zlx.com.br/imgs/series/small/b39ad17d80d0083.jpg',{'title': 'Naruto: Shippuuden'})

def listar_narutoNormal():
	addDir('Do 000 ate 220','',0,'http://animes.zlx.com.br/imgs/series/small/4cb6174c3ef8bfb.jpg',{'title': 'Do 000 ate 220'})
	addDir('Ir para o Episodio','',210,artfolder +"goto.png",{'title': 'Ir para o Episodio'})	

def listar_narutoShippuuden():
	match = re.compile('<a alt=".+?" href=".+?"><u>Episódio (.+?)</u></a>').findall(obterURL('http://animes.zlx.com.br/serie/144/0/Naruto-Shippuuden')) 
	print match
	
	addDir('Naruto: Shippuuden','',0,'http://animes.zlx.com.br/imgs/series/small/b39ad17d80d0083.jpg',{'title': 'Naruto: Shippuuden'})
	addLink('Ultimo Episodio - ' +match[0],narEP +match[0] +'.mp4',narEP +match[0] +'.jpg')
	
	addDir('Do 000 ate ' +match[0],'',0,'http://animes.zlx.com.br/imgs/series/small/b39ad17d80d0083.jpg',{'title': 'Do 000 ate ' +match[0]})
	addDir('Ir para o Episodio','',220,artfolder +"goto.png",{'title': 'Ir para o Episodio'})
	
def listar_fairyTail():
	addDir('Fairy Tail','',31,'http://animes.zlx.com.br/imgs/series/small/205a078e9a010af.jpg',{'title': 'Fairy Tail'})
	addDir('Fairy Tail 2014','',32,'http://animes.zlx.com.br/imgs/series/small/7c15d47e3be614a.jpg',{'title': 'Fairy Tail 2014'})

def listar_fairyTailNormal():
	addDir('Do 000 ate 259','',0,'http://animes.zlx.com.br/imgs/series/small/205a078e9a010af.jpg',{'title': 'Do 000 ate 259'})
	addDir('Ir para o Episodio','',310,artfolder +"goto.png",{'title': 'Ir para o Episodio'})	

def listar_fairyTail2014():
	match = re.compile('<a alt=".+?" href=".+?"><u>Episódio (.+?)</u></a>').findall(obterURL('http://animes.zlx.com.br/serie/1091/0/Fairy-Tail-2014')) 
	print match
	
	addDir('Fairy Tail 2014','',0,'http://animes.zlx.com.br/imgs/series/small/7c15d47e3be614a.jpg',{'title': 'Fairy Tail'})
	addLink('Ultimo Episodio - ' +match[0],fairEP +match[0] +'.mp4',fairEP +match[0] +'.jpg')
	
	addDir('Do 00 ate ' +match[0],'',0,'http://animes.zlx.com.br/imgs/series/small/7c15d47e3be614a.jpg',{'title': 'Do 000 ate ' +match[0]})
	addDir('Ir para o Episodio','',320,artfolder +"goto.png",{'title': 'Ir para o Episodio'})
	
def goto_geral(letra,serie):
	keyb = xbmc.Keyboard('', 'Ir para o Episodio')
	keyb.doModal()
	if (keyb.isConfirmed()):
		search = keyb.getText()
		parametro_pesquisa=urllib.quote(search)
		print serie +" " +parametro_pesquisa
		if serie=='fairy-tail-2014' and int(parametro_pesquisa)<=81:
			epN = parametro_pesquisa +'-p-'
		url = geralURL +letra +'/' +serie +'/MQ/episodios/' + str(epN)
		addLink('Episodio - ' +str(parametro_pesquisa),url +'.mp4',url +'.jpg')

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
	MenuPrincipal()   
elif mode==1:
	onepiece()
elif mode==2:
	listar_naruto()
elif mode==3:
	listar_fairyTail()
elif mode==21:
	listar_narutoNormal()
elif mode==22:
	listar_narutoShippuuden()
elif mode==31:
	listar_fairyTailNormal()
elif mode==32:
	listar_fairyTail2014()
elif mode==10:
	listar_episodios_onepiece(url)
elif mode==100:
	goto_geral('O','one-piece')
elif mode==210:
	goto_geral('N','naruto')
elif mode==220:
	goto_geral('N','naruto-shippuuden')
elif mode==310:
	goto_geral('F','fairy-tail')
elif mode==320:
	goto_geral('F','fairy-tail-2014')

xbmcplugin.endOfDirectory(__handle__)