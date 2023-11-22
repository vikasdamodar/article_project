# article_project

Simple Blog Article project which has an article list, detail view, and contact request functionalities. 

## Prerequisites and Project Requirements 
- Requirements are added in requirements.txt
- Please install by `pip install requirements.txt`

## Running Project locally
- `python manage.py migrate` - If starting a new DB
- To start the server - `python manage.py runserver`
- Locally by default port will be 8000, Please try to access via `localhost:8000/` or `http://127.0.0.1:8000/`
- Create superuser for admin page - `python manage.py createsuperuser`

## APIs and details
- `/article-list/` - Will list all the Published Articles ordered by ID, A Maximum of 5 articles will be on a page.
- `/article-detail/<int:id>/<str:slug>/` - View the details of a particular article
- `/contact-request/` - Request to contact with name, email, and content
- `/admin/` - Admin page to manage DB Data, (Please note that ContactRequest data cannot be created/modified)

## Test Cases
- `python manage.py test` to run test cases, which also checks email functionality. 

#Notes
- Currently Email send domain is not configured, So the actual recipients won't receive the email
- Email details and body can be tested using test cases
  
