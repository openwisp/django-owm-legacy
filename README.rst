django-owm-legacy
=================

.. image:: https://travis-ci.org/openwisp/django-owm-legacy.svg
   :target: https://travis-ci.org/openwisp/django-owm-legacy
   :alt: CI build status

.. image:: https://coveralls.io/repos/openwisp/django-owm-legacy/badge.svg
  :target: https://coveralls.io/r/openwisp/django-owm-legacy
  :alt: Test Coverage

.. image:: https://requires.io/github/openwisp/django-owm-legacy/requirements.svg?branch=master
   :target: https://requires.io/github/openwisp/django-owm-legacy/requirements/?branch=master
   :alt: Requirements Status

.. image:: https://img.shields.io/gitter/room/nwjs/nw.js.svg
   :target: https://gitter.im/openwisp/general
   :alt: Chat

.. image:: https://badge.fury.io/py/django-owm-legacy.svg
   :target: http://badge.fury.io/py/django-owm-legacy

.. image:: https://pepy.tech/badge/django-own-legacy
   :target: https://pepy.tech/project/django-own-legacy
   :alt: Downloads

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://pypi.org/project/black/
   :alt: code style: black

------------

Legacy features of OpenWISP Manager reimplemented in django for `OpenWISP2
<https://github.com/openwisp/ansible-openwisp2>`_.

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

Add ``openwisp_controller`` and ``owm_legacy`` to ``INSTALLED_APPS`` as follow:

.. code-block:: python

    INSTALLED_APPS = [
        # ...
        'django.contrib.sites',
        # allauth
        'allauth',
        'allauth.account',
        'django_extensions',
        # openwisp2 modules
        'openwisp_controller.config',
        'openwisp_controller.pki',
        'openwisp_controller.geo',
        'openwisp_controller.connection',
        'openwisp_users',
        # openwisp2 admin theme
        # (must be loaded here)
        'openwisp_utils.admin_theme',
        'django.contrib.admin',
        'django.forms',
        # other dependencies
        'sortedm2m',
        'reversion',
        'leaflet',
        'flat_json_widget',
        'owm_legacy',
        # ...
    ]

Other settings needed in ``settings.py``:

.. code-block:: python

    EXTENDED_APPS = ('django_x509', 'django_loci')

    AUTH_USER_MODEL = 'openwisp_users.User'
    SITE_ID = 1

Your ``urls.py`` should look like the following:

.. code-block:: python

    from django.conf.urls import include, url
    from django.contrib import admin
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    admin.autodiscover()


    urlpatterns = [
        url(r'^admin/', include(admin.site.urls)),
        url(r'^', include('openwisp_controller.urls', namespace='controller')),
        url(r'^', include('owm_legacy.urls', namespace='owm_legacy')),
    ]

    urlpatterns += staticfiles_urlpatterns()

Installing for development
--------------------------

Install sqlite:

.. code-block:: shell

    sudo apt install -y sqlite3 libsqlite3-dev openssl libssl-dev
    sudo apt install -y gdal-bin libproj-dev libgeos-dev libspatialite-dev libsqlite3-mod-spatialite

Launch Redis:

.. code-block:: shell
    
    docker-compose up -d redis

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

Launch celery worker (for background jobs):

.. code-block:: shell
    
    celery -A openwisp2 worker -l info

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

Please refer to the `OpenWISP contributing guidelines <http://openwisp.io/docs/developer/contributing.html>`_.

.. _PEP8, Style Guide for Python Code: http://www.python.org/dev/peps/pep-0008/

Changelog
---------

See `CHANGES <https://github.com/openwisp/django-owm-legacy/blob/master/CHANGES.rst>`_.

License
-------

See `LICENSE <https://github.com/openwisp/django-owm-legacy/blob/master/LICENSE>`_.

Support
-------

See `OpenWISP Support Channels <http://openwisp.org/support.html>`_.
