from time import sleep

from django.core.urlresolvers import reverse
from django.test import TestCase

from django_netjsonconfig.models import Config
from owm_legacy.settings import ALLOWED_SUBNETS


class TestOwmLegacy(TestCase):
    """
    tests for owm_legacy
    """
    def _create_config(self):
        d = Config(name='test',
                   backend='netjsonconfig.OpenWrt',
                   config={'general':{'hostname':'test'}},
                   key='00:11:22:33:44:55')
        d.full_clean()
        d.save()
        return d

    def test_get_config_md5(self):
        d = self._create_config()
        response = self.client.get(reverse('owm:get_config_md5', args=[d.key]))
        self.assertEqual(response['Content-Disposition'], 'attachment; filename=00:11:22:33:44:55')
        self.assertEqual(len(response.content), 32)
        checksum1 = response.content
        sleep(1)
        response = self.client.get(reverse('owm:get_config_md5', args=[d.key]))
        checksum2 = response.content
        self.assertEqual(checksum1, checksum2)
        d.refresh_from_db()
        self.assertIsNotNone(d.last_ip)

    def test_get_config(self):
        c = self._create_config()
        response = self.client.get(reverse('owm:get_config', args=[c.key]))
        self.assertEqual(response['Content-Disposition'], 'attachment; filename=test.tar.gz')

    def test_last_ip(self):
        c = self._create_config()
        response = self.client.get(reverse('owm:get_config', args=[c.key]))
        c.refresh_from_db()
        self.assertIsNotNone(c.last_ip)

    def test_status(self):
        c = self._create_config()
        response = self.client.get(reverse('owm:get_config', args=[c.key]))
        c.refresh_from_db()
        self.assertEqual(c.status, 'running')

    def test_forbidden_ip(self):
        ALLOWED_SUBNETS.remove('127.0.0.1/32')
        response = self.client.get(reverse('owm:get_config', args=['00:11:22:33:44:55']))
        self.assertEqual(response.status_code, 403)
        ALLOWED_SUBNETS.append('127.0.0.1/32')
