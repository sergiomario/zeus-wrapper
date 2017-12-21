# coding: utf-8

import unittest

from tapioca_zeus_wrapper import Zeus_wrapper


class TestTapiocaZeus_wrapper(unittest.TestCase):

    def setUp(self):
        self.wrapper = Zeus_wrapper()


if __name__ == '__main__':
    unittest.main()
