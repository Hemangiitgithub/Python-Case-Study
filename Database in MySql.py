import mysql.connector
import tabulate
from datetime import date


def displayAll():
    cur.execute("SELECT *FROM COMP_STUD")
    res=cur.fetchall()
    print(tabulate.tabulate(res,headers=["PRN","FRIST_NAME","MIDDLE_NAME","LAST_NAME","ADDRESS","MOBILE","EMAIL","DOB"]))

def dispNameAge():
    cur.execute("SELECT FRIST_NAME,MIDDLE_NAME,LAST_NAME,DOB FROM COMP_STUD")
    res=cur.fetchall()
    todaysdate = date.today()
    li=[]
    for i in res:
        age = todaysdate - i[-1]
        li.append((i[0]+" "+i[1]+" "+i[2],age.days//365))
    print(tabulate.tabulate(li,headers=["name","age"]))

def NewRecordAdd():
    print(".....Adding new record....")
    PRN=input("Enter prn.no : ")
    FRIST_NAME=input("Enter FRIST_NAME :").upper()
    MIDDLE_NAME=input("MIDDLE_NAME :").upper()
    LAST_NAME=input("LAST_NAME :").upper()
    ADDRESS=input("ADDRESS :").upper()
    MOBILE=input("MOBLE NUMBER : ").upper()
    EMAIL=input("EMAIL :").lower()
    DOB=input("DOB :")
    cur.execute("INSERT INTO COMP_STUD VALUES('{}','{}','{}','{}','{}','{}','{}','{}')".format(PRN,FRIST_NAME,MIDDLE_NAME,LAST_NAME,ADDRESS,MOBILE,EMAIL,DOB))
    mycon.commit()
    print("Record added successfully")

def DeleteRecord():
    PRN=input("Enter the PRN whose record is to be deleted: ")
    QUERY="Delete from Comp_stud where PRN='{}'".format(PRN)
    cur.execute(QUERY)
    mycon.commit()
    print("Record deleted successfully")

def UpdatePhoneEmail():
    PRN = input("Enter the PRN whose record is to be deleted: ")
    MOB = input("Enter new mobile number: ")
    EMAIL = input("Enter new email id: ")
    QUERY = "UPDATE COMP_STUD SET MOBILE='{}',EMAIL='{}' WHERE PRN='{}'".format(MOB, EMAIL, PRN)
    cur.execute(QUERY)
    mycon.commit()
    print("Database updated Successfully")

def AddCGPA(flag):
    if flag:
        query = "ALTER TABLE COMP_STUD ADD COLUMN CGPA FLOAT"
        cur.execute(query)
        mycon.commit()
        print("\n CGPA field added successfully...\n")
        cur.execute("SELECT PRN FROM COMP_STUD")
        x = cur.fetchall()
        for i in x:
            prn = i[0]
            print("Enter the CGPA of PRN ", prn, end=': ')
            cgpa = float(input())
            query = "UPDATE COMP_STUD SET CGPA='{}' WHERE PRN='{}'".format(cgpa, prn)
            cur.execute(query)
            mycon.commit()
        return False
    else:
        print("The field CGPA already exists.")
        return True

def functions():
    print('''
            1. Display the database
            2. Display name and age of all students
            3. Add record 
            4. Delete a record
            5. Update email and Phone number
            6. Add column CGPA
            Enter any other key to exit
    ''')

if __name__ == "__main__":
    print("Welcome to DBATU Second year Computer Engineering Department")
    print("--" * 30)
    mycon = mysql.connector.connect(host="localhost", user="root", password="Hemangi", database="comp_stud")
    cur = mycon.cursor()
    global flag
    flag = False
    try:
        cur.execute("ALTER TABLE COMP_STUD DROP COLUMN CGPA")
    except:
        pass
    flag = True
    if mycon.is_connected():
        functions()
        while True:
            opt = input("Select your choice(h for help): ")
            if opt == '1':
                displayAll()
            elif opt == '2':
                dispNameAge()
            elif opt == '3':
                NewRecordAdd()
            elif opt == '4':
                DeleteRecord()
            elif opt == '5':
                UpdatePhoneEmail()
            elif opt == '6':
                flag = AddCGPA(flag)
            elif opt in 'hH':
                functions()
            else:
                break
    else:
        print("Unable to connect to MySQL")


