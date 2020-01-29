import unittest
from user_input import Input

class TestUserInput(unittest.Testcase):
  
  def test_ReadEnv1(self):
    env = Input.ReadEnv(abc)
    self.assertEqual(env, INVALID)
  
  def test_ReadEnv2(self):
    env = Input.ReadEnv(Development)
    self.assertEqual(env, Development)
  
  def test_ReadEnv3(self):
    env = Input.ReadEnv(prod)
    self.assertEqual(env, INVALID)

if __name__ == '__main__':
  unittest.main()
