import xml.etree.ElementTree as ET 
import os
import pathlib
import shutil
import sys
import xlsxwriter


def excelsheet(dirList,path,l1):
    row=0
    column=0        
    workbook = xlsxwriter.Workbook('data.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write(0,0,"TestCase")
    worksheet.write(0,1,"Date")
    worksheet.write(0,2,"Status")
    row=1
    for dirs in dirList:
        dirname=path+"/"+dirs+"/tc_log.xml"
        tree = ET.parse(dirname) 
        root = tree.getroot()
        
        for i in root.findall("TCASE"):
            name=i.findtext("NAME")
            worksheet.write(row,0,name)
            date=i.findtext("DATE")
            worksheet.write(row, 1,date)
            verdict=i.findtext("VERDICT")
            worksheet.write(row,2,verdict)
            row+=1

    workbook.close()  

def checkstring(dirList,path,string1,string2):
    flag=0
    l=[]
    try:
        for file in dirList:
            dirpath=path+"/"+file
            for file in os.listdir(dirpath):
                sub = os.path.join(dirpath, file)
                if os.path.isdir(sub):
                    flag=0     
                    for file in os.listdir(sub):
                        if pathlib.Path(file).suffix == '.cfa':
                            flag=1
                            for file in os.listdir(sub):
                                if pathlib.Path(file).suffix == '.xml':
                                    check=open(sub+"/"+file,"r")
                                    readfile = check.read()
                                    if string1 in readfile or string2 in readfile: 
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
        return l
    except FileNotFoundError:
        print('Invalid directory')

def removeFailTestCases(dirList,path,l1):
    try:
        for dirs in dirList:
            dirname=path+"/"+dirs+"/tc_log.xml"
            tree = ET.parse(dirname) 

            # get the parent tag 
            root = tree.getroot()
            # print the root (parent) tag along with its memory location 
            for i in root.findall("TCASE"): 
                log=i.findtext("LOG")
                log=log.replace("\\","/")
                da=log.split("/")
                
                if da[1] not in l1:
                    root.remove(i)
            tree.write(dirname)

            print("process completed")
        
                    
            
    except Exception as ez:
        print(ez)



def path_dir(dir):
    path = pathlib.Path(dir)
    dir = []
    try:
        for item in path.iterdir():
            itemdataList=False
            for itemdata in item.iterdir():
                if itemdata.name.split("/")[-1]=="tc_log.xml":
                    itemdataList=True
            if itemdataList:
                if item.name.split("/")[-1] in ['A2DP', 'BAS', 'DID', 'DIS', 'HFP','RFCOMM']:
                    dir.append(item.name.split("/")[-1])
        return dir
    except FileNotFoundError:
        print('Invalid directory')

def main():

    path="./SAMPLEWork"
    string1="Final Verdict:INCONC"
    string2="Final Verdict:PASS"
    flag=0
    l=[]
    dirList=path_dir(path)
    l1=checkstring(dirList,path,string1,string2)
    removeFailTestCases(dirList,path,l1)
    excelsheet(dirList,path,l1)
main()
    
        

                        
                            
                        
                        
                        

                    
                        
                        
                        
