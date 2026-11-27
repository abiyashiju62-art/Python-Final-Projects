#import required modules
import sqlite3
from datetime import date

#import database table creation function
from database import create_tables

#establish database connection
try:
 conn = sqlite3.connect("library.db")
 cursor = conn.cursor()
except sqlite3.Error as e:
  print("Database error:" ,e)
  raise SystemExit

#function to register a new user
def register():
    
    #get a valid username
    while True:
     user = input("Enter your username:").strip()
     if user:
       break
     else:
       print("User can't be empty")

    #get a valid password
    while True:
     password = input("Enter password:").strip()
     if password:
       break
     else:
       print("Password can't be empty")

    #check whether the username already exists
    cursor.execute(''' 
                   SELECT * FROM user_details WHERE USER_NAME = ?  
                   ''',(user,))
    result = cursor.fetchone()

    #register the user if the username is available
    if result is None:
     cursor.execute('''insert into user_details(USER_NAME,PASSWORD,ROLE)
                     values(?,?,?)
                     ''',(user,password,"user"))
     conn.commit()
     print("Registration successful")
    else:
     print("Username already exists")


#function to authenticate a user
def login():

   #get a valid username
   while True:
    print("-" * 40)
    user = input("Enter your username:").strip()
    if user:
      break
    else:
      print("User can't be empty")

   #get a valid password
   while True:
    password = input("Enter your password:").strip()
    if password:
      break
    else:
      print("Password can't be empty")

  #verify the username and password
   cursor.execute(''' 
                  SELECT * FROM user_details WHERE USER_NAME = ? AND Password = ?
                 ''',(user,password))
   result = cursor.fetchone()
   print("-" * 40)

   #check login credentials
   if result is None:
      print("Invaild username or password")
   else:
      print("Login is successful".center(40))

      #identify the user's role
      role = result[3] 

      #display a welcome message based on the role
      if role == "admin":
        print("welcome, Admin!".center(40))
      else:
       print("Welcome, User!".center(40)) 
      return role,user 

#function to create a default admin account
def create_admin():

  #check whether an admin account already exists
  cursor.execute('''
                  SELECT * FROM user_details  WHERE USER_Name = ?
                 ''',("admin",))
  result = cursor.fetchone()
  if result is None:

    #Create the admin account if it does not exist
    cursor.execute('''
                    insert into user_details (USER_NAME, PASSWORD, ROLE)
                    VALUES (?, ?, ?)
                    ''', ("admin", "admin123", "admin"))
    conn.commit()
    print("-" * 40)
    print("Admin account created successfully")


#function to add a new book
def add_book():
    #get a valid book title
    while True:
      title = input("Enter the title of the book: ").strip()
      if title:
        break
      else:
        print("-" * 40)
        print("Title can't be empty")

    #get a valid author name
    while True:
     author = input("Enter the author name: ").strip()
     if author:
       break
     else:
       print("-" * 40)
       print("Author can't be empty")

    #validate the available book quantity
    while True:
     try:
      quantity = int(input("Enter the number of books available:" ))
      if quantity > 0:
        break
      else:
       print("-" * 40)
       print("Enter a positive value")
     except ValueError:
      print("-" * 40)
      print("Quantity must be a whole number")
      continue

    #validate the book price
    while True:
     try:
      price = float(input("Enter the price of the book:" )) 
      if price > 0:
        break
      else:
        print("-" * 40)
        print("Enter a positive value")
     except ValueError:
      print("-" * 40)
      print("Price must be a numerical value")
      continue  
     
    #insert the book details into the database
    cursor.execute('''insert into book_details(TITLE,AUTHOR,QUANTITY,PRICE)
                      values(?,?,?,?)
                      ''',(title,author,quantity,price))
    conn.commit()

    #display success message
    print("-" * 40)
    print("Book added successfully".center(40))


#function to display all aviable books
def view_books():

  #retrive all books records from database
  cursor.execute(''' 
                 SELECT * FROM book_details  
                ''')
  books = cursor.fetchall()

  #check whether any book are available
  if not books:
    print("-" * 40)
    print("No books available")
  else:
    for book in books:
     print("-" * 40) 

     #display the details of each book 
     print("BOOK_ID: ",book[0],
           "\nTITLE: ",book[1],
           "\nAUTHOR: ",book[2],
           "\nQUANTITY: ",book[3],
           "\nPRICE: ",book[4] ) 


