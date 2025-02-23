#  EmpUpdate.py<----File Name and Module Name
import pickle
def empupdate():
    try:
        with open("employee.pick", "rb") as fp:
            allemprec = []
            while True:
                try:
                    record = pickle.load(fp)
                    allemprec.append(record)
                except EOFError:
                    break
            updation = False
            empno = int(input("Enter Emp Number to update Emp Sal and Desg:"))
            for i in range(len(allemprec)):
                if empno == allemprec[i][0]:
                    allemprec[i][2] = float(input("Enter New Emp Sal:"))
                    allemprec[i][3] = input("Enter New Emp Designation:")
                    updation = True
                    break
            if updation:
                updateFile(allemprec)
            else:
                print("Emp Number does not Exist")
    except FileNotFoundError:
        print("Employee File Does not Exist:")


def updateFile(allemprec):
    with open("employee.pick", "wb") as fp:
        for record in allemprec:
            pickle.dump(record, fp)
        else:
            print("Employee Details are updated--verify")
