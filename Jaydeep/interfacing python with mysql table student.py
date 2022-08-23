import mysql.connector as sql

conn = sql.connect(user = 'root', password = '00b', host = 'localhost')
cs = conn.cursor()

cs.execute("create database if not exists school")
cs.execute("use school")
cs.execute("create table if not exists student(rollno int primary key, name varchar(20), class int, marks int)")

while True:
    print('''
            MENU
            1. Add student details
            2. Update student details
            3. Delete student details
            4. View student details
            5. Exit
            ''')
    choice = int(input("Enter choice 1/2/3/4/5: "))
    if choice==1:
        r = int(input("Enter rollno: "))
        n = input("Enter name: ")
        cl = int(input("Enter class: "))
        m = int(input("Enter marks: "))
        cs.execute("insert into student values(%s, '%s',%s,%s)" %(r,n,cl,m))
        conn.commit()
        
    elif(choice == 2):
        rno = int(input("Enter rollno for mark updation: "))
        m = int(input("Enter new marks: "))
        cs.execute("Update student set marks = %s where rollno=%s"%(m, rno))
        conn.commit()
        print("Details updated")
        
    elif(choice == 3):
        rno = int(input("Enter rollno for deletion: "))
        cs.execute('delete from student rollno = %s'%(rno))
        conn.commit()
        print("Details removed")
    elif(choice == 4):
        cs.execute('select * from student')
        r = cs.fetchall()
        for i in r:
            for j in i:
                print(j, end = "\t")
            print()
    else:
        break
