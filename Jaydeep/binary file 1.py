import pickle

def addRecord():
    f = open('teacher.dat', 'wb')
    n = int(input("Enter number of records: "))

    for i in range(n):
        a = int(input("Enter teacher's code: "))
        b = input('Enter teacher\'s name: ')
        c = int(input("Enter teacher's salary: "))

        pickle.dump([a,b,c],f)
    f.close()

def readRecord():
    f = open("teacher.dat", 'rb')
    print("Teacher records: ")

    while True:
        try:
            data = pickle.load(f)
            print(data)

        except EOFError:
            break

def searchRecord():
    f = open("teacher.dat", 'rb')
    a = int(input("Enter teacher code: "))

    while True:
        try:
            data = pickle.load(f)
            if(data[0] == a):
                print("Record found!")
                print("Teacher name:", data[1])
                print("Teacher salary:", data[2])
                break
        except EOFError:
            print("Record doesn't exist")
            break

def countRecord():
    f = open("teacher.dat", 'rb')
    c = 0
    while True:
        try:
            pickle.load(f)
            c += 1
        except EOFError:
            break

    print(c)

def updateRecord():
    a = int(input("Enter teacher code to update: "))
    while True:
        f = open("teacher.dat", "rb")
        try:
            data = pickle.load(f)
            if(data[0] == a):
                choice = int(input("Enter 1 to update name, and 2 to update salary: "))
                if(choice == 1):
                    name = input("Enter new teacher name: ")
                    data[1] = name
                elif(choice == 2):
                    salary = int(input("Enter new salary: "))
                    data[2] = salary
                else:
                    print("Invalid choice")
                
            f = open("teacher.dat", "wb")
            pickle.dump(data, f)
            f.close()

        except EOFError:
            break

        f.close()

updateRecord()
readRecord()
