# EmpDelete.py<---File Name
import pickle
def empdelete():
    try:
        with open("employee.pick", "rb") as fp:
            allemprec = []
            while True:
                try:
                    record = pickle.load(fp)
                    allemprec.append(record)

                except EOFError:
                    break
            deletion = False
            empno = int(input("Enter Emp Number to delete from File:"))
            for i in range(len(allemprec)):
                if empno == allemprec[i][0]:
                    allemprec.pop(i)
                    deletion = True
                    break
            if deletion:
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


