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
import os

# Get the plugin handle as an integer number.
__handle__ = int(sys.argv[1])


versao = '1.8'
addon_id = 'plugin.video.skudme'
selfAddon = xbmcaddon.Addon(id=addon_id)
addonfolder = selfAddon.getAddonInfo('path')
artfolder = addonfolder + '/resources/img/'
fanart = addonfolder + '/fanart.jpg'
oneEP = 'http://st01hd.animesproject.com.br/vod/O/one-piece/MQ/episodios/'
narEP = 'http://st01hd.animesproject.com.br/vod/N/naruto-shippuuden/MQ/episodios/'
fairEP = 'http://st01hd.animesproject.com.br/vod/F/fairy-tail-2014/MQ/episodios/'
opmEP = 'http://st01hd.animesproject.com.br/vod/O/one-punch-man/MQ/episodios/'
kob1EP = 'http://st01hd.animesproject.com.br/vod/K/kuroko-no-basket/MQ/episodios/'
kob2EP = 'http://st01hd.animesproject.com.br/vod/K/kuroko-no-basket-2/MQ/episodios/'
kob3EP = 'http://st01hd.animesproject.com.br/vod/K/kuroko-no-basket-3/MQ/episodios/'
geralURL = 'http://st01hd.animesproject.com.br/vod/'

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
	addDir('One Piece','',1,artfolder +'onepiece.png',{'title': 'One Piece'}) 
	addDir('Naruto','',2,artfolder +'naruto.png',{'title': 'Naruto'})
	addDir('Fairy Tail','',3,artfolder +'fairytail.png',{'title': 'Fairy Tail'})
	addDir('One Punch Man','',4,artfolder +'onepunchman.png',{'title': 'One Punch Man'})
	addDir('Kuroko no Basket','',5,artfolder +'kuroko.png',{'title': 'Kuroko no Basket'})
	
def listar_onepiece():
	match = ultimoEpGeral('one-piece')
	print match
	
	addDir('One Piece','',0,'http://animes.zlx.com.br/imgs/series/small/30ff3cba97dd1d2.jpg',{'title': 'One Piece'})
	addLink('Ultimo Episodio - ' +match,oneEP +match +'.mp4',oneEP +match +'.jpg')
	addDir('Do 000 ate 718','',0,'http://animes.zlx.com.br/imgs/series/small/30ff3cba97dd1d2.jpg',{'title': 'Do 000 ate 718'})
	addDir('Ir para o Episodio','',110,artfolder +"goto.png",{'title': 'Ir para o Episodio'})	
	addDir('Filmes','',13,artfolder +'filmes.png',{'title': 'Filmes'})		

def listar_onepiece_filmes():	
	addDir('Filmes','',13,artfolder +'filmes.png',{'title': 'Filmes'})		
	addLink('One Piece: The Movie','http://st01hd.animesproject.com.br/vod/O/one-piece/MQ/filmes/01.mp4','http://st01hd.animesproject.com.br/vod/O/one-piece/MQ/filmes/01.jpg')
	addLink('Aventura na Ilha Nejimaki','http://st01hd.animesproject.com.br/vod/O/one-piece/MQ/filmes/02.mp4','http://st01hd.animesproject.com.br/vod/O/one-piece/MQ/filmes/02.jpg')
	addLink('O Reino de Chopper na Ilha dos Estranhos Animais ','http://st01hd.animesproject.com.br/vod/O/one-piece/MQ/filmes/03.mp4','http://st01hd.animesproject.com.br/vod/O/one-piece/MQ/filmes/03.jpg')
	addLink('Aventura Mortal!','http://st01hd.animesproject.com.br/vod/O/one-piece/MQ/filmes/04.mp4','http://st01hd.animesproject.com.br/vod/O/one-piece/MQ/filmes/04.jpg')
	addLink('A Maldição da Espada Sagrada','http://st01hd.animesproject.com.br/vod/O/one-piece/MQ/filmes/05.mp4','http://st01hd.animesproject.com.br/vod/O/one-piece/MQ/filmes/05.jpg')
	addLink('Barão Omatsuri e a Ilha Secreta','http://st01hd.animesproject.com.br/vod/O/one-piece/MQ/filmes/06.mp4','http://st01hd.animesproject.com.br/vod/O/one-piece/MQ/filmes/06.jpg')
	addLink('Os Mechas do Castelo Karakuri!','http://st01hd.animesproject.com.br/vod/O/one-piece/MQ/filmes/07.mp4','http://st01hd.animesproject.com.br/vod/O/one-piece/MQ/filmes/07.jpg')
	addLink('Episódio de Alabasta: A Princesa do Deserto e os Piratas','http://st01hd.animesproject.com.br/vod/O/one-piece/MQ/filmes/08.mp4','http://st01hd.animesproject.com.br/vod/O/one-piece/MQ/filmes/08.jpg')
	addLink('Episódio de Chopper Plus: Bloom no inverno, Milagre de Sakura','http://st01hd.animesproject.com.br/vod/O/one-piece/MQ/filmes/09.mp4','http://st01hd.animesproject.com.br/vod/O/one-piece/MQ/filmes/09.jpg')
	addLink('One Piece Film: World Strong','http://st01hd.animesproject.com.br/vod/O/one-piece/MQ/filmes/10.mp4','http://st01hd.animesproject.com.br/vod/O/one-piece/MQ/filmes/10.jpg')
	addLink('One Piece 3D: Perseguição aos Chapéus de Palha','http://st01hd.animesproject.com.br/vod/O/one-piece/MQ/filmes/11.mp4','http://st01hd.animesproject.com.br/vod/O/one-piece/MQ/filmes/11.jpg')
	addLink('One Piece Film: Z','http://st01hd.animesproject.com.br/vod/O/one-piece/MQ/filmes/12.mp4','http://st01hd.animesproject.com.br/vod/O/one-piece/MQ/filmes/12.jpg')
	
