#!/usr/bin/python
from user_input import Input
from create_template import Create

input = Input()
env = input.ReadEnv()
cidr = input.ReadCIDR()

create = Create()
create.CreateTemplate(env, cidr)