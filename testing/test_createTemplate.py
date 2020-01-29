import unittest
import json
import sys
sys.path.append('/Users/alka/Downloads/NENT-f_addTests/')
from create_template import Create

class TestCreateTemplate(unittest.TestCase):
  
  def test_ReadEnv1(self):
    create = Create()
    cfn = Create.CreateTemplate(create, 'a', 'z')
    try:
      json_object = json.loads(cfn.to_json())
    except ValueError as e:
      return False
    return True

if __name__ == '__main__':
  unittest.main()
