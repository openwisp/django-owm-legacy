from time import sleep

from django.test import TestCase
from django.urls import reverse

from openwisp_controller.config.models import Config, Device
from openwisp_controller.config.tests import CreateConfigMixin
from openwisp_users.tests.utils import TestOrganizationMixin
from owm_legacy.settings import ALLOWED_SUBNETS


class TestOwmLegacy(CreateConfigMixin, TestOrganizationMixin, TestCase):
    """
    tests for owm_legacy
    """

    config_model = Config
    device_model = Device

    def test_get_config_md5(self):
        c = self._create_config()
        response = self.client.get(
            reverse('owm_legacy:get_config_md5', args=[c.mac_address])
        )
        self.assertEqual(
            response['Content-Disposition'],
            'attachment; filename={0}'.format(self.TEST_MAC_ADDRESS),
        )
        self.assertEqual(len(response.content), 32)
        checksum1 = response.content
        sleep(1)
        response = self.client.get(
            reverse('owm_legacy:get_config_md5', args=[c.mac_address])
        )
        checksum2 = response.content
        self.assertEqual(checksum1, checksum2)
        c.refresh_from_db()
        self.assertIsNotNone(c.device.last_ip)

    def test_get_config(self):
        d = self._create_device(name='test')
        c = self._create_config(device=d)
        response = self.client.get(
            reverse('owm_legacy:get_config', args=[c.mac_address])
        )
        self.assertEqual(
            response['Content-Disposition'], 'attachment; filename=test.tar.gz'
        )

    def test_last_ip(self):
        c = self._create_config()
        self.client.get(reverse('owm_legacy:get_config', args=[c.mac_address]))
        c.refresh_from_db()
        self.assertIsNotNone(c.device.last_ip)

    def test_status(self):
        c = self._create_config()
        self.client.get(reverse('owm_legacy:get_config', args=[c.mac_address]))
        c.refresh_from_db()
        self.assertEqual(c.status, 'applied')

    def test_forbidden_ip(self):
        ALLOWED_SUBNETS.remove('127.0.0.1/32')
        response = self.client.get(
            reverse('owm_legacy:get_config', args=['00:11:22:33:44:55'])
        )
        self.assertEqual(response.status_code, 403)
        ALLOWED_SUBNETS.append('127.0.0.1/32')
