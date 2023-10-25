from validation import *
def validID(e):
    for i in Emp:
        if i.emp_id==e:
            return False
    return True

class Employee:
    def __init__(self,emp_id,name,salary,age,gender,address,city,DOB,DOJ,dept_name,designation,pan_no,adhar_no):
        self.emp_id=emp_id
        self.name=name
        self.salary=salary
        self.age=age
        self.gender=gender
        self.address=address
        self.city=city
        self.DOB=DOB
        self.DOJ=DOJ
        self.dept_name=dept_name
        self.designation=designation
        self.pan_no=pan_no
        self.adhar_no=adhar_no
    def display(self):
        print(self.emp_id," ",self.name," ",self.salary," ",self.age," ",self.gender," ",self.address," ",self.city," ",self.DOB," ",self.DOJ," ",self.dept_name," ",self.designation," ",self.pan_no," ",self.adhar_no)
Emp=[]
while True:
     print("1 :- Add a Record of Employee ")
     print("2 :- Display Record of Employee ")
     print("3 :- Delete The Record Of Employee ")
     print("4 :- Update Employee Details ")
     print("5 :- Search Employee Details  ")
     print("6 :- Display theDetalis 0f Employee with Highest salary")
     print("7 :- Display theDetalis 0f Employee with lowest salary")
     print("8 :- Know how long a employee is working in the organization from him Employee ID")
     print("9 :- Exit")
     choice = int(input("Enter your choice: "))
     if choice==1:
         while True:
             emp_id=input("Enter the Employee ID: ")
             if validID(emp_id):
                 print("Employee ID registered Success", emp_id)
                 break
             else:
                 print("Enter Valid ID. ")       
         while True:
             emp_name=input("Enter the Employee Name: ")
             if validname(emp_name):
                 break
             else:
                 print("Enter Valid name. ")
         while True:
             mobile=input("Enter the Employee mobile: ")
             if validmobileno(mobile):
                 break
             else:
                 print("Enter Valid mobile no. ")
         while True:
             salary=input("Enter the Employee Salary: ")
             if validsalary(salary):
                 break
             else:
                 print("Enter Valid Salary. ")
         while True:
             print("Enter your age as directed: \n")
             year=int(input("Enter your Birth year: "))
             month=int(input("Enter your Birth month: "))
             day=int(input("Enter your Birth day: "))
             dob=date(year, month, day)
             age=calculateAge(date(year, month, day))
             if age:
                 print("DOB register success.\n Your age is: ",age ,dob)
                 break
             else:
                 print("Enter Valid Date. ")
         while True:
             Gender=input("Enter the Employee Gender: ")
             if validgender(Gender):
                 break
             else:
                 print("Enter Valid Gender. ")
                 
         address = input("Enter your address : ")
         while True:
             state=input("Enter your state Name: ")
             City=input("Enter your City Name: ")
             if validcity(state,City):
                 break
             else:
                 print("Enter Valid City. ")
         while True:
             dept_name=input("Enter your department Name: ")
             if validdepartment(dept_name):
                 break
             else:
                 print("Enter Valid department. ")
         while True:
             designation=input("Enter your designation Name: ")
             if validdesignation(designation):
                 break
             else:
                 print("Enter Valid designation. ") 
         while True:
             pan_card_no=input("Enter your pan_card_no: ")
             if validpan(pan_card_no):
                 break
             else:
                 print("Enter Valid pan_card_no. ") 
         while True:
             adhar_number=input("Enter your adhar Number: ")
             if validadhar(adhar_number):
                 break
             else:
                 print("Enter Valid adhar. ") 
         while True:
             print("Enter your date of Joining as directed: \n")
             join_year=int(input("Enter your Joining year: "))
             join_month=int(input("Enter your Joining month: "))
             join_day=int(input("Enter your Joining age: "))
             doj=date(join_year, join_month, join_day)
             join_age=calculateAge(date(join_year, join_month, join_day))
             if join_age:
                 print("DOJ register success.\n Your Date of Joining is: ",join_age ,doj)
                 break
             else:
                 print("Enter Valid Date. ")
         E=Employee(emp_id,emp_name,salary,age,Gender,address,City,dob,doj,dept_name,designation,pan_card_no,adhar_number)
         Emp.append(E)
     elif choice==2:
        print("Details of Employee")
        for i in Emp:
             i.display()
     elif choice==3:
        e=input("enter the emp_id to be delete in the record")
        for i in Emp:
            if i.emp_id==e:
                Emp.remove(i)
     elif choice==4:
        print("press 1 to update details of specific employee")
        print("press 2 to update salary of specific department")
        print("press 3 to update salary of all employees")
        ch1=int(input("Enter your choice for updation: "))
        print(ch1)
        if ch1==1:
            e=input("enter the emp_id whose records you want to update")
            for i in Emp:
             if i.emp_id==e:
                print("press A to update name")
                print("press B to update adress of Employee")
                print("press C to update DOB of Employee")
                print("press D to update Salary of Employee")
                ch=input("enter your choice")
                if ch=="A":
                   nm=input("enter the updated name")
                   i.name=nm
                elif ch=="B":
                     adr=input("enter the updated adress")
                     i.address=adr
                elif ch=="C":
                    print("Enter your DOB to be updated as directed: \n")
                    year=int(input("Enter your Birth year: "))
                    month=int(input("Enter your Birth month: "))
                    day=int(input("Enter your Birth age: "))
                    dob=date(year, month, day)
                    i.DOB=dob
                elif ch=="D":
                    salary_updated=input("enter the updated Salary")
                    i.salary=salary_updated
                else:
                    print("invalid choice")
        elif ch1==2:
            department_updated=input("Enter the department name whose salary needs to be updated")
            salary_update=input("Enter the updated salary")
            for i in Emp:
                if i.dept_name==department_updated:
                    i.salary=salary_update
        elif ch1==3:
            salary_update_all=input("Enter the salary which needs to be updated for all")
            for i in Emp:
                i.salary=salary_update_all
     elif choice==5:
         print("enter choice I to search by employee ID")
         print("enter choice II to search by name")
         print("enter choice III to search by Department name")
         ch=input("enter your choice")
         if ch=="I":
             eid=input("enter the employee id  to be search")
             for i in Emp:
                 if i.emp_id==eid:
                     i.display()
         elif ch=="II":
             nm = input("enter the name to be search")
             for i in Emp:
                 if i.name==nm:
                     i.display()
         elif ch=="III":
             dep=input("enter the department name to be search")
             for i in Emp:
                 if i.dept_name==dep:
                     i.display()
     elif choice==6:
         salary_list=[]
         for i in Emp:
             salary_list.append(i.salary)
         print('Maximum salary is ', max(salary_list))
     elif choice==7:
         salary_list=[]
         for i in Emp:
             salary_list.append(i.salary)
         print('Minimum salary is ', min(salary_list))
     elif choice==8:
         emp_year=input("Enter the emp ID of the person")
         for i in Emp:
             if i.emp_id==emp_year:
                 emp_join_date=i.DOJ
                 print("The employee has been working since", calculateAge(date(emp_join_date.year, emp_join_date.month, emp_join_date.day)), "years")
     elif choice==9:
         print("Thank You")
         break

    
        
             
         
             




             
         



      

         