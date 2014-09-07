import urllib
from urllib import urlretrieve
import time
import sys
import os

curval=0

filename=""
def download(url, filename):
    
    def report(block_count, block_size, total_size):
        curval=os.path.getsize(filename)
        prevt=time.time()
        #prev=(bar.curval/1024.0)
        prev=(curval/1024.0)
        currentt=time.time()
        current=curval/1024.0
        
        if (currentt-prevt)!=0:
            totalt=1/(currentt-prevt)
        else:
            totalt=1
        total=str(total_size/1024.0)+" Kb"
        print str(current)+" Kb"+'/'+total          #+' -------------at '+str((current-prev)*totalt)+ " Kbs "
        

    urlretrieve(url, filename, reporthook=report)
ans='y'
while True:
    msg='Want to download a youtube video?(y/n)'
    ans=raw_input(msg)
    if ans=='y' or ans=='Y':
        while ans=='y' or ans=='Y':
            url=raw_input("Enter the video URL : ")
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
            print "\nFormats available for download are :"    
            choices=range(i+1)
            for j in range(i):
                if j==i-1:
                    qstr=str(quality[j])
                    choices[j]=qstr[0:-1]
                else:
                    choices[j]=quality[j]
                print str(j+1)+") "+choices[j]
            choices[j+1]="Cancel Download"
            print str(j+2)+") "+choices[j+1]
            k = input("\n\nWhich Format To Download (Enter the number in front of that option here)")
            #reply=buttonbox(msg,title,choices=choices)
            if choices[k-1]=="Cancel Download":
                sys.exit(0)
            else:
                videourl=urllist[k-1]         #final video url
                path=raw_input("Enter the path where file is to be saved : ")
                if path[-4:-1]!='.fl' and path != None:
                    path=path+videotitle+'.flv'
                if path==None:
                    sys.exit(0)
                else:
                    url = videourl
                    filename = path
                    download(url, filename)
                    print "Download completed successfully !!!"
                    ans=raw_input("Want to download more videos ?(y/n)")
                    if ans!='y' and ans!='Y':
                        print "Thank You for using this software\nHope you liked it and will use it again !!"
                        ans='n'
                        sys.exit(0)
    else:
        print "Thank You for using this software\nHope you liked it and will use it again !!"
        sys.exit(0) 
