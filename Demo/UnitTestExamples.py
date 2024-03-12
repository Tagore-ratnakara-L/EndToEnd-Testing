import unittest
from Examples import Examples


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('This will run once before all the methods')

    @classmethod
    def tearDownClass(cls):
        print("This will run once after all the methods")

    def setUp(self):
        print("This will run before every method")

    def tearDown(self):
        print("This will run after every method")

    def test_add(self):
        result = Examples.add(self,10,20)
        self.assertEqual(result, 30)

    def test_sub(self):
        result = Examples.sub(self,40,20)
        self.assertEqual(result,20)


    # def test_something(self):
    #     self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
