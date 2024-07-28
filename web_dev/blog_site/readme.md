This project is based on the Python crash course book. Notes below are from the book too!

### Writing a web spec
A spec needs to:
- detail project goals
- project functionality
- discuss appearance
- user interface

### Project spec
We’ll write a blog app  that allows users to blog on topics they’re interested in and to make journal entries. The blog  home page will describe the site and invite users to either register or log in. Once logged in, a user can create new blogs, add new entries, and read and edit existing entries.

### Django website
- manage.py - file takes in commands and feeds them to parts of django that needs it
- settings.py - controls how django interacts with your system and manages your project
- urls.py - tells django which build in response to browser requests
- wsgi.py - helps django serve the file it creates

Database
----
- django stores info in databases
command: python manage.py migrate
- we modify a database, we say we’re migrating the database
- The SQLite is a database that runs off a single file

Viewing the project
---
- running the project:
command:python manage.py runserver
- The URL http://127.0.0.1:8000/ indicates that the project is listening for requests on port 8000 on your computer, which is called a localhost
starting app
command: python3 manage startapp blog_website
- A class called Topic, which inherits from Model
    —a parent class included in Django that defines a model’s basic functionality
    - We add two attributes to the Topic class: text and date_added
    - We tell Django which attribute to use by default when it displays information about a topic. Django calls a __str__() method to display a simple representation of a mode

Activating models
----
- To use our models, we have to tell Django to include our app in the overall project
- Add our app to this list by modifying INSTALLED_APP
- Grouping apps together in a project helps to keep track of them as the
project grows to include more apps
- Django to modify the database so it can store information related to the model Topic
- command line: python manage.py makemigrations app_name
- The command makemigrations tells Django to figure out how to modify
the database so it can store the data associated with any new models we’ve
defined
- apply this migration and have Django modify the database
- Whenever we want to modify the data that Learning Log manages, we’ll follow these three steps: modify models.py, call makemigrations on learning_logs, and tell Django to migrate the project

Admin site
----
- We’ll set up the admin site and use it to add some topics through the
Topic model.
The most restrictive privilege settings allow a user to only read public information on the site. Registered users typically have the privilege of reading their own private data and some selected information available only to
members. To effectively administer a web application, the site owner usuall needs access to all information stored on the site. A good administrator is careful with their users’ sensitive information, because users put a lot of trust into the apps they access
- creating a superuser
python manage.py createsuperuser

Registering a Model with the Admin Site
----
- Django includes some models in the admin site automatically, such as User
and Group, but the models we create need to be added manually
- register Topic with the admin site
- The code admin.site.register() tells Django to manage our model
through the admin site
- Then you can add topics e.g. Daily blog and Weekly review

Entry model
----
- E.g. For a user to record what they’ve been learning about chess and rock climbing, we need to define a model for the kinds of entries users can make in their learning logs. Each entry needs to be associated with a particular
topic. This relationship is called a many-to-one relationship, meaning many entries can be associated with one topic
- The Entry class inherits from Django’s base Model class, ju
- The first attribute, topic, is a ForeignKey instance
  - A foreign key is a database term; it’s a reference to another record in the database
  - This is the code that connects each entry to a specific topic.

Migrating the entry model
----
- Because we’ve added a new model, we need to migrate the database again.
command: python manage.py makemigrations app name
command:python manage.py migrate
Registering Entry with the Admin Site
add to admin.py

Making pages
----
- making pages consists of three stages:
  - defining URLs
  - writing views
  - writing templates
- Define a URL pattern - A URL pattern describes the way the URL is laid out. 
- It also tells Django what to look for when matching a browser request with a site URL so it knows which page to
return.
- URL then maps to a particular view
- the view function retrieves and processes the data needed for that page
- The view function often renders the page using a template, which contains the overall structure of the page.
- We’ll define the URL for the home page, write its view function, and create a simple template

Maping a URL
----
Users request pages by entering URLs into a browser and clicking links, so we’ll need to decide what URLs are needed.
The home page URL is first:it’s the base URL people use to access the project. At the moment the base URL, http://localhost:8000/, returns the default Django site that lets us know the project was set up correctly. We’ll change this by mapping the base URL to blog page.

View
----
- a view takes in informatio from a request, prepares the data needed to generate a page, and then sends the data back to the browser, often by using a template that defines what the page will look like
- When a URL request matches the pattern we just defined, Django looks for a function called index() in the views.py file. Django then passes the request object to this view function. 
- The render() function here passes two arguments—the original request object and a template it can use to build the page


