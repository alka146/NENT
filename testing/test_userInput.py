import unittest
import sys
sys.path.append('/Users/alka/Downloads/NENT-f_addTests/')
from user_input import Input

class TestUserInput(unittest.TestCase):
  
  def test_ReadEnv1(self):
    input = Input()
    env = Input.ReadEnv(input, 'dying')
    self.assertEqual(env, 'INVALID')
  
  def test_ReadEnv2(self):
    input = Input()
    env = Input.ReadEnv(input, 'Development')
    self.assertEqual(env, 'Development')
  
  def test_ReadEnv3(self):
    input = Input()
    env = Input.ReadEnv(input, 'prod')
    self.assertEqual(env, 'INVALID')

if __name__ == '__main__':
  unittest.main()
