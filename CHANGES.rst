Changelog
=========

Version 0.3.0 [2017-01-18]
--------------------------

- `2db46c8 <https://github.com/openwisp/django-owm-legacy/commit/2db46c8>`_:
  [requirements] set minimum `django-netjsonconfig
  <https://github.com/openwisp/django-netjsonconfig>`_ version to 0.5.0
- `f388d9c <https://github.com/openwisp/django-owm-legacy/commit/f388d9c>`_:
  [views] use ``mac_address`` field instead of ``key``
- `5a8b793 <https://github.com/openwisp/django-owm-legacy/commit/5a8b793>`_:
  [views] added compatibility with ``openwisp2.config``

Version 0.2.3 [2016-02-29]
--------------------------

- `b162867 <https://github.com/openwisp/django-owm-legacy/commit/b162867>`_:
  log denied requests with warning level

Version 0.2.2 [2016-02-12]
--------------------------

- `f66bec1 <https://github.com/openwisp/django-owm-legacy/commit/f66bec1>`_:
  update ``last_ip`` on checksum if necessary
- `4ae482e <https://github.com/openwisp/django-owm-legacy/commit/4ae482e>`_:
  updated minimum ``django-netjsonconfig`` version to 0.2.3

Version 0.2.1 [2016-01-28]
--------------------------

- `ebf950a <https://github.com/openwisp/django-owm-legacy/commit/ebf950a>`_:
  updated requirements.txt
- `61e6ddd <https://github.com/openwisp/django-owm-legacy/commit/61e6ddd>`_:
  fill last_ip and status fields when config is downloaded

Version 0.2 [2016-01-14]
------------------------

- `#1 <https://github.com/openwisp/django-netjsonconfig/issues/1>`_:
  upgraded to django-netjsonconfig 0.2

Version 0.1 [2015-12-21]
------------------------

- ``get_config`` view
- ``get_config_md5`` view
- ``OWM_LEGACY_ALLOWED_SUBNETS`` setting