#function to search for a book using its ID
def search_book():

  #validate the book id
  while True:
    try:
     book_id = int(input("Enter the BOOK_ID:"))
     if book_id >0:
       break
     else:
       print("-" * 40)
       print("Enter a positive value")
    except ValueError:
      print("-" * 40)
      print("Book_ID must be a whole number")
      continue

  #search for the book in the database
  cursor.execute(''' 
                   SELECT * FROM book_details where BOOK_ID=?  
                  ''',(book_id,))
  book = cursor.fetchone()

  #display the book details if found
  if book is None:
    print("-" * 40)
    print("Book not found")
  else:
    print("-" * 40)
    print("BOOK_ID: ",book[0],
               "\nTITLE: ",book[1],
               "\nAUTHOR: ",book[2],
               "\nQUANTITY: ",book[3],
               "\nPRICE: ",book[4] ) 


#function to update book details
def update_book():

  #validate the book id
  while True:
   try: 
    book_id = int(input("Enter the Book_ID: "))
    if book_id > 0:
     break
    else:
     print("-" * 40)
     print("Enter a positive value")
   except ValueError:
    print("-" * 40)
    print("Book_ID must be a whole number")
    continue

  #check whether the book exists
  cursor.execute(''' 
                  SELECT * FROM book_details where BOOK_ID=?  
                  ''',(book_id,))
  book = cursor.fetchone()
  if book is None:
    print("-" * 40)
    print("Book not found")
  else:

    #validate the updated book quantity
    while True:
     try:
      quantity = int(input("Enter the number of avaiable books: "))
      if quantity >=0:
         break
      else:
        print("-" * 40)
        print("Enter a positive value")
     except ValueError:
       print("-" * 40)
       print("Quantity must be a whole value")
       continue

    #validate the updated book price
    while True:
     try:
      price = float(input("Enter the price of the book: "))
      if price > 0:
        break
      else:
        print("-" * 40)
        print("Enter zero or a positive number")
     except ValueError:
       print("-" * 40)
       print("Price must be a numerical value")

    #update the book details in the database
    cursor.execute(''' 
                   update book_details set QUANTITY=? , PRICE = ? where book_id =? 
                  ''',(quantity,price,book_id,))
    conn.commit()

    #display the success message
    print("-" * 40)
    print("Book updated successfully".center(40))


#function to delete a book from the databse
def delete_book():

  #validate the book id
  while True:
    try:
     book_id = int(input("Enter the Book_ID of the book you want to delete:" ))
     if book_id > 0:
       break
     else:
       print("-" * 40)
       print("Enter a positive value")
    except ValueError:
      print("-" * 40)
      print("Book_ID must be a whole number")
      continue

  #Check whether the book exists
  cursor.execute(''' 
                       SELECT * FROM book_details where BOOK_ID=?  
                      ''',(book_id,))
  book = cursor.fetchone()

  #delete the book if it exists
  if book is None:
    print("-" * 40)
    print("Book not found")
  else:
    cursor.execute(''' 
                   Delete from book_details where book_id =? 
                  ''',(book_id,))
    conn.commit()

    #display success message
    print("-" * 40)
    print("Book deleted successfully".center(40))



#function to borrow a book for a registered user
def borrow_books(username):

  #validate the book id
  while True:
    try:
     book_id = int(input("Enter the Book_ID :" ))
     if book_id >0:
       break
     else:
       print("Enter a positive number")
    except ValueError:
      print("Book_ID must be a whole number")
      continue
 
  #retrive the selected book fro the database
  cursor.execute(''' 
                  SELECT * FROM book_details where BOOK_ID=?  
                  ''',(book_id,))
  book = cursor.fetchone()

  #check whether the book is available
  if book is None:
    print("-" * 40)
    print("Book is not found")
  else:
    if book[3]>0:
      print("-" * 40)
      print("Available to Borrow")

      #retrieve the user's details
      cursor.execute(''' 
                     SELECT * FROM user_details where USER_NAME=?  
                     ''',(username,))
      user = cursor.fetchone()

      #get the current date
      today =date.today().isoformat()

      #store the borrowing record in the database
      cursor.execute('''
                        insert into borrow_details (USER_ID,USER_NAME,BOOK_ID,BOOK_TITLE,BORROW_DATE,RETURN_DATE,STATUS)
                        VALUES (?,?,?,?,?,?,?)
                        ''', (user[0],username,book_id,book[1],today,None,"Borrowed"))

      #get the generated borrow id
      borrow_id = cursor.lastrowid

      #reduce the avaiable book quantity by one
      cursor.execute(''' 
                      update book_details set QUANTITY=?  where BOOK_ID =?
      
                      ''',(book[3]-1,book_id,))

      #save  the changes to the database
      conn.commit()

      #display borrowing confirmation
      print("-" * 40)
      print("Book borrowed successfully".center(40))
      print(f"Your Borrowing ID:{borrow_id}".center(40))
    else:
      print("-" * 40)
      print("Not Available")
    


