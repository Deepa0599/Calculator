import unittest

def login_verification(username,password):
    if username == "admin" and password == "12345":
        return True
    else:
        return False

class Verification(unittest.TestCase):
    def test_verfication1(self):
        username = "admin"
        password = "12345"
        result = login_verification(username, password)
        self.assertTrue(result)

if __name__=="__main__": 
    unittest.main()


