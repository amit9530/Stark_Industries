from WWUDo import View_Skip
from WWUDo import Add_Kid
from WWUDo import View_Kid
from WWUDo import Print_Login_Count
from WWUDo import Add_Question
from WWUDo import Delete_User
from WWUDo import Reset_Player
from WWUDo import Print_Last_Grade
from WWUDo import login_report


import unittest
class Unit_Test(unittest.TestCase):

    def test_View_Skip(self):
        self.assertEqual(View_Skip(), 0)
    def test_Add_Kid(self):
        parent_id = 123456789
        self.assertEqual(Add_Kid(parent_id), 0)
    def test_View_Kid(self):
        self.assertEqual(View_Kid(), 0)
    def test_Print_Login_Count(self):
        self.assertEqual(Print_Login_Count(), 0)
    def test_Add_Question(self):
        self.assertEqual(Add_Question(), 0)
    def test_Delete_User(self):
        self.assertEqual(Delete_User(), 0)
    def test_Reset_Player(self):
        self.assertEqual(Reset_Player(), 0)
    def test_Print_Last_Grade(self):
        id = 8415
        self.assertEqual(Print_Last_Grade(id), 0)
    def test_Print_login_report(self):
        id = 8415
        self.assertEqual(login_report(id), 0)

        

'''if __name__ == '__main__':
    unittest.main()'''