#function to return a borrowed book
def return_books(username):

  #validate the borrow id
  while True:
    try:
     borrow_id = int(input("Enter your Borrow_ID : "))
     if borrow_id > 0:
       break
     else:
       print("-" * 40)
       print("Enter a positive value")
    except ValueError:
      print("-" * 40)
      print("Borrow_ID must be a whole number")
      continue

  #find the borrowing record for the logged-in user
  cursor.execute(''' 
                  SELECT * FROM borrow_details where USER_NAME=? and BORROW_ID =? and STATUS =?
                  ''',(username,borrow_id,"Borrowed",))
  borrow = cursor.fetchone()

  #check whether a valid borrowing exists
  if borrow is None:
    print("-" * 40)
    print("Borrowing record not found")
  else:

    #get the current return datae
    today = date.today().isoformat()

    #update the borrowing record as returned 
    cursor.execute(''' 
                   update borrow_details set STATUS =? ,RETURN_DATE =? where BORROW_ID =?
                   ''',("Returned", today,borrow_id,))

    #increase the available book quantity
    cursor.execute(''' 
                    update book_details set QUANTITY=QUANTITY +1  where BOOK_ID =?
                    ''',(borrow[3],))

    #save the changes to the database
    conn.commit()

    #display return confirmation
    print("-" * 40)
    print("Book returned successfully".center(40))


#function to display the admin menu
def admin_menu():
  choice = 0

  #continue display the menu until the admin logs out
  while choice !=6:
   print("-" * 40)
   print("1.Add Book")
   print("2.View Books")
   print("3.Search Book")
   print("4.Update Book")
   print("5.Delete Book")
   print("6.Logout")

   #get and validate the admin's menu choice
   try:
    print("-" * 40)
    choice = int(input("Enter your choice: "))
   except ValueError:
     print("Enter a value from the above choices")
     continue

   #perform the selected admin operation
   if choice == 1:
    add_book()
   elif choice == 2:
    view_books()
   elif choice == 3:
    search_book()
   elif choice == 4:
    update_book()
   elif choice == 5:
    delete_book() 
   elif choice == 6:
     print("-" * 40)
     print("You have been logged out successfully")
   else:
     print("-" * 40)
     print("Invalid choice")


#function to display the user menu
def user_menu(username):
  choice = 0

  #continue display the menu until the user logs out
  while choice !=5:
   print("-" * 40)
   print("1.View Books")
   print("2.Search Books")
   print("3.Borrow Books")
   print("4.Return Books")
   print("5.Logout")

   #get and validate the user's menu choice
   try:
    print("-" * 40)
    choice = int(input("Enter your choice:" ))
   except ValueError:
     print("-" * 40)
     print("Enter a value from the above choices")
     continue

   #perform the selected user operation
   if choice == 1:
    view_books()
   elif choice == 2:
    search_book()
   elif choice == 3:
    borrow_books(username)
   elif choice == 4:
    return_books(username)
   elif choice == 5:
    print("-" * 40)
    print("You have been logged out successfully") 
   else:
    print("-" * 40)
    print("Invalid choice")

#function to display the main menu
def main_menu():

  #display the welcome screen
  print("=" * 40)
  print("LIBRARY MANAGEMENT SYSTEM".center(40))
  print("=" * 40)
  print("Welcome!".center(40))
  print()
  print("Your gateway to knowledge and reading".center(40))
  
  choice = 0

  #continue display the menu until user choose to exit
  while choice != 3:
   print("=" * 40)
   print("1.Register")
   print("2.Login")
   print("3.Exit")
   print("-" * 40)

   #get and validate the user's menu choice
   try:
    choice = int(input("Choose an option: "))
   except ValueError:
     print(" Enter a value from the above choices")
     continue

   #perform the selected operations
   if choice == 1:
    register()
   elif choice == 2:
    result = login()
    if result is not None :
      role, username = result
      if role =="admin":
       admin_menu()
      elif role == "user":
       user_menu(username)
      else:
       pass
   elif choice == 3:
    print("=" * 40)
    print("Thank you for using our LMS".center(40))
    print("=" * 40)
   else:
    print("-" * 40)
    print("Invaild choice")

#execute the main program
try:
 create_tables()
 create_admin()
 main_menu()
except sqlite3.Error as e :
  print("Database error:",e)
finally:
  conn.close()

