=====
Short URL
=====

ShortURL is a URL shortener app built in Python by Shaig Gafarli. Short URLs will make your sharing experience enjoyable!

Using instructions:
First time users need to sign up to the webpage with their emails in order to use the service. There is no limit for URL shortening. After you're done, you can logout by clicking on 'Sign Out' button. This will direct you to the home page.

Django framework was used to develop this app.
Back-end: Python
Front-end: HTML, CSS & Javascript

Quick start
-----------

1. Add "shorturl" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'shorturl.apps.ShorturlConfig',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('shorturl/', include('shorturl.urls')),

3. Run ``python manage.py migrate`` to create the shorturl models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
to login as admin.

5. Visit http://127.0.0.1:8000/ to shorten your URLs.

ShortURL App was deployed to Heroku.
Please visit: https://urlworld.herokuapp.com
