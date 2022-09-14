"""
College Details

A technical event was conducted by the Government of India for the various colleges from all over India. On the valedictory function, a momento was given to all the colleges with the college details inscribed on it. The momento's order was given to a famous epigrapher who does it manually.  But since many colleges had participated it was difficult for him to do it manually. So he requests the management team to arrage a software code which would display the college details so that it would be easy for him to put it in his machine. The management team asks the development team to write a code which display the college details (specified in the Input format). Imagine you are working in the development team and this work is assigned to you. Write a code as per the requirement.
Create a base class CollegeName with one variable:


Data Type	Variable Name
String	collegeName


Use an appropriate constructor.

Create a base class Establishment with one variable:



Data Type	Variable Name
Integer	establishment


Use an appropriate constructor.

Create a Class Detais with the following attributes which is derived from both CollegeName and Establishment

Data Type	Variable Name
Integer	numOfDepts
String	address

Include appropriate constructor.
Override the str() method to display the details in the format shown in the output in the class.

Input and Output Format:
Input consists of college(string), Year of Establishment (integer), Number of departments (integer) and address( string).
Refer sample input and output for formatting specifications.

All text in bold corresponds to input and rest correspond to output.

Sample Input and Output:
College Details
Enter the College name
GSSS
Year of Establishment
2003
Enter the number of departments
50
Enter the address
West Siang, Arunachal Pradesh
College name : GSSS
Year of Establishment : 2003
Number of departments : 50
Address : West Siang, Arunachal Pradesh


Additional Sample TestCases
Sample Input and Output 1 :
College Details
Enter the College name
GSSS
Year of Establishment
2003
Enter the number of departments
50
Enter the address
West Siang, Arunachal Pradesh
College name : GSSS
Year of Establishment : 2003
Number of departments : 50
Address : West Siang, Arunachal Pradesh
"""
class CollegeName:
    collegeName=""
    def __init__(self):
         self.collegeName = input("College Details\nEnter the College name\n")
class Establishment:
    establishment=0
    def __init__(self):
         self.establishment = int(input("Year of Establishment\n"))
class Details(CollegeName,Establishment):
    numOfDepts=0
    address=""
    def __init__(self):
         CollegeName.__init__(self)
         Establishment.__init__(self)
         self.numOfDepts = int(input("Enter the number of departments\n"))
         self.address = input("Enter the address\n")
    def __str__(self):
        return f'College name : {self.collegeName} \n Year of Establishment : {self.establishment} \nNumber of departments :{self.numOfDepts}\n Address : {self.address}'

ob=Details()
print(ob)