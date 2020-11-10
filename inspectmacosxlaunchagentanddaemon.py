import os
from pathlib import Path
def crawlAgentsAndDaemons():

    agentsNDaeomns={
        str(Path.home())+'/Library/LaunchAgents':['Currently logged in user'],
        '/Library/LaunchAgents':['Currently logged in user'],
        '/Library/LaunchDaemons':['root or the user specified with the key UserName'],
        '/System/Library/LaunchAgents':['Currently logged in user'],
        '/System/Library/LaunchDaemons':['root or the user specified with the key UserName']
    }
    directories=list(agentsNDaeomns.keys())
    for dirs in directories:
        print ("============"+dirs+"===========")
        print ()
        plistFiles=os.listdir(dirs)
        #print(plistFiles)
        for pfiles in plistFiles:
            print ("Application Name: "+pfiles)
            print()
            fileOpen=open(dirs+'/'+pfiles)
            try:
             fileRead=fileOpen.read()
             print(fileRead)
             fileOpen.close()
            except(UnicodeDecodeError):
               
                try:
                 os.system('plutil -convert xml1 '+dirs+'/'+pfiles)
                 fileOpen=open(dirs+'/'+pfiles)
                 fileRead=fileOpen.read()
                 print(fileRead)
                 fileOpen.close()
                 os.system('plutil -convert binary1 '+dirs+'/'+pfiles)
                except:
                    pass



crawlAgentsAndDaemons()         
