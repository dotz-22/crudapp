# CRUDProject
CRUDProject is a project that uses Django REST Framework application to implements CRUD (Create, Read, Update, Delete) operations for managing `Books` and `Authors`. It includes APIs to add, retrieve, update, and delete entries.
## Project Setup
### Requirements
- Python 3.8+
- sqlparse 0.5.3
- Django 4.0+
- Django REST Framework 3.15+
### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd CRUDProject
   ```
2. Create and activate a virtual environment:
   ```bash
   to create a virtual enviroment venv run the command line

   python -m venv venv
   or
   python3 -m venv venv

   venv\Scripts\activate
   or
   venv/bin/activate ,on mac
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```
   python manage.py migrate
   ```
5. Run the server:
   ```
   python manage.py runserver
   ```
6. Access the application at:
   ```
   http://127.0.0.1:8000/
   ```
## API Endpoints
### AppOne (Books Management)

#### 1. **Retrieve a specific book**
- **URL**: `/api/appone/<id>/`
- **Method**: `GET`
- **Response Example**:
  ```json
  {
    "id": 1,
    "book_title": "philosophers stone",
    "book_author": "jk rowling	",
    "publication_date": "Dec. 22, 2024",
    "description":	"fiction"
  }
  ```

#### 2. **List all books**
- **URL**: `/api/appone/`
- **Method**: `GET`
- **Response Example**:
  ```json
  [
    {
    "id": 1,
    "book_title": "philosophers stone",
    "book_author": "jk rowling	",
    "publication_date": "Dec. 22, 2024",
    "description":	"fiction"
    },
   {
    "id": 3,
    "book_title":"prisoner of azkaban",
    "book_author":"jk rowling",
    "publication_date":"Dec. 22, 2024",	
    "description":"absolute cinema"
        }
  ]
  ```

#### 3. **Create a new book**
- **URL**: `/api/appone/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
   
    "book_title":"prisoner of azkaban",
    "book_author":"jk rowling",
    "publication_date":"Dec. 22, 2024",	
    "description":"absolute cinema"
  }
  ```
- **Response Example**:
  ```json
  {
    "id": 3,
    "book_title":"prisoner of azkaban",
    "book_author":"jk rowling",
    "publication_date":"Dec. 22, 2024",	
    "description":"absolute cinema"
  }
  ```
#### 4. **Update a book**
- **URL**: `/api/appone/<id>/`
- **Method**: `PUT`
- **Request Body**:
  ```json
  {
    "title": "Updated Book Title",
    "author": "Updated Author",
    "publication_date": "2024-02-01"
  }
  ```
- **Response Example**:
  ```json
  {
    "id": 3,
    "title": "Updated Book Title",
    "author": "Updated Author",
    "publication_date": "2024-02-01"
  }
  ```

#### 5. **Update a book**
- **URL**: `/api/appone/<id>/`
- **Method**: `PATCH`
- **Request Body**:
  ```json
  {
    "title": "re-Updated Book Title",
    "author": "re-Updated Author",
  }
  ```
- **Response Example**:
  ```json
  {
    "id": 3,
    "title": "re-Updated Book Title",
    "author": "re-Updated Author",
    "publication_date": "2024-02-01"
  }
  ```
  
#### 6. **Delete a book**
- **URL**: `/api/appone/<id>/`
- **Method**: `DELETE`
- **Response**: `204 No Content`

---------
### AppTwo (Authors Management)

#### 1. **Retrieve a specific author**
- **URL**: `/api/apptwo/<id>/`
- **Method**: `GET`
- **Response Example**:
  ```json
  {
    "id": 1,
    "name": "charles dickens",
    "bio": "fucktard",
    "date_of_birth": "2000-01-01"
  }
  ```

#### 2. **List all authors**
- **URL**: `/api/apptwo/`
- **Method**: `GET`
- **Response Example**:
  ```json
  [
    {
     "id": 1,
    "name": "charles dickens",
    "bio": "fucktard",
    "date_of_birth": "2000-01-01"
    },
    {
      "id": 2,
      "name": "ugo. c .ugo",
      "bio": "nigerian author",
      "date_of_birth": "2000-10-10"
    }
  ]
  ```

#### 3. **Create a new author**
- **URL**: `/api/apptwo/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {   
  "name": "J.K. Rowling",
  "bio": "British author, best known for the Harry Potter series.",
  "date_of_birth": "1965-07-31"
  }
  ```
- **Response Example**:
  ```json
  {
  "id": 3,
  "name": "J.K. Rowling",
  "bio": "British author, best known for the Harry Potter series.",
  "date_of_birth": "1965-07-31"
  }
  ```
#### 4. **Update an author**
- **URL**: `/api/apptwo/<id>/`
- **Method**: `PUT`
- **Request Body**:
  ```json
  {
    "name": "Updated Author Name",
    "bio": "Updated biography.",
    "date_of_birth": "1921-01-03"
  }
  ```
- **Response Example**:
  ```json
  {
    "id": 3,
    "name": "Updated Author Name",
    "bio": "Updated biography.",
    "date_of_birth": "1921-01-03"
  }
  ```
  #### 5. **Update an author**
- **URL**: `/api/apptwo/<id>/`
- **Method**: `PATCH`
- **Request Body**:
  ```json
  {
    "name": "re=Updated Author Name",
    
    "date_of_birth": "1925-11-03"
  }
  ```
- **Response Example**:
  ```json
  {
    "id": 3,
    "name": "re-Updated Author Name",
    "bio": "Updated biography.",
    "date_of_birth": "1925-11-03"
  }
  ```
#### 6. **Delete an author**
- **URL**: `/api/apptwo/<id>/`
- **Method**: `DELETE`
- **Response**: `204 No Content`
---
- Tested the APIs using Postman
---