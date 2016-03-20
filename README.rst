django-owm-legacy
=================

.. image:: https://travis-ci.org/openwisp/django-owm-legacy.svg
   :target: https://travis-ci.org/openwisp/django-owm-legacy

.. image:: https://coveralls.io/repos/openwisp/django-owm-legacy/badge.svg
  :target: https://coveralls.io/r/openwisp/django-owm-legacy

.. image:: https://requires.io/github/openwisp/django-owm-legacy/requirements.svg?branch=master
   :target: https://requires.io/github/openwisp/django-owm-legacy/requirements/?branch=master
   :alt: Requirements Status

.. image:: https://badge.fury.io/py/django-owm-legacy.svg
   :target: http://badge.fury.io/py/django-owm-legacy

.. image:: https://img.shields.io/pypi/dm/django-owm-legacy.svg
   :target: https://pypi.python.org/pypi/django-owm-legacy

------------

Legacy features of OpenWISP Manager reimplemented in django.

Install stable version from pypi
--------------------------------

Install from pypi:

.. code-block:: shell

    pip install django-owm-legacy

Install development version
---------------------------

Install tarball:

.. code-block:: shell

    pip install https://github.com/openwisp/django-owm-legacy/tarball/master

Alternatively you can install via pip using git:

.. code-block:: shell

    pip install -e git+git://github.com/openwisp/django-owm-legacy#egg=django-owm-legacy

If you want to contribute, install your cloned fork:

.. code-block:: shell

    git clone git@github.com:<your_fork>/django-owm-legacy.git
    cd django-owm-legacy
    python setup.py develop

Setup (integrate in an existing django project)
-----------------------------------------------

Add ``django_netjsonconfig``, ``sortedm2m`` and ``owm_legacy`` to ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS = [
        # other apps
        'django_netjsonconfig',
        'sortedm2m',
        'reversion',
        'owm_legacy'
        # ...
    ]

Your ``urls.py`` should look like the following:

.. code-block:: python

    from django.conf.urls import include, url
    from django.contrib import admin
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    admin.autodiscover()


    urlpatterns = [
        url(r'^admin/', include(admin.site.urls)),
        url(r'^', include('django_netjsonconfig.controller.urls', namespace='controller')),
        url(r'^', include('owm_legacy.urls', namespace='owm')),
    ]

    urlpatterns += staticfiles_urlpatterns()

Installing for development
--------------------------

Install sqlite:

.. code-block:: shell

    sudo apt-get install sqlite3 libsqlite3-dev

Install your forked repo:

.. code-block:: shell

    git clone git://github.com/<your_fork>/django-owm-legacy
    cd django-owm-legacy/
    python setup.py develop

Install test requirements:

.. code-block:: shell

    pip install -r requirements-test.txt

Create database:

.. code-block:: shell

    cd tests/
    ./manage.py migrate
    ./manage.py createsuperuser

Launch development server:

.. code-block:: shell

    ./manage.py runserver

You can access the admin interface at http://127.0.0.1:8000/admin/.

Run tests with:

.. code-block:: shell

    ./runtests.py

Settings
--------

``OWM_LEGACY_ALLOWED_SUBNETS``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------+------------------------------------------+
| **type**:    | ``list``                                 |
+--------------+------------------------------------------+
| **default**: | ``['10.8.0.0/16', '127.0.0.1/32']``      |
+--------------+------------------------------------------+

List of strings representing ip networks allowed to retrieve
checksums and download configuration archives.

Contributing
------------

1. Announce your intentions in the `OpenWISP Mailing List <https://groups.google.com/d/forum/openwisp>`_
2. Fork this repo and install it
3. Follow `PEP8, Style Guide for Python Code`_
4. Write code
5. Write tests for your code
6. Ensure all tests pass
7. Ensure test coverage is not under 90%
8. Document your changes
9. Send pull request

.. _PEP8, Style Guide for Python Code: http://www.python.org/dev/peps/pep-0008/
