# first_name = "ada"
# # last_name="love"
# # full_name=f"{first_name} {last_name}"
# # print(full_name)
from django01.name import *
import unittest
class NameTest(unittest.TestCase):
    ''' 测试'''
    def test_name(self):
        fm = get_name("长" , "框")
        equal = self.assertEqual(fm, '长 框')
        print(equal)

    def test_name2(self):
        fm = get_fname("a", "b","c")
        self.assertEqual(fm, 'a c b')


if __name__ =="__main__":
    unittest.main()