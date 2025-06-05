Food Recipe API
A Django REST Framework-powered API that allows users to sign up, upload recipes, like recipes, and comment on them.

Features
✅ Basic Authentication for user access
✅ Endpoints for creating, retrieving & deleting recipes
✅ Making Categories for recipes
✅ Like functionality for recipes
✅ Commenting system for recipe discussions

Tech Stack
- Backend: Django REST Framework
- Authentication: Basic Authentication
- Database: SQLite

API Endpoints
| Method | Endpoint | Description | Authorization |
| POST | /users/signup | Sign up | no need | 
| POST | /users/login | Log in | no need | 
| GET | / | Retrieve all recipes | no need |
| GET | /categories/ExCat | ExCat Categorie page | no need |
| GET | /recepie/ExRec | ExRec Recipe page | noo need |
| POST | /recepie/ExRec | Leave Comment | Basic Auth |
| PUT | /recepie/ExRec | Like Recipe | Basic Auth |
| POST | /create | Create new Recipe | Basic Auth | 

Body for SignUp
```json
{
"username" : "user",
"password" : "pass",
"email : "mail@gmail.com"
}
```
Body for LogIn
```json
{
    "username" : "user",
    "password" : "pass"
}
```
Body for Comment
```json
{"text" : "new comment"}
```
Body for Create Recipe
```json
{
"name" : "recepie name" ,
"text" : " Main Text about Recipe " ,
"account" : 1 ,
"main_recepie" : " main recipe " ,
"categorie" : 1

,
"ingiridients": [{"name" : "salt" , "measurement":"pinch" , "number":"1"},
 {"name" : "rice" , "measurement":"cup" , "number":"2"}]

}
```

Installation & Setup
- Clone the repository:
```bash
git clone https://github.com/Sina-Rayo/Papion
cd [PROJECT DIRECTORY]
```
- Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
- Install dependencies:
```bash
pip install -r requirements.txt
```
- Apply migrations:
```bash
python manage.py migrate
```
- Run the server:
```bash
python manage.py runserver
```
- API base URL: http://127.0.0.1:8000/
Usage
Consume the API using tools like Postman or cURL, passing Basic Authentication credentials for protected endpoints.
Contributing
Pull requests are welcome! Follow these steps:
- Fork the repository
- Create a new branch (git checkout -b feature-branch)
- Make your changes & commit (git commit -m "Added a new feature")
- Push to the branch (git push origin feature-branch)
- Submit a pull request

