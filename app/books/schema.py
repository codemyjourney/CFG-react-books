import graphene 
from graphene_django import DjangoObjectType
from .models import Book


class BookType(DjangoObjectType):
    class Meta:
        model = Book

class Query(graphene.ObjectType):
    books = graphene.List(BookType)

    def resolve_books(self, info):
        return Book.objects.all()

class CreateBook(graphene.Mutation):
    book = graphene.Field(BookType)

    class Arguments:
        title = graphene.String()
        author = graphene.String()
        description = graphene.String()
        url = graphene.String()

    def mutate(self, info, title, author, description, url):
        user = info.context.user 

        if user.is_anonymous:
            raise Exception("Login to add a book")

        book = Book(title=title, author=author, description=description, url=url, posted_by=user)
        book.save()
        return CreateBook(book=book)

class UpdateBook(graphene.Mutation):
    book = graphene.Field(BookType)

    class Arguments:
        book_id = graphene.Int(required=True)
        title = graphene.String()
        author = graphene.String()
        description = graphene.String()
        url = graphene.String()

    def mutate(self, info, book_id, title, author, description, url):
        user = info.context.user
        book = Book.objects.get(id=book_id)
        
        if book.posted_by != user:
            raise Exception("Not permited to update")

        book.title = title
        book.description = description
        book.author = author
        book.url = url

        book.save()

        return UpdateBook(book=book)

class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()