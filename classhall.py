"""
OOPs-equals() method


 Praveen works for as a Reservation manager, he keeps the record of all the booking details and reservations. But he wants to automate it since manually maintainig all the files consumes a lot of time. So,  he asks help from the Development team to write a code which takes the details of of 'n' number of entries of the halls followed by the hall details which includes Hall name, Contact and Address of the user, Booking Date, Cost and owner of the Hall. And finds whether the hall is available for registration or not by comparing the name, Phone number and the booking date of the booking. If yes, add it to hall details list and display the Booked Hall.If not, the display "Already registered".

Create Hall class with following attribute.

DataType	Variable
String	Name
Integer	Phone number
String	Address
Date	 bookingDate
Float	Cost
String	Owner
Initialize the constructor using "__init__()" method.
Create an object of this Hall class using above mentioned constructor.
Use the following methods in Hall class.



Method	Description
Equals()	To check whether all the details of hall match or not.
Display()	Display all the details of hall

Input Format:
Input consists of an integer 'n' indicating the number of entries followed by the details of 'n' number of halls. Next the user is asked to enter the hall details to be booked.

Output format:
The output should display "Already registered" if the halls are booked followed by the booked hall details.
The output should display "Registration Available" if the hall to be booked is available followed by the booked hall details.

Refer sample input and output for formatting specifications.

All text in bold corresponds to the input and the rest corresponds to output.

Input-Output Sample:
Enter the number of Entries
1
Enter details of Hall 1
Enter Hall name
chandan palace
Enter Phone
9876540321
Enter Address
Chandan Palce,RamakrishnaNagar,Mysore
Enter Date of booking
Dec 12 2017
Enter cost
1243
Enter owner name
Chandan

Enter the Hall details for booking
Enter Hall name
chandan palace
Enter Phone
9876540321
Enter Address
Chandan Palce,RamakrishnaNagar,Mysore
Enter Date of booking
Dec 12 2017
Enter cost
1243
Enter owner name
Chandan

Already Registered

Display the Booked Hall details
Hall name :chandan palace
Phone No : 9876540321
Address :Chandan Palce,RamakrishnaNagar,Mysore
Cost :1243.00
Owner name :Chandan

"""


class Hall:
    name=[]
    phone=[]
    add=[]
    date=[]
    cost=[]
    owner=[]
    def __init__(self,a,b,c,d,e,f):
        self.name=a
        self.phone=b
        self.add=c
        self.date=d
        self.cost=e
        self.owner=f
        
    def equal(self,a,b,c,d,e,f):
        flag=0
        if a in self.name and b in self.phone and d in self.date:
            flag=1
        if flag==0:
            print("Registration available")
            self.name.append(a)
            self.phone.append(b)
            self.add.append(c)
            self.date.append(d)
            self.cost.append(e)
            self.owner.append(f)
        else:
            print("Already Registered")
            
    def display(self):
        print("Display the Booked Hall details")
        for i in range(len(self.name)):
            print("Hall name :{}".format(self.name[i]))
            print("Phone No : {}".format(self.phone[i]))
            print("Address :{}".format(self.add[i]))
            print("Cost :{:.2f}".format(self.cost[i]))
            print("Owner name :{}".format(self.owner[i]))
            
        
    
        
n=int(input("Enter the number of Entries\n"))
a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
for i in range(n):
    print("Enter details of Hall",i+1)
    a.append(input("Enter Hall name\n"))
    b.append(int(input("Enter Phone\n")))
    c.append(input("Enter Address\n"))
    d.append(input("Enter Date of booking\n"))
    e.append(int(input("Enter cost\n")))
    f.append(input("Enter owner name\n"))
ob=Hall(a,b,c,d,e,f)
print("Enter the Hall details for booking\n")
name1=input("Enter Hall name\n")
phone1=int(input("Enter Phone\n"))
add1=input("Enter Address\n")
date1=input("Enter Date of booking\n")
cost1=int(input("Enter cost\n"))
owner1=input("Enter owner name\n")
ob.equal(name1,phone1,add1,date1,cost1,owner1)
ob.display()

