Changelog
=========

Version 1.1.0 [2024-11-29]
--------------------------

- Upgraded to openwisp-controller 1.1.0
- Upgraded to django 4.2

Version 1.0.0 [2022-05-03]
--------------------------

- Upgraded to openwisp-controller 1.0.0
- Upgraded to django 3.2 and django 4.0

Version 0.5.0 [2021-02-05]
--------------------------

- upgraded to openwisp-controller 0.8

Version 0.4.1 [2018-02-19]
--------------------------

- upgraded to django 2.0 and django-netjsonconfig 0.8.0

Version 0.4.0 [2017-05-24]
--------------------------

- `8078e07
  <https://github.com/openwisp/django-owm-legacy/commit/8078e07>`_:
  Upgraded to **django-netjsonconfig 0.6.0**

Version 0.3.1 [2017-03-08]
--------------------------

- `fb595bd
  <https://github.com/openwisp/django-owm-legacy/commit/fb595bd>`_:
  [views] Added support for openwisp-controller

Version 0.3.0 [2017-01-18]
--------------------------

- `2db46c8
  <https://github.com/openwisp/django-owm-legacy/commit/2db46c8>`_:
  [requirements] set minimum `django-netjsonconfig
  <https://github.com/openwisp/django-netjsonconfig>`_ version to 0.5.0
- `f388d9c
  <https://github.com/openwisp/django-owm-legacy/commit/f388d9c>`_:
  [views] use ``mac_address`` field instead of ``key``
- `5a8b793
  <https://github.com/openwisp/django-owm-legacy/commit/5a8b793>`_:
  [views] added compatibility with ``openwisp2.config``

Version 0.2.3 [2016-02-29]
--------------------------

- `b162867
  <https://github.com/openwisp/django-owm-legacy/commit/b162867>`_: log
  denied requests with warning level

Version 0.2.2 [2016-02-12]
--------------------------

- `f66bec1
  <https://github.com/openwisp/django-owm-legacy/commit/f66bec1>`_: update
  ``last_ip`` on checksum if necessary
- `4ae482e
  <https://github.com/openwisp/django-owm-legacy/commit/4ae482e>`_:
  updated minimum ``django-netjsonconfig`` version to 0.2.3

Version 0.2.1 [2016-01-28]
--------------------------

- `ebf950a
  <https://github.com/openwisp/django-owm-legacy/commit/ebf950a>`_:
  updated requirements.txt
- `61e6ddd
  <https://github.com/openwisp/django-owm-legacy/commit/61e6ddd>`_: fill
  last_ip and status fields when config is downloaded

Version 0.2 [2016-01-14]
------------------------

- `#1 <https://github.com/openwisp/django-netjsonconfig/issues/1>`_:
  upgraded to django-netjsonconfig 0.2

Version 0.1 [2015-12-21]
------------------------

- ``get_config`` view
- ``get_config_md5`` view
- ``OWM_LEGACY_ALLOWED_SUBNETS`` setting
