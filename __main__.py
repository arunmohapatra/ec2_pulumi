"""An AWS Python Pulumi program"""

import pulumi
import pulumi_aws as aws

# Define an AWS Key Pair for SSH access
# key_pair = aws.ec2.KeyPair("my-key-pair",
#     public_key="your-public-key-here"
# )

# Create a security group to allow SSH access
sec_group = aws.ec2.SecurityGroup('web-secgrp',
    description='Enable SSH access',
    ingress=[
        aws.ec2.SecurityGroupIngressArgs(
            protocol='tcp',
            from_port=22,
            to_port=22,
            cidr_blocks=['0.0.0.0/0'],
        ),
    ]
)

# Launch an EC2 instance
ec2_instance = aws.ec2.Instance("my-ec2-instance",
    instance_type="t2.micro",
    vpc_security_group_ids=[sec_group.id],
    ami="ami-0ebfd941bbafe70c6",  # Amazon Linux 2 AMI
    # key_name=key_pair.key_name,
    tags={
        "Name": "Pulumi EC2 Instance",
    }
)

# Export the public IP of the instance
pulumi.export('public_ip', ec2_instance.public_ip)
pulumi.export('instance_id', ec2_instance.id)

