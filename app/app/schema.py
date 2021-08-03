import graphene 
import users.schema
import books.schema

class Query(users.schema.Query,books.schema.Query, graphene.ObjectType):
    pass

class Mutation(users.schema.Mutation, books.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)