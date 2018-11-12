import unittest
import SimpleAdd



class TestSimpleAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(SimpleAdd.add(3,4), 7)
        self.assertEqual(SimpleAdd.add('pavel', 'roy'), 'pavelroy')




if __name__ == '__main__':
    unittest.main()
    print('Pavel is here to learn')