Template
----
The template defines what the page should look like, and Django fills in the relevant data each time the page is requested. A template allows you to access any data provided by the view. Because our view for the home page provided no data, this template is fairly simple. 
- add index file in subfolder
- Now when you request the project’s base URL, http://localhost:8000/, you should see the page we just built instead of the default Django page. Django
will take the requested URL, and that URL will match the pattern ''; then
Django will call the function views.index(), which will render the page using the template contained in index.html.
- Although it might seem like a complicated process for creating one page, this separation between URLs, views, and templates works quite well. It allows you to think about each aspect of a project separately. In larger projects, it allows individuals working on the project to focus on the areas
in which they’re strongest. For example, a database specialist can focus on the models, a programmer can focus on the view code, and a web designer can focus on the templates


Additional pages
----
- a page that lists all topics and a page that shows all the entries
- We’ll create a base template that all templates in the project can inherit from.
  - When building a website, some elements will always need to be repeated on each page. Rather than writing these elements directly into each page, you can write a base template containing the repeated elements and then have each page inherit from the base
  - a template tag, which is indicated by braces and percent signs {% %}. A template tag generates information to be displayed on a page
  - In a simple HTML page, a link is surrounded by the anchor tag <a>
  - Having the template tag generate the URL for us makes it much easier to keep our links up to date. We only need to change the URL pattern in urls.py, and Django will automatically insert the updated URL the next time
  the page is requested
  - Every page in our project will inherit from base.html,
  so from now on, every page will have a link back to the home page
  - we insert a pair of block tags - placeholder the child template will define the content
  - update index html, this line pulls in everything contained in the base.html template and allows index.html to define what goes in the space reserved by the content block
  - benefit of template inheritance: in a child template, we only need to include content that’s unique to that page. This not only simplifies each template, but also makes it much easier to modify the site. To modify an element common to many pages, you only need to modify the parent template. Your changes are then carried over to every
  page that inherits from that template 
- For each page, we’ll specify a URL pattern, write a view function, and write a template
  - We’ll use the word topics, so the URL http:/localhost:8000/topics/ will return this page
  - We’ve simply added topics/ into the string argument used for the home page URL
  - When Django examines a requested URL, this pattern will match any URL that has the base URL followed by topics
  - Any request with a URL that matches this pattern will then be passed to the function topics() in views.py
  - The topics() function needs to retrieve some data from the database and send it to the template
  - we query the database by asking for the Topic objects,
sorted by the date_added attribute
  - A context is a dictionary in which the keys are names we’ll use in the template to access the data, and the values are the data we need to send to the template
  - When building a page that uses data, we pass the context variable to render() as well as the request object and the path to the template

Topics template
---
- The template for the topics page receives the context dictionary, so the template can use the data that topics() provides
- We use the {% extends %} tag to inherit from base.html
- To print a variable in a template, wrap the variable name in double braces. The braces won’t appear on the page; they just indicate to Django that we’re using a template variable. So the code {{ topic }} at will be replaced by the value of topic on each pass through the loop
- modify the base template to include a link to the topics page
- We add a dash after the link to the home page u, and then add a link to the topics page using the {% url %} template tag again v. This linetells Django to generate a link matching the URL pattern with the name 'topics' in learning_logs/urls.py.

Individual topic pages
----
- We’ll again define a new URL pattern, write a view, and create a template
- We’ll also modify the topics page so each item in the bulleted list links to its corresponding topic page.
- Let’s examine the string 'topics/<int:topic_id>/' in this RL pattern. The first part of the string tells Django to look for URLs that have the wordtopics after the base URL. The second part of the string, /<int:topic_id>/,matches an integer between two forward slashes and stores the integer value in an argument called topic_i
- When Django finds a URL that matches this pattern, it calls the view function topic() with the value stored in topic_id as an argument. We’ll use the value of topic_id to get the correct topic inside the function.
- We store the topic and entries in the context dictionary x and send context to the template topic.html
- The template needs to display the name of the topic and the entries. We also need to inform the user if no entries have been made yet for this topic
- we need to modify the topics template so each topic links to the appropriate page
- We use the URL template tag to generate the proper link, based on the URL pattern in learning_logs with the name 'topic'. This URL pattern requires a topic_id argument, so we add the attribute topic.id to the URL template tag. Now each topic in the list of topics is a link to a topic page,such as http://localhost:8000/topics/1/.

so far...
----

you learned how to build simple web applications using the
Django framework. You wrote a brief project specification, installed Django to a virtual environment, set up a project, and checked that the project was set up correctly. You set up an app and defined models to represent the data for your app. You learned about databases and how Django helps you migrate your database after you make a change to your models. You created a superuser for the admin site, and you used the admin site to enter some initial data. You also explored the Django shell, which allows you to work with your project’s data in a terminal session. You learned to define URLs, create view
functions, and write templates to make pages for your site. You also used template inheritance to simplify the structure of individual templates and make it easier to modify the site as the project evolves

