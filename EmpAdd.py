#  Program for adding new employee to employee.pick
#  EmpAdd.py<----File Name and Module Name
import pickle
def saveemprecord():
    with open("employee.pick", "ab") as fp:
        while True:
            try:
                #  read the emp data from KBD
                print("----------------------------------")
                empno = int(input("Enter Employee Number:"))
                ename = input("Enter Employee Name:")
                sal = float(input("Enter Employee Salary:"))
                dsg = input("Enter Employee Designation:")
                print("----------------------------------")
                #  add employee values to Iterable object
                lst = []
                lst.append(empno)
                lst.append(ename)
                lst.append(sal)
                lst.append(dsg)
                #  Save the Iterable object data to the file
                pickle.dump(lst, fp)
                print("Employee Record Saved in a File")
                print("----------------------------------")
                ch = input("Do u want to Insert another Record(yes/no):")
                if ch.lower() == "no":
                    print("Thx for Using Program")
                    break
            except ValueError:
                print("Don't enter alphanumerics,symbols and str for employeenumber, and salary")


