import urllib
from EasyDialogs import ProgressBar
from urllib import urlretrieve
import os
from easygui import *
import sys

def download(url, filename):
    bar = ProgressBar(title='Downloading... ', label=videotitle)

    def report(block_count, block_size, total_size):
        prevt=time.time()
        prev=(bar.curval/1024.0)
        if block_count == 0:
            bar.set(0, total_size)
        bar.inc(block_size)
        currentt=time.time()
        current=bar.curval/1024.0
        if (currentt-prevt)!=0:
            totalt=1/(currentt-prevt)
        else:
            totalt=1
        total=str(bar.maxval/1024.0)+" Kb"
        print str(current)+" Kb"+'/'+total          #+' -------------at '+str((current-prev)*totalt)+ " Kbs "
        

    urlretrieve(url, filename, reporthook=report)
ans='y'
while True:
    msg='Want to download a youtube video?'
    title='Youtube downloader  - Made by Aaditya Gavandalkar'
    if ccbox(msg,title):
        while ans=='y' or ans=='Y':
            url=enterbox(msg='Enter youtube video URL', title='Youtube Downloader  - Made by Aaditya Gavandalkar', default="enter the youtube video url : ", strip=True, image=None, root=None)
            urldata=urllib.urlopen(url).read()
                        
            #getting the video title
            y=urldata.find('<title>')
            z=urldata.find('- YouTube')
            urldata2=urldata[y+8:z]
            videotitle=urldata2


            #getting all video urls
            urllist=range(20)
            quality=range(20)
            x=urldata.find('\/\/')
            afterF=urldata[x+1:x+1]
            
            for a in range(20):
                newurldata=urldata
                x=newurldata.find('http%3A%2F%2F'+afterF)
                if x<0:
                    break
                y=newurldata.find('\u0026quality')
                if y<0:
                    break
                tempurl=str(newurldata[x:y])
                tempurl=tempurl.replace('%3A',':')
                tempurl=tempurl.replace('%2F','/')
                tempurl=tempurl.replace('%3F','?')
                tempurl=tempurl.replace('%26','&')
                tempurl=tempurl.replace('%3D','=')
                tempurl=tempurl.replace('%252','%2')
                p=tempurl.find('\u0026type=')
                q=tempurl.find('\u0026sig=')
                tempurl=tempurl[:p]+'&signature'+tempurl[q+9:]
                urllist[a]=tempurl
                urldata=newurldata[y:]
                newurldata=urldata
                p=newurldata.find('\u0026quality')
                q=newurldata.find(',')
                quality[a]=newurldata[p+14:q]
                urldata=newurldata[p+14:]
                
            for i in range(10):
                ulstr=str(urllist[i])
                qstr=str(quality[i])
                if ulstr[0:3] != "htt":
                    quality[i]="Cancel Download"
                    break
                
            choices=range(i+1)
            for j in range(i):
                if j==i-1:
                    qstr=str(quality[j])
                    choices[j]=qstr[0:-1]
                else:
                    choices[j]=quality[j]
            choices[j+1]="Cancel Download"
            msg="Which Format To Download"
            title="Youtube Downloader  - Made by Aaditya Gavandalkar"
            reply=buttonbox(msg,title,choices=choices)
            if reply=="Cancel Download":
                sys.exit(0)
            else:
                for k in range(i):
                    if quality[k]==reply:
                        break
                videourl=urllist[k]         #final video url
                path=filesavebox(msg='Where to save', title='Saving options', default=videotitle+'.flv', filetypes=None)

                if path==None:
                    sys.exit(0)
                else:
                    url = videourl
                    filename = path
                    download(url, filename)
                    msgbox("Download completed successfully !!!")
                    msg="Want to download more videos !"
                    choices=["Yes","No"]
                    title='Youtube Downloader  - Made by Aaditya Gavandalkar'
                    reply=buttonbox(msg,title,choices=choices)
                    if reply=='Yes':
                        ans='y'
                    else :
                        msgbox("Thank You for using this software\nHope you liked it and will use it again !!")
                        ans='n'
                        sys.exit(0)
    else:
        msgbox("Thank You for using this software\nHope you liked it and will use it again !!")
        sys.exit(0) 
