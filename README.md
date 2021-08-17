### Run Backend

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


### Execute Queries and Mutations:

1. go to http://localhost:8000/graphql/
2. explore the "Docs" on the right (Queries, Mutations)
3. Write your first query:


### QUERIS 
#### -> GET BOOKS

GET BOOKS:
```
query getBooks {
  books {
    id
    author
    description
    url
 }
}
```

#### -> CREATE A USER & LOG IN
CREATE A NEW USER:
```
mutation {
  createUser(email: "VALID_EMAIL", password: "VALID_PASSWORD", username: "USERNAME"){
    user {
      id
      email
      username
    }
  }
}
```
example -> createUser(email: "test@gmail.com", password: "1234567890", username: "test_123")

After creating a user profile, you can login

1. GET THE AUTH TOKEN


Enter your username and password you've just provided. After executing the query copy the auth token

```
mutation {
  tokenAuth(username:"USERNAME", password: "VALID_PASSWORD") {
    token
  }
}
```

---- IMAGE ---

2. LOG IN


Enter your Auth Token in REQUEST HEADERS TAB
```
{
"Authentication": "JWT {YOUR TOKEN}"
}
```

GET INFO ABOUT THE USER YOU HAVE CREATED:
```
{
  me {
    id
    username
    email
  }
}

```

### BOOKS QUERIES AND MUTATIONS 

#### CREATE A BOOK

```
mutation {
  createBook(author:"cool author", description: "some desct", url: "9599", title: "titlre"){
    book {
      id
      title
      description
      author
      url
      createdAt
    }
  }
}
```

#### UPDATE A BOOK
TODO

#### DELETE A BOOK
TODO
#### LIKE A BOOK
TODO
#### CHECK HOW MANY LIKES ARE ON BOOKS
TODO
#### SEARCH A BOOK
TODO
