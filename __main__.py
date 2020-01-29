#!/usr/bin/python
import sys
from user_input import Input
from create_template import Create

input = Input()
env = input.ReadEnvFromUser()
cidr = input.ReadCIDRFromUser()

create = Create()
cfn = create.CreateTemplate(env, cidr)
print (cfn.to_json())
