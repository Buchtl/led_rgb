import unittest
import led_rgb.tests.context
from led_rgb.src.led_pwm import LedPwm


class TestStringMethods(unittest.TestCase):
    subject: LedPwm

    def setUp(self):
        self.subject = LedPwm()

    def test_current_rgb(self):
        self.assertEqual('0x000000', self.subject.get_rgb())


if __name__ == '__main__':
    unittest.main()
