from json2html import *
import json

f = open('Sheet1.json')

input = json.load(f)
htmlform =json2html.convert(json = input)
Func = open("htmlfile1.html","w")
text='''
<html>
    <head>
        <title>HTML Report</title>
        <style type="text/css">
                  table          {border:ridge 5px #AED6F1  ;}
                  table tr  {background-color:#76D7C4  ;}
                  table td  {border:ridge 2px #AED6F1  ;}
                  table th  {background-color:#2471A3  ;color:white}
                  table tr:nth-child(even) {background-color: #f2f2f2;}
        </style>
    </head>
    <body>
        <h1 style="color:#154360;font-family: cursive;font-size: 300%;">STATUS REPORT :</h1>
    </body>
</html>
'''
Func.write(text)
Func.write(htmlform)
  
# Saving the data into the HTML file
Func.close()
f.close()

