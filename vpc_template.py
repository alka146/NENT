#!/usr/bin/python

import sys
import ConfigParser

from troposphere import Output
from troposphere import  Ref, Tags, Template
from troposphere.ec2 import PortRange, NetworkAcl, Route, \
    VPCGatewayAttachment, VPC, NetworkAclEntry, InternetGateway 


config = ConfigParser.ConfigParser()
config.read(sys.argv[1])
env = config.get('variables', 'env')
cidr = config.get('variables', 'cidr')


t = Template()

# Cloud Formation Template Description

t.set_description("""\
Service VPC""")

# Cloud Formation Template Metadata

t.add_metadata({
    "DependsOn": [],
    "Environment": (env),
    "StackName": (env) + "-VPC",
})

# Cloud Formation Resources

# Internet Gateway

internetGateway = t.add_resource(
    InternetGateway(
        'InternetGateway',
        Tags=Tags(
            Environment=(env),
            Name=(env) + "-InternetGateway")))
out_igw = Output("InternetGateway")
out_igw.Value = Ref(internetGateway)

# VPC

VPC = t.add_resource(
    VPC(
        'VPC',
        CidrBlock= (cidr),
        EnableDnsHostnames="true",
        EnableDnsSupport="true",
        InstanceTenancy= "default",
        Tags=Tags(
            Environment=(env),
            Name=(env) + "-ServiceVPC")))

out_vpc = Output("VPCID")
out_vpc.Value = Ref(VPC)

# Internet Gateway Attachment to VPC

gatewayAttachment = t.add_resource(
    VPCGatewayAttachment(
        'VpcGatewayAttachment',
        VpcId=Ref(VPC),
        InternetGatewayId=Ref(internetGateway)))


# NACL

networkAcl = t.add_resource(
    NetworkAcl(
        'VpcNetworkAcl',
        VpcId=Ref(VPC),
        Tags=Tags(
            Environment=(env),
            Name=(env) + "-NetworkAcl"),
    ))

# NACL Ingress

InboundPrivateNetworkAclEntry = t.add_resource(NetworkAclEntry(
    "VpcNetworkAclInboundRule",
    NetworkAclId=Ref(networkAcl),
    RuleNumber=100,
    Protocol="6",
    PortRange=PortRange(To="443", From="443"),
    Egress="false",
    RuleAction="allow",
    CidrBlock="0.0.0.0/0",
))

# NACL Egress

OutBoundPrivateNetworkAclEntry = t.add_resource(NetworkAclEntry(
    "VpcNetworkAclOutboundRule",
    NetworkAclId=Ref(networkAcl),
    RuleNumber=200,
    Protocol="6",
    Egress="true",
    RuleAction="allow",
    CidrBlock="0.0.0.0/0",
))

t.add_output(out_igw)
t.add_output(out_vpc)

print(t.to_json())