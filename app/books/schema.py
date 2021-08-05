import graphene 
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from django.db.models import Q
from .models import Book, Like
from users.schema import UserType


class BookType(DjangoObjectType):
    class Meta:
        model = Book

class LikeType(DjangoObjectType):
    class Meta:
        model = Like


class Query(graphene.ObjectType):
    books = graphene.List(BookType, search=graphene.String())
    likes = graphene.List(LikeType)

    def resolve_books(self, info, search=None):
        if search: 
            filter = (
                Q(title__icontains=search) |
                Q(description__icontains=search) |
                Q(url__icontains=search) |
                Q(posted_by__username__icontains=search)
            )
            return Book.objects.filter(filter)

        return Book.objects.all()
    def resolve_likes(self, info):
        return Like.objects.all()


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
            raise GraphQLError("Login to add a book")

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
            raise GraphQLError("Not permited to update")

        book.title = title
        book.description = description
        book.author = author
        book.url = url

        book.save()

        return UpdateBook(book=book)


class DeleteBook(graphene.Mutation):
    book_id = graphene.Int()

    class Arguments:
        book_id = graphene.Int(required=True)

    def mutate(self, info, book_id):
        user = info.context.user
        book = Book.objects.get(id=book_id)

        if book.posted_by != user:
            raise GraphQLError("Not permited to delete this book")

        book.delete()

        return DeleteBook(book_id=book_id)


class CreateLike(graphene.Mutation):
    user = graphene.Field(UserType)
    book = graphene.Field(BookType)

    class Arguments:
        book_id = graphene.Int(required=True)

    def mutate(self, info, book_id):
        user = info.context.user

        if user.is_anonymous:
            raise GraphQLError("Login first")

        book = Book.objects.get(id=book_id)
        if not book:
            raise GraphQLError('Cannot find a book with id {}'.format(book_id))

        Like.objects.create(
            user=user,
            book=book
        )

        return CreateLike(user=user, book=book)

class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()
    delete_book = DeleteBook.Field()
    create_like = CreateLike.Field()