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


versao = '2.0'
addon_id = 'plugin.video.skudme'
selfAddon = xbmcaddon.Addon(id=addon_id)
addonfolder = selfAddon.getAddonInfo('path')
artfolder = addonfolder + '/resources/img/'
fanart = addonfolder + '/fanart.jpg'

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

def getInfo(url, infoN):
	if infoN == 1:		
		animeName = re.compile('<h2 class="panel-title"><span itemprop="name">(.+?)</span></h2>').findall(obterURL(url))
		return animeName[0]
	elif infoN == 2:
		imgAnime = re.compile('<img class=" img-hover" src="(.+?)" alt=".+?" title=".+?" width="250">').findall(obterURL(url))
		return 'https://www.anitube.es' +imgAnime[0]
	elif infoN == 3:
		nTotalEps = re.compile('<span itemprop="numberofEpisodes">.+?/(.+?)</span>').findall(obterURL(url))
		return int(nTotalEps[0])
	else:
		return 'Erro'
	
	
def MenuPrincipal():
	menuPrincipal = re.compile('<li><a href="/anime/(.+?)">(.+?)</a></li>').findall(obterURL('https://www.anitube.es/anime'))
	for n in range(0, len(menuPrincipal)):
		addDir(menuPrincipal[n][1],'https://www.anitube.es/anime/' +menuPrincipal[n][0],1,'',{'title': menuPrincipal[n][1]}) 

def	listarAnimes():
	url = urllib2.unquote(sys.argv[2].split('&url=')[1])
	listaAnimes = re.compile('<h2 class="go"><a class="internalUrl" href="(.+?)" title="(.+?)" rel="bookmark" itemprop="name">').findall(obterURL(url))
	listaAnimesImg = re.compile('<img class="img-responsive" alt=".+?" title=".+?" src="(.+?)" itemprop="image">').findall(obterURL(url))
			
	for x in range(0, len(listaAnimesImg)):
		addDir(listaAnimes[x][1], 'https://www.anitube.es' +listaAnimes[x][0],2, 'https://www.anitube.es' +listaAnimesImg[x],{'title': listaAnimes[x][1]})
	
	
def listarAnime():
	url = urllib2.unquote(sys.argv[2].split('&url=')[1])
	AnimeName = getInfo(url,1)
	nTotalEps = getInfo(url, 3)
	nPaginas = 1
	
	addDir(AnimeName +' - ' +str(nTotalEps) +' Eps','',2,getInfo(url,2),{'title':AnimeName +' ' +str(nTotalEps) +' Eps'})
	
	if nTotalEps % 12 == 0:
		nPaginas = nTotalEps/12
	else:
		nPaginas += int(nTotalEps)
	
	for epN in range(1, nPaginas+1):
		printEps(AnimeName, url +'/page/' +str(epN))
		
def printEps(animeName, url):
	EPSurl = re.compile('<a itemprop="url" href="(.+?)>').findall(obterURL(url))
	EPS = re.compile('<img src="(.+?)" title="(.+?)" alt=".+?"  class="img-responsive "/>').findall(obterURL(url))	
	for n in range(0, len(EPS)):
		addDir(EPS[n][1],'https://www.anitube.es' +EPSurl[n],3,'https://www.anitube.es' +EPS[n][0],{'title':EPS[n][1]})
		
def verEp():
	url =  urllib2.unquote(sys.argv[2].split('&url=')[1]).replace('"', '')
		
	videoUrl = re.compile('<script type="text/javascript" src="https://www.anitube.es/insertVideo/(.+?)"></script>').findall(obterURL(url))
	videoUrl = 'https://www.anitube.es/insertVideo/' +videoUrl[0]
	videoQualidade = re.compile("source: '(.+?)',").findall(obterURL(videoUrl))
	
	addLink('SD',videoQualidade[0],'')
	addLink('HD',videoQualidade[1],'')
	
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
	listarAnimes()
elif mode==2:
	listarAnime()
elif mode==3:
	verEp()
	
xbmcplugin.endOfDirectory(__handle__)
