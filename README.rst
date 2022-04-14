=====
Short URL
=====

ShortURL is a Django app to shorten extra long web URLs. Short URLs will make your sharing experience enjoyable!

Detailed documentation is in the "docs" directory.

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