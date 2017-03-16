import unittest
from caesar_gui import Application

class MyTests (unittest.TestCase):
    def test_encryption(self):
        app = Application()
        output = app.caesar("aaa",3, 1)
        self.assertEqual(output, "ddd")

    def test_decryption(self):
        app = Application()
        output = app.caesar("bbb",1, 2)
        self.assertEqual(output, "aaa")

if __name__ == "__main__":
	unittest.main()
