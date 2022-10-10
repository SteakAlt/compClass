import csv

def addRecords():
    fp = open('product.csv', 'w', newline='')
    n = int(input("Enter number of records: "))
    writer = csv.writer(fp, delimiter=',')
    for i in range(n):
        productId = int(input("Enter product Id: "))
        productName = input("Enter product name: ")
        price = int(input("Enter product price: "))

        writer.writerow([productId, productName, price])

    fp.close()


def readRecords():
    fp = open('product.csv', 'r')
    data = csv.reader(fp, delimiter=',')
    for i in data:
        print(i)

def countRecords():
    fp = open('product.csv', 'r')
    data = csv.reader(fp, delimiter=',')
    c = 0
    for i in data:
        c+=1
    print("Count:", c)

def searchRecords():
    fp = open('product.csv', 'r')
    data = csv.reader(fp, delimiter=',')
    a = input("Enter product Id: ")
    for i in data:
        if(i[0] == a):
            print(i)
            break
    else:
        print("Record not found!")

while True:
    choice = int(input("""1) Add Records
2) Read Records
3) Count Records
4) Search Records
5) Exit
"""))
    if choice == 1:
        addRecords()
    elif choice == 2:
        readRecords()
    elif choice == 3:
        countRecords()
    elif choice == 4:
        searchRecords()
    elif choice == 5:
        print("Thank you")
        break
    else:
        print("Invalid choice!")
