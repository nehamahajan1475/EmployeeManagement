import re
def validname(name):
    l=name.split()
    if len(l) == 3:
        if l[0].isalpha() and l[1].isalpha() and l[2].isalpha():
             return True
    return False
def validmobileno(mobileno):
    if len(mobileno)==10 and mobileno.isdigit():
        return True
    else:
        return False
print(validname("neha rohidas Mahajan"))
print(validmobileno("1234567890"))

def validpan(pan):
    exp = '^[A-Z]{5}[0-9]{4}[A-Z]{1}$'
    if re.match (exp,pan):
        return True
    else:
        return False
print(validpan("GDEPM4496P"))

def validadhar(adhar):
    l = adhar.split()
    if (len(l)==3):
        if l[0].isdigit() and l[1].isdigit() and l[2].isdigit():
            return True 
    return False
print(validadhar("1234 4567 7890"))

def validsalary(salary):
    if(len(salary)==5 and salary.isdigit()):
        return True
    else:
        return False
print(validsalary("1234567"))    

def validgender(gender):
    l=['male','female','other','Female','Male','F','M',]
    if gender in l:
        return True
    else:
        return False
print(validgender("male"))

def validcity(state,city):
    sc={"maharashatra":["mumbai","pune","nashik","jalgaon"],
    "MP":["indore","ujjain"],"gujarat":["surat","ahmedabad"]}
    v=sc[state]
    if city in v:
        return True
    else:
        return False
print(validcity("MP","indore"))

def validdepartment(depart):
    l=['IT','human resources','finance','development','production']
    if depart in l:
        return True
    else:
        return False
print(validdepartment("finance"))      

def validdesignation(design):
    l=["manager","HR","director","employee"]
    if design in l:
        return True
    else:
        return False
print(validdesignation("finance"))      


from datetime import date
 
def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day)< (birthDate.month, birthDate.day))
    if age>0 or age<=100:
        return age
    else:
        return False
     
print(calculateAge(date(2001, 8, 25)), "years")







    
    
    

    