def listar_naruto():
	addDir('Naruto','',21,'http://animes.zlx.com.br/imgs/series/small/4cb6174c3ef8bfb.jpg',{'title': 'Naruto'})
	addDir('Naruto: Shippuuden','',22,'http://animes.zlx.com.br/imgs/series/small/b39ad17d80d0083.jpg',{'title': 'Naruto: Shippuuden'})

def listar_narutoNormal():
	addDir('Naruto','',21,'http://animes.zlx.com.br/imgs/series/small/4cb6174c3ef8bfb.jpg',{'title': 'Naruto'})
	addDir('Do 000 ate 220','',0,'http://animes.zlx.com.br/imgs/series/small/4cb6174c3ef8bfb.jpg',{'title': 'Do 000 ate 220'})
	addDir('Ir para o Episodio','',210,artfolder +"goto.png",{'title': 'Ir para o Episodio'})	
	addDir('Filmes','',211,artfolder +"filmes.png",{'title': 'Filmes'})	

def listar_narutoNormal_filmes():
	addDir('Filmes','',211,artfolder +"filmes.png",{'title': 'Filmes'})	
	addLink('2004 - Naruto O Filme: O Confronto Ninja no Pais da Neve','http://st01hd.animesproject.com.br/vod/N/naruto/MQ/filmes/01.mp4','http://st01hd.animesproject.com.br/vod/N/naruto/MQ/filmes/01.jpg')
	addLink('2005 - As Ruínas Fantasmas nos Confins da Terra','http://st01hd.animesproject.com.br/vod/N/naruto/MQ/filmes/02.mp4','http://st01hd.animesproject.com.br/vod/N/naruto/MQ/filmes/02.jpg')
	addLink('2006 - A Revolta dos Animais da Lua Crescente','http://st01hd.animesproject.com.br/vod/N/naruto/MQ/filmes/03.mp4','http://st01hd.animesproject.com.br/vod/N/naruto/MQ/filmes/03.jpg')

def listar_narutoShippuuden():
	match = ultimoEpGeral('naruto-shippuuden')
	print match
	
	addDir('Naruto: Shippuuden','',0,'http://animes.zlx.com.br/imgs/series/small/b39ad17d80d0083.jpg',{'title': 'Naruto: Shippuuden'})
	addLink('Ultimo Episodio - ' +match,narEP +match +'.mp4',narEP +match +'.jpg')
	
	addDir('Do 000 ate ' +match,'',0,'http://animes.zlx.com.br/imgs/series/small/b39ad17d80d0083.jpg',{'title': 'Do 000 ate ' +match})
	addDir('Ir para o Episodio','',220,artfolder +"goto.png",{'title': 'Ir para o Episodio'})
	
	addDir('Filmes','',221,artfolder +"filmes.png",{'title': 'Filmes'})	
	
