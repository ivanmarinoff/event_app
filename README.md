# [event_app](git@github.com:ivanmarinoff/event_app.git)


This is a `Event App` course project built with  **Django**.
> Example project by [SoftUni](http://www.softuni.bg").

<br>

## This is a App `Home page`

![home_page](https://github.com/ivanmarinoff/event_app/assets/107050101/9f7c0453-668a-49f8-9516-90cb4d723994)
<br />

## This is a `Profile details` page
![profile_details](https://github.com/ivanmarinoff/event_app/assets/107050101/059922df-580f-46cb-b7b7-60dd7356d08a)

<br />

## This is a `Create Event` view
![create_event](https://github.com/ivanmarinoff/event_app/assets/107050101/0114d557-3cae-4ee6-8bda-e9c2d19bac06)

<br />

## This is a `Curent Events` page
![current_event](https://github.com/ivanmarinoff/event_app/assets/107050101/29216a4c-fef4-44b7-b33d-6e816853257d)

<br />

## This is a `Django Admin` page
![django_admin](https://github.com/ivanmarinoff/event_app/assets/107050101/185c6b7c-c6f6-48db-a4db-d8d58fcb2aac)

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
