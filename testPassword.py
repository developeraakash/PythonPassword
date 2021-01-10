import unittest
from Password import Password
from User import User

class testPassword(unittest.TestCase):
    def test1(self):
        User.set_name(self,name = "John")
        response = User.get_name(self)
        self.assertTrue(response,"John")
        

    def test2(self):
        V1 = Password.pwd_complex(self,"Hkdun!123k")
        self.assertEqual(V1,True)

if __name__ == '__main__':
    unittest.main()