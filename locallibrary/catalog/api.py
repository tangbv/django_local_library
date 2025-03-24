from ninja import NinjaAPI, ModelSchema
from django.shortcuts import get_object_or_404
from typing import List
from .models import Author, Genre, Language, Book, BookInstance
from ninja.security import HttpBearer




class GlobalAuth(HttpBearer):
   def authenticate(self, request, token):
       print(f"Token received: {token}")  # Debugging line
       if token == "supersecret":
           return token
       return None  # This should return None if the token is invalid

api = NinjaAPI(auth=GlobalAuth())

# ---------------------
# SCHEMAS
# ---------------------
class AuthorSchema(ModelSchema):
   class Config:
       model = Author
       model_fields = "__all__"

class GenreSchema(ModelSchema):
   class Config:
       model = Genre
       model_fields = "__all__"

class LanguageSchema(ModelSchema):
   class Config:
       model = Language
       model_fields = "__all__"

class BookSchema(ModelSchema):
   class Config:
       model = Book
       model_fields = "__all__"

class BookInstanceSchema(ModelSchema):
   class Config:
       model = BookInstance
       model_fields = "__all__"

# ---------------------
# AUTHOR ENDPOINTS
# ---------------------
@api.get("/authors", response=List[AuthorSchema], auth=None)
def list_authors(request):
   return list(Author.objects.all())

@api.get("/authors/{author_id}", response=AuthorSchema, auth=None)
def get_author(request, author_id: int):
   return get_object_or_404(Author, id=author_id)

@api.post("/authors", response=AuthorSchema)
def create_author(request, author: AuthorSchema):
   return Author.objects.create(**author.dict())

@api.put("/authors/{author_id}", response=AuthorSchema)
def update_author(request, author_id: int, author: AuthorSchema):
   author_obj = get_object_or_404(Author, id=author_id)
   for attr, value in author.dict().items():
       setattr(author_obj, attr, value)
   author_obj.save()
   return author_obj

@api.delete("/authors/{author_id}")
def delete_author(request, author_id: int):
   author_obj = get_object_or_404(Author, id=author_id)
   author_obj.delete()
   return {"success": True}

# ---------------------
# GENRE ENDPOINTS
# ---------------------
@api.get("/genres", response=List[GenreSchema], auth=None)
def list_genres(request):
   return list(Genre.objects.all())

@api.get("/genres/{genre_id}", response=GenreSchema, auth=None)
def get_genre(request, genre_id: int):
   return get_object_or_404(Genre, id=genre_id)

@api.post("/genres", response=GenreSchema)
def create_genre(request, genre: GenreSchema):
   return Genre.objects.create(**genre.dict())

@api.put("/genres/{genre_id}", response=GenreSchema)
def update_genre(request, genre_id: int, genre: GenreSchema):
   genre_obj = get_object_or_404(Genre, id=genre_id)
   for attr, value in genre.dict().items():
       setattr(genre_obj, attr, value)
   genre_obj.save()
   return genre_obj

@api.delete("/genres/{genre_id}")
def delete_genre(request, genre_id: int):
   genre_obj = get_object_or_404(Genre, id=genre_id)
   genre_obj.delete()
   return {"success": True}

# ---------------------
# LANGUAGE ENDPOINTS
# ---------------------
@api.get("/languages", response=List[LanguageSchema], auth=None)
def list_languages(request):
   return list(Language.objects.all())

@api.get("/languages/{language_id}", response=LanguageSchema, auth=None)
def get_language(request, language_id: int):
   return get_object_or_404(Language, id=language_id)

@api.post("/languages", response=LanguageSchema)
def create_language(request, language: LanguageSchema):
   return Language.objects.create(**language.dict())

@api.put("/languages/{language_id}", response=LanguageSchema)
def update_language(request, language_id: int, language: LanguageSchema):
   language_obj = get_object_or_404(Language, id=language_id)
   for attr, value in language.dict().items():
       setattr(language_obj, attr, value)
   language_obj.save()
   return language_obj

@api.delete("/languages/{language_id}")
def delete_language(request, language_id: int):
   language_obj = get_object_or_404(Language, id=language_id)
   language_obj.delete()
   return {"success": True}

# ---------------------
# BOOK ENDPOINTS
# ---------------------

@api.get("/books", response=List[BookSchema], auth=None)
def list_books(request):
   return list(Book.objects.all())

@api.get("/books/{book_id}", response=BookSchema, auth=None)
def get_book(request, book_id: int):
   return get_object_or_404(Book, id=book_id)

@api.post("/books", response=BookSchema)
def create_book(request, book: BookSchema):
   return Book.objects.create(**book.dict())

@api.put("/books/{book_id}", response=BookSchema)
def update_book(request, book_id: int, book: BookSchema):
   book_obj = get_object_or_404(Book, id=book_id)
   for attr, value in book.dict().items():
       setattr(book_obj, attr, value)
   book_obj.save()
   return book_obj

@api.delete("/books/{book_id}")
def delete_book(request, book_id: int):
   book_obj = get_object_or_404(Book, id=book_id)
   book_obj.delete()
   return {"success": True}

# ---------------------
# BOOKINSTANCE ENDPOINTS
# ---------------------
@api.get("/bookinstances", response=List[BookInstanceSchema], auth=None)
def list_book_instances(request):
   return list(BookInstance.objects.all())

@api.get("/bookinstances/{instance_id}", response=BookInstanceSchema, auth=None)
def get_book_instance(request, instance_id: str):
   return get_object_or_404(BookInstance, id=instance_id)

@api.post("/bookinstances", response=BookInstanceSchema)
def create_book_instance(request, instance: BookInstanceSchema):
   return BookInstance.objects.create(**instance.dict())

@api.put("/bookinstances/{instance_id}", response=BookInstanceSchema)
def update_book_instance(request, instance_id: str, instance: BookInstanceSchema):
   instance_obj = get_object_or_404(BookInstance, id=instance_id)
   for attr, value in instance.dict().items():
       setattr(instance_obj, attr, value)
   instance_obj.save()
   return instance_obj

@api.delete("/bookinstances/{instance_id}")
def delete_book_instance(request, instance_id: str):
   instance_obj = get_object_or_404(BookInstance, id=instance_id)
   instance_obj.delete()
   return {"success": True}
