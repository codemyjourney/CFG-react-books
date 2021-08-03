### Backend

```
pipenv shell
```
```
pipenv install
```
```
cd app
```
```
python manage.py runserver
```
### create data
```
cd app
python manage.py shell

from books.models import Book
Book.objects.create(title="Track 2", description="Description 2", author="Author 2", url="https://google.com")
```


### Query And Mutation examples

```
# query getBooks {
#   books {
#     id
#     author
#   }
# }

# 

# mutation {
#   createBook(author:"cool author", description: "some desct", url: "9599", title: "titlre"){
#     book {
#       id
#       title
#       description
#       author
#       url
#       createdAt
#     }
#   }
# }

# query {
#   user (id: 2) {
#     id
#     username
#     email
#   }
# }

# mutation {
#   createUser(email: "s.karlinska@gmail.com", password: "45634343", username: "s.kutyepov"){
#     user {
#       id
#       email
#       username
#     }
#   }
# }
```