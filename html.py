from json2html import *
input = [
    {
        "TestCase": "A2DP/SRC/AS/BV-01-I",
        "Date": "09/14/2020 18:06:34",
        "Status": "PASS"
    },
    {
        "TestCase": "A2DP/SNK/CC/BV-08-I",
        "Date": "09/14/2020 18:06:20",
        "Status": "FAIL"
    },
    {
        "TestCase": "A2DP/SNK/CC/BV-06-I",
        "Date": "09/14/2020 17:59:28",
        "Status": "PASS"
    },
    {
        "TestCase": "A2DP/SNK/CC/BV-05-I",
        "Date": "09/14/2020 17:58:52",
        "Status": "PASS"
    },
    {
        "TestCase": "A2DP/SNK/CC/BV-02-I",
        "Date": "09/14/2020 17:57:45",
        "Status": "PASS"
    },
    {
        "TestCase": "A2DP/SNK/CC/BV-01-I",
        "Date": "09/14/2020 17:56:29",
        "Status": "PASS"
    },
    {
        "TestCase": "A2DP/SNK/AS/BV-01-I",
        "Date": "09/14/2020 17:53:54",
        "Status": "PASS"
    },
    {
        "TestCase": "BAS/SR/CN/BV-01-C",
        "Date": "09/14/2020 19:15:49",
        "Status": "PASS"
    },
    {
        "TestCase": "BAS/SR/CON/BV-01-C",
        "Date": "09/14/2020 18:09:54",
        "Status": "INCONC"
    },
    {
        "TestCase": "BAS/SR/CR/BV-01-C",
        "Date": "09/14/2020 18:07:15",
        "Status": "PASS"
    },
    {
        "TestCase": "BAS/SR/DEC/BV-01-C",
        "Date": "09/14/2020 18:06:55",
        "Status": "INCONC"
    },
    {
        "TestCase": "DIS/SR/DEC/BV-05-C",
        "Date": "09/14/2020 20:05:01",
        "Status": "PASS"
    },
    {
        "TestCase": "DIS/SR/DEC/BV-06-C",
        "Date": "09/14/2020 20:04:39",
        "Status": "FAIL"
    },
    {
        "TestCase": "DIS/SR/DEC/BV-01-C",
        "Date": "09/14/2020 20:04:03",
        "Status": "PASS"
    },
    {
        "TestCase": "DIS/SR/DEC/BV-03-C",
        "Date": "09/14/2020 20:03:37",
        "Status": "PASS"
    },
    {
        "TestCase": "HFP/HF/CIT/BV-01-I",
        "Date": "09/15/2020 08:02:46",
        "Status": "PASS"
    },
    {
        "TestCase": "HFP/HF/TCA/BV-04-I",
        "Date": "09/15/2020 08:02:28",
        "Status": "PASS"
    },
    {
        "TestCase": "HFP/HF/TCA/BV-02-I",
        "Date": "09/15/2020 08:02:10",
        "Status": "PASS"
    },
    {
        "TestCase": "HFP/HF/ICA/BV-06-I",
        "Date": "09/15/2020 08:01:44",
        "Status": "PASS"
    },
    {
        "TestCase": "HFP/HF/ICA/BV-01-I",
        "Date": "09/15/2020 08:01:17",
        "Status": "INCONC"
    },
    {
        "TestCase": "HFP/HF/ACR/BV-02-I",
        "Date": "09/15/2020 08:00:54",
        "Status": "PASS"
    },
    {
        "TestCase": "HFP/HF/OOR/BV-01-I",
        "Date": "09/15/2020 07:59:43",
        "Status": "PASS"
    }
]
htmlform =json2html.convert(json = input)
Func = open("htmlfile.html","w")
  
# Adding input data to the HTML file
Func.write(htmlform)
  
# Saving the data into the HTML file
Func.close()
