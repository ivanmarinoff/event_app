# [event_app](git@github.com:ivanmarinoff/event_app.git)


This is a `Event App` course project built with  **Django**.
> Example project by [SoftUni](http://www.softuni.bg").

<br>

## This is a App `Home page`

![home](file:///static/pictures/home_page.png)
<br />

## This is a `Profile details` page
![profile](file:///static/pictures/profile_details.png)
<br />

## This is a `Create Event` view
![create_event](file:///static/pictures/create_event.png)
<br />

## This is a `Curent Events` page

![current_event](file:///static/pictures/current_events.png)
<br />

## This is a `Django Admin` page
![admin](file:///static/pictures/django_admin.png)

<br />

- **Sections Covered**: 
  - `Admin Section`, reserved for `superusers`
  - `All pages` managed by `Django.contrib.AUTH`
  - `Create user` page
  - `Create event` page
  - `Current events` page 
  

## How to use it
<br />

> **Install the package** via `PIP` 

```bash
$ Use the pip install -r requirements.txt command 
// OR
$ pip install git@github.com:ivanmarinoff/event_app.git
```

<br />

> Use command `venv\Scripts\activate` in to terminal to create `venv` file of your Django project directory!

<br />

> **Start the app**
> To set up SQLite database run the `db.sqlite3` file


```bash
$ # Set up the database
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Create the superuser
$ python manage.py createsuperuser
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
```

Access the `admin` section in the browser: `http://127.0.0.1:8000/`

<br />
