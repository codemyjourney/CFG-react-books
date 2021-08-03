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