def listar_narutoShippuuden_filmes():
	addDir('Filmes','',221,artfolder +"filmes.png",{'title': 'Filmes'})	
	addLink('2007 - Naruto Shippuden the Movie','http://st01hd.animesproject.com.br/vod/N/naruto-shippuuden/MQ/filmes/01.mp4','http://st01hd.animesproject.com.br/vod/N/naruto-shippuuden/MQ/filmes/01.jpg')
	addLink('2008 - Naruto Shippuden the Movie: Bonds','http://st01hd.animesproject.com.br/vod/N/naruto-shippuuden/MQ/filmes/02.mp4','http://st01hd.animesproject.com.br/vod/N/naruto-shippuuden/MQ/filmes/02.jpg')
	addLink('2009 - Naruto Shippuden the Movie: The Will of Fire','http://st01hd.animesproject.com.br/vod/N/naruto-shippuuden/MQ/filmes/03.mp4','http://st01hd.animesproject.com.br/vod/N/naruto-shippuuden/MQ/filmes/03.jpg')
	addLink('2010 - Naruto Shippuden the Movie: The Lost Tower','http://st01hd.animesproject.com.br/vod/N/naruto-shippuuden/MQ/filmes/04.mp4','http://st01hd.animesproject.com.br/vod/N/naruto-shippuuden/MQ/filmes/04.jpg')
	addLink('2011 - Naruto the Movie: Blood Prison','http://st01hd.animesproject.com.br/vod/N/naruto-shippuuden/MQ/filmes/05.mp4','http://st01hd.animesproject.com.br/vod/N/naruto-shippuuden/MQ/filmes/05.jpg')
	addLink('2012 - Road to Ninja: Naruto the Movie','http://st01hd.animesproject.com.br/vod/N/naruto-shippuuden/MQ/filmes/06.mp4','http://st01hd.animesproject.com.br/vod/N/naruto-shippuuden/MQ/filmes/06.jpg')
	addLink('2014 - The Last: Naruto the Movie','http://st01hd.animesproject.com.br/vod/N/naruto-shippuuden/MQ/filmes/07.mp4','http://st01hd.animesproject.com.br/vod/N/naruto-shippuuden/MQ/filmes/07.jpg')

def listar_fairyTail():
	addDir('Fairy Tail','',31,'http://animes.zlx.com.br/imgs/series/small/205a078e9a010af.jpg',{'title': 'Fairy Tail'})
	addDir('Fairy Tail 2014','',32,'http://animes.zlx.com.br/imgs/series/small/7c15d47e3be614a.jpg',{'title': 'Fairy Tail 2014'})
	
def listar_fairyTailNormal():
	addDir('Fairy Tail','',31,'http://animes.zlx.com.br/imgs/series/small/205a078e9a010af.jpg',{'title': 'Fairy Tail'})
	addDir('Do 000 ate 259','',0,'http://animes.zlx.com.br/imgs/series/small/205a078e9a010af.jpg',{'title': 'Do 000 ate 259'})
	addDir('Ir para o Episodio','',310,artfolder +"goto.png",{'title': 'Ir para o Episodio'})	
	addDir('Ovas','',311,artfolder +"ovas.png",{'title': 'Ovas'})

def listar_fairyTailNormal_ovas():
	addDir('Ovas','',311,artfolder +"ovas.png",{'title': 'Ovas'})
	addLink('Fairy Hills','http://st01hd.animesproject.com.br/vod/F/fairy-tail/MQ/ovas/OVA_01.mp4','http://st01hd.animesproject.com.br/vod/F/fairy-tail/MQ/ovas/OVA_01.jpg')
	addLink('Fairy Academy','http://st01hd.animesproject.com.br/vod/F/fairy-tail/MQ/ovas/OVA_02.mp4','http://st01hd.animesproject.com.br/vod/F/fairy-tail/MQ/ovas/OVA_02.jpg')
	addLink('Dias Memoráveis','http://st01hd.animesproject.com.br/vod/F/fairy-tail/MQ/ovas/OVA_03.mp4','http://st01hd.animesproject.com.br/vod/F/fairy-tail/MQ/ovas/OVA_03.jpg')
	addLink('Acampamento de Treinamento das Fadas','http://st01hd.animesproject.com.br/vod/F/fairy-tail/MQ/ovas/OVA_04.mp4','http://st01hd.animesproject.com.br/vod/F/fairy-tail/MQ/ovas/OVA_04.jpg')
	addLink('Dokidoki Ryuuzetsu Land','http://st01hd.animesproject.com.br/vod/F/fairy-tail/MQ/ovas/OVA_05.mp4','http://st01hd.animesproject.com.br/vod/F/fairy-tail/MQ/ovas/OVA_05.jpg')
	addLink('Fairy Tail X Rave Master','http://st01hd.animesproject.com.br/vod/F/fairy-tail/MQ/ovas/OVA_06.mp4','http://st01hd.animesproject.com.br/vod/F/fairy-tail/MQ/ovas/OVA_06.jpg')
	
