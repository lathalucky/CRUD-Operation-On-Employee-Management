# Code Viewing all employee OR Single Employee
# EmpView.py<---File Name and Module Name
import pickle


def viewallemployees():
    try:
        with open("employee.pick", "rb") as fp:
            print("------------------------------")
            print("\tEmployee Details")
            print("------------------------------")
            while True:
                try:
                    record = pickle.load(fp)
                    for val in record:  # To display Record Values
                        print("{}".format(val), end="\t\t")
                    print()
                except EOFError:
                    print("------------------------------")
                    break
    except FileNotFoundError:
        print("File Does not Exist")


def viewemployee():
    try:
        with open("employee.pick", "rb") as fp:
            empno = int(input("Enter Employee Number to view Deatils:"))
            found = False
            while True:
                try:
                    record = pickle.load(fp)
                    if empno == record[0]:
                        found = True
                        emprec = record
                        break
                except EOFError:
                    break
            if found:
                print("=" * 40)
                print("Employee Deatils")
                print("=" * 40)
                print("\tEmployee Number={}".format(record[0]))
                print("\tEmployee Name={}".format(record[1]))
                print("\tEmployee Salary={}".format(record[2]))
                print("\tEmployee Designation={}".format(record[3]))
                print("=" * 40)
            else:
                print("Employee Record Does not Exist")
    except FileNotFoundError:
        print("Employee File Does not Exist:")


