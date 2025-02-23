# EmpProjectMain.py
from EmpDelete import empdelete
from EmpMenu import menu
from EmpSearch import searchemployee
from EmpView import viewallemployees, viewemployee
from EmpAdd import saveemprecord
from EmpUpdate import empupdate
while True:
    menu()
    try:
        ch=int(input("Enter Ur Choice:"))
        match ch:
            case 1:
                saveemprecord()
            case 2:
                viewallemployees()
            case 3:
                viewemployee()
            case 4:
                searchemployee()
            case 5:
                empupdate()
            case 6:
                empdelete()

            case 7:
                print("Thx for this Project")
                break
            case _:
                print("Ur Selection of Operation is wrong-Try again")
    except ValueError:
        print("Don't enter strs, symbols and alphanumerics for choice-try again")
