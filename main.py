from fastapi import FastAPI
from fastapi import Body
app=FastAPI()  

books = [{"book number":"book1","title": "The Catcher in the Rye", "author": "J.D. Salinger", "category": "Fiction"},
         {"book number":"book2","title": "Sapiens: A Brief History of Humankind", "author": "Yuval Noah Harari", "category": "Non-Fiction"},
         {"book number":"book3","title": "To Kill a Mockingbird", "author": "Harper Lee", "category": "Fiction"},
         {"book number":"book4","title": "random_book1", "author": "George Orwell", "category": "maths"},
          ]


@app.get("/books/read_all_books")
async def first_api():
    return books


#Path parameters
@app.get("/books/my_book")                  
async def read_book():
    return {'my book':'my favourite book'}

@app.get("/books/{book_number}")                  #Here the order does matters. If we keep this function above the 
async def read_book(book_number:str):             #/books/my_book then even after calling '/books/my_book' it will  
    for book in books:                            #run the get method with {dynamic_param}.
        if book.get("book number").casefold()==book_number.casefold():
            return book
        else:
            return "Please enter the valid book number"

#Query parameters
@app.get("/books/")
async def read_category_by_query(category:str):
    books_to_return=[]
    for book in books:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


#Combination of both Path and Query parameters
@app.get("/books/{author}/")
async def read_author_category_by_query(author:str,category:str):
    books_to_return=[]
    for book in books:
        if book.get('author').casefold()==author.casefold() and book.get('category').casefold()==category.casefold():
            books_to_return.append(book)
    return books_to_return

#Post Method is used to create the data. For post method we need to import 'Body'.
@app.post('/books/create_book/')
async def create_book(new_book=Body()):
    books.append(new_book)

#Put method is used to update the data. 
@app.put('/books/update_book/')
async def update_book(updated_book=Body()):
    for i in range (len(books)):
        if books[i].get('title').casefold()==updated_book.get('title').casefold():
            books[i]=updated_book

#Delete method is used to update the data.
@app.delete('/books/delete_book/{book_title}')
async def delete_book(book_title:str):
    for i in range (len(books)):
        if books[i].get('title').casefold()==book_title.casefold():
            del books[i]
            break

