from fastapi import Body,FastAPI

app=FastAPI()

BOOKS=[
    {"title":"Title One" , "author":"Author One", "category":"science"},
    {"title":"Title Two" , "author":"Author Two", "category":"science"},
    {"title":"Title Three" , "author":"Author Three", "category":"history"},
    {"title":"Title Four" , "author":"Author Four", "category":"math"},
    {"title":"Title Five" , "author":"Author Five", "category":"math"},
]


@app.get("/books")
async def read_all_books():
    return BOOKS

# @app.get("/books/mybook")
# async def read_all_books():
#     return {"book_title":"My favorite book !"}

@app.get("/books/{book_title}") 
async def read_books(book_title : str): # Otomatik olarak int değeri girilirse str ye çevirir.
    for book in BOOKS:
        if book.get("title").casefold()==book_title.casefold():
            return book

@app.get("/books/")
async def read_books_by_category(category:str):
    book_return=[]
    for book in BOOKS:
        if book.get("category").casefold()==category.casefold():
            book_return.append(book)
    return book_return


@app.get("/books/{book_author}/")
async def read_books_author_category(book_author:str,category:str):
    book_return=[]
    for book in BOOKS:
        if book.get("author").casefold()==book_author.casefold() and book.get("category").casefold()==category.casefold():
            book_return.append(book)
    return book_return

@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put("/books/update_book")
async def update_book(update_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold()==update_book.get("title").casefold():
            BOOKS[i]=update_book


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title :str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold()==book_title.casefold():
            BOOKS.pop(i)
            break

# @app.get("/books/{dynamic_param}")
# async def read_all_books(dynamic_param : str): # Otomatik olarak int değeri girilirse str ye çevirir.
#     return {"dynamic_param":dynamic_param}




