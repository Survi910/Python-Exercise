import xml.etree.ElementTree as ET 
import os
from pathlib import Path
import shutil

rootdir = './SAMPLEWork'
string1="Final Verdict:INCONC"
flag=0
l=[]
for file in os.listdir(rootdir):
    d = os.path.join(rootdir, file)
    if os.path.isdir(d):
        for file in os.listdir(d):
            sub = os.path.join(d, file)
            if os.path.isdir(sub):
                flag=0     
                for file in os.listdir(sub):
                    if Path(file).suffix == '.cfa':
                        flag=1
                        for file in os.listdir(sub):
                            if Path(file).suffix == '.xml':
                                check=open(sub+"/"+file,"r")
                                readfile = check.read()
                                if string1 in readfile: 
                                    print('String', string1, 'Found In File')
                                    print(sub)
                                    l.append(file)
                                    check.close() 
                                else:
                                    shutil.rmtree(sub, ignore_errors=True)
                                    print("==========String not found folder deleted=============")

                if flag == 0:
                    shutil.rmtree(sub, ignore_errors=True)
                    print("----------cfa folder deleted -----------")

    
    for file in os.listdir(d):
        if file == 'tc_log.xml':
            tree = ET.parse(d+"\\"+file)
            root = tree.getroot()
            for i in root.findall("TCASE"): 
                log=i.findtext("LOG")
                log=log.replace("\\","/")
                da=log.split("/")
                if da[1] not in l:
                    root.remove(i)
            tree.write(d+"\\"+file)

            print("process completed")    
         
    
        

                        
                            
                        
                        
                        

                    
                        
                        
                        