def listar_fairyTail2014():
	match = ultimoEpGeral('fairy-tail-2014')
	
	addDir('Fairy Tail 2014','',0,'http://animes.zlx.com.br/imgs/series/small/7c15d47e3be614a.jpg',{'title': 'Fairy Tail'})
	addLink('Ultimo Episodio - ' +match,fairEP +match +'-p-.mp4',fairEP +match +'-p-.jpg')
	
	addDir('Do 00 ate ' +match,'',0,'http://animes.zlx.com.br/imgs/series/small/7c15d47e3be614a.jpg',{'title': 'Do 000 ate ' +match})
	addDir('Ir para o Episodio','',320,artfolder +"goto.png",{'title': 'Ir para o Episodio'})
	
def listar_opm():
	match = ultimoEpGeral('one-punch-man')
	print match
	
	addDir('One Punch Man','',0,'http://animes.zlx.com.br/imgs/series/small/0bebc1c9c64e494.jpg',{'title': 'One Punch Man'})
	addLink('Ultimo Episodio - ' +match,opmEP +match +'-p-.mp4',opmEP +match +'.-p-jpg')
	
	addDir('Do 00 ate ' +match,'',0,'http://animes.zlx.com.br/imgs/series/small/0bebc1c9c64e494.jpg',{'title': 'Do 00 ate ' +match})
	addDir('Ir para o Episodio','',410,artfolder +"goto.png",{'title': 'Ir para o Episodio'})
	addDir('Ovas','',411,artfolder +"ovas.png",{'title': 'Ovas'})

def listar_opm_ovas():
	addDir('Ovas','',411,artfolder +"ovas.png",{'title': 'Ovas'})
	addLink('One Punch Man Ova 1','http://st01hd.animesproject.com.br/vod/O/one-punch-man/MQ/ovas/OVA_01.mp4','http://st01hd.animesproject.com.br/vod/O/one-punch-man/MQ/ovas/OVA_01.jpg')

def listar_kob():
	addDir('Kuroko no Basket 1','',51,'http://animes.zlx.com.br/imgs/series/small/297f0d8181f3f9e.jpg',{'title': 'Kuroko no Basket 1'})
	addDir('Kuroko no Basket 2','',52,'http://animes.zlx.com.br/imgs/series/small/42c34f613cdc731.jpg',{'title': 'Kuroko no Basket 2'})
	addDir('Kuroko no Basket 3','',53,'http://animes.zlx.com.br/imgs/series/small/182a5941eae31f2.jpg',{'title': 'Kuroko no Basket 3'})

def listar_kob1():
	addDir('Kuroko no Basket 1','',51,'http://animes.zlx.com.br/imgs/series/small/297f0d8181f3f9e.jpg',{'title': 'Kuroko no Basket 1'})
	addDir('Do 00 ate 25','',0,'http://animes.zlx.com.br/imgs/series/small/297f0d8181f3f9e.jpg',{'title': 'Do 00 ate 25'})
	addDir('Ir para o Episodio','',510,artfolder +"goto.png",{'title': 'Ir para o Episodio'})	

def listar_kob2():
	addDir('Kuroko no Basket 2','',52,'http://animes.zlx.com.br/imgs/series/small/42c34f613cdc731.jpg',{'title': 'Kuroko no Basket 2'})
	addDir('Do 00 ate 25','',0,'http://animes.zlx.com.br/imgs/series/small/42c34f613cdc731.jpg',{'title': 'Do 00 ate 25'})
	addDir('Ir para o Episodio','',520,artfolder +"goto.png",{'title': 'Ir para o Episodio'})	

def listar_kob3():
	addDir('Kuroko no Basket 3','',53,'http://animes.zlx.com.br/imgs/series/small/182a5941eae31f2.jpg',{'title': 'Kuroko no Basket 3'})
	addDir('Do 00 ate 25','',0,'http://animes.zlx.com.br/imgs/series/small/182a5941eae31f2.jpg',{'title': 'Do 00 ate 25'})
	addDir('Ir para o Episodio','',530,artfolder +"goto.png",{'title': 'Ir para o Episodio'})	
	
