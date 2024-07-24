This project is based on the Python crash course book.

### Writing a web spec
A spec needs to:
- detail project goals
- project functionality
- discuss appearance
- user interface

### Project spec
We’ll write a blog app  that allows users to blog on topics they’re interested in and to make journal entries. The blog  home page will describe the site and invite users to either register or log in. Once logged in, a user can create new blogs, add new entries, and read
and edit existing entries.

### Notes on django
- manage.py - takes in commands and feeds them to parts of django that needs it
- settings.py - controls how django interacts with your system and manages your project
- urls.py - tells django which build in response to browser requests
- wsgi.py - helps django serve the file it creates

database
- django stores info in databases
command: python manage.py migrate
- we modify a database, we say we’re migrating the database
SQLite is a database that runs off a single file

viewing the project
command:python manage.py runserver
- The URL http://127.0.0.1:8000/ indicates that the project is listening for requests on port 8000 on your computer, which is called a localhost


