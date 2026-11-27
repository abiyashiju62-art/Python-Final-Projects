import sqlite3

#connects to the library database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

#function to create the required database tables
def create_tables():

 #create the book details table
 cursor.execute('''create table if not exists book_details(
                BOOK_ID integer primary key,
                TITLE text,
                AUTHOR text,
                QUANTITY integer,
                PRICE real,
                VOLUME_NUMBER integer,
                CATEGORY text,
                PUBLISHER text,
                ISBN text
                )
                
                ''')


 #create the user details table
 cursor.execute('''create table if not exists user_details(
                USER_ID integer primary key,
                USER_NAME text,
                PASSWORD text,
                ROLE text
                )
                
                ''')
 
 #create the borrowing details table
 cursor.execute('''create table if not exists borrow_details(
                BORROW_ID integer primary key,
                USER_ID integer,
                USER_NAME text,
                BOOK_ID integer,
                BOOK_TITLE text,
                BORROW_DATE text,
                RETURN_DATE text,
                STATUS text
                )
                
                ''')
 #save the changes and close the databse connection
 conn.commit()
 conn.close()

