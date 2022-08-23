import mysql.connector as c

db = c.connect(user= 'root', password = '00b', host = 'localhost', database = 'jay')
cs = db.cursor()

while True:
    print("""MENU
          1. Display shop table
          2. Insert new record
          3. Display one row  using fetchone function
          4. Display n rows using fetchmany function and display the row count
          5. Exit the program""")
    ch = int(input("Enter choice 1/2/3/4/5: "))
    if ch == 1:
        cs.execute("select * from shop")
        data = cs.fetchall()
        for i in data:
            print(i)
            
    if ch == 2:
        itemId = int(input("Enter id: "))
        itemName = input("Enter item name: ")
        price = int(input("Enter price: "))
        cs.execute(f'insert into shop values({itemId}, "{itemName}", {price})')
        db.commit()
        print("New record is added!")
    
    if ch == 3:
        cs.execute('Select * from shop')
        data = cs.fetchone()
        print(data)
        
    if ch == 4:
        cs.execute('select * from shop')
        data = cs.fetchmany(2)
        rc = cs.rowcount
        for i in data:
            print(i)
        print('Rowcount: ', rc)
            
    if ch == 5:
        break
    
