from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB, VPC, PublicSubnet, PrivateSubnet
from diagrams.aws.security import WAF

with Diagram("AWS Architecture", show=False):
    with Cluster("VPC"):
        vpc = VPC("VPC")
        with Cluster("Public Subnet"):
            public_subnet = PublicSubnet("Public Subnet")
            waf = WAF("WAF")
            elb = ELB("ELB (Load Balancer)")
            ec2_public = EC2("EC2 (Public)")
        with Cluster("Private Subnet"):
            private_subnet = PrivateSubnet("Private Subnet")
            ec2_private = EC2("EC2 (Private)")
            db = RDS("RDS")

    waf - elb
    elb - ec2_public
    elb - ec2_private
    ec2_public - db
    ec2_private - db

    vpc - public_subnet
    vpc - private_subnet