def goto_geral(letra,serie):
	ultimoEP = ultimoEpGeral(serie)
	
	if str(ultimoEP) == "???":
		keyb = xbmc.Keyboard('', 'Sem ultimo ep de momento, defina um numero maximo')	
		keyb.doModal()
		if (keyb.isConfirmed()):
			search = keyb.getText()
			ultimoEP = int(urllib.quote(search))
	
	keyb = xbmc.Keyboard('', 'Ir para o Episodio')	
	keyb.doModal()
	if (keyb.isConfirmed()):
		search = keyb.getText()
		_ep = int(urllib.quote(search))
		print serie +" _ep: " +str(_ep)
		
		
		for epN in range(_ep, int(ultimoEP)+1):
			epF = str(epN)
			_cast = ''
			
			if (serie=='fairy-tail-2014' or serie=='one-punch-man' or serie=='kuroko-no-basket-3') and (epN<82 or epN>84):
				_cast = '-p-'
				
			print str(epN) +"_cast: " +_cast
			
			if serie=='fairy-tail-2014' or serie=='one-punch-man' or serie=='kuroko-no-basket' or serie=='kuroko-no-basket-2' or serie=='kuroko-no-basket-3':
				if epN > 0 and epN < 10:
					epF = '0' +str(epN)
				elif epN > 9:
					epF = str(epN)
			else:
				if epN > 0 and epN < 10:
					epF = '00' +str(epN)
				elif epN > 9 and epN < 100:
					epF = '0' +str(epN)
			
			url = geralURL +letra +'/' +serie +'/MQ/episodios/' +epF +_cast
			addLink('Episodio - ' +epF,url +'.mp4',url +'.jpg')
			
def ultimoEpGeral(serie):
	if serie=='one-piece':
		url = 'http://animes.zlx.com.br/serie/117/0/One-Piece'
	elif serie=='naruto':
		return 220
	elif serie=='naruto-shippuuden':
		url = 'http://animes.zlx.com.br/serie/144/0/Naruto-Shippuuden'
	elif serie=='fairy-tail':
		return 259
	elif serie=='fairy-tail-2014':
		url = 'http://animes.zlx.com.br/serie/1091/0/Fairy-Tail-2014'
	elif serie=='one-punch-man':
		url = 'http://animes.zlx.com.br/serie/1214/0/One-Punch-Man'
	elif serie=='kuroko-no-basket' or serie=='kuroko-no-basket-2' or serie=='kuroko-no-basket-3':
		return 25
		
	epF = re.compile('Assista online o último vídeo lançado do anime .+?, o Episódio (.+?)"').findall(obterURL(url)) 
	#'<a alt="Assista online o último vídeo lançado do anime One Punch Man, o Episódio 09" href="/serie/1214/1954/One-Punch-Man-Episodio-09">Episódio 09</a>'
	
	#
	print "epF: " +str(epF)
	try:
		if str(epF[0]) == "":
			epF[0] = "???"
	except:	
		return "???"
	return str(epF[0])

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
	listar_onepiece()
elif mode==2:
	listar_naruto()
elif mode==3:
	listar_fairyTail()
elif mode==4:
	listar_opm()
elif mode==5:
	listar_kob()
elif mode==13:
	listar_onepiece_filmes()
elif mode==21:
	listar_narutoNormal()
elif mode==211:
	listar_narutoNormal_filmes()
elif mode==22:
	listar_narutoShippuuden()
elif mode==221:
	listar_narutoShippuuden_filmes()
elif mode==31:
	listar_fairyTailNormal()
elif mode==311:
	listar_fairyTailNormal_ovas()
elif mode==32:
	listar_fairyTail2014()
elif mode==411:
	listar_opm_ovas()
elif mode==51:
	listar_kob1()
elif mode==52:
	listar_kob2()
elif mode==53:
	listar_kob3()
elif mode==110:
	goto_geral('O','one-piece')
elif mode==210:
	goto_geral('N','naruto')
elif mode==220:
	goto_geral('N','naruto-shippuuden')
elif mode==310:
	goto_geral('F','fairy-tail')
elif mode==320:
	goto_geral('F','fairy-tail-2014')
elif mode==410:
	goto_geral('O','one-punch-man')
elif mode==510:
	goto_geral('K','kuroko-no-basket')
elif mode==520:
	goto_geral('K','kuroko-no-basket-2')	
elif mode==530:
	goto_geral('K','kuroko-no-basket-3')
	
xbmcplugin.endOfDirectory(__handle__)