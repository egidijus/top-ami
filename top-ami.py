#!/usr/bin/env python
"""
generate a human readable list of most popular AWS ami images used for running instances.
"""

import boto3
from collections import Counter
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("AWS_PROFILE", default='default', nargs="?", help="which aws profile configured in ~/.aws/credentials should we use?")

args = parser.parse_args()

boto_connection = boto3.session.Session(profile_name=args.AWS_PROFILE)
"""
replace 'default', with what ever aws account profile you wantto use in your
'~/.aws/credentials' file
"""
ec2 = boto_connection.resource('ec2')

instances = ec2.instances.filter(Filters=[{
    'Name': 'instance-state-name',
    'Values': ['running']
}])
"""
We will check the popularity of RUNNING ec2 instance AMIs.
"""


def ami_info(ami_id):
    """
    pass it an ami id, get creation date and description
    """
    image = ec2.Image(ami_id)
    info = [image.creation_date, image.description]
    return info


def all_amis():
    """
    retun a list of all AMIs on the account that match filters in 'instances'
    """
    ami_list = []
    for instance in instances:
        ami_list.append(instance.image_id)
    return ami_list


def top_amis(top_how_many):
    """
    pass in an 'int' how many top AMIs you want returned, get a tuple of popular AMI ids and popularity count
    """
    input_ami_list = Counter(all_amis())
    top_list = input_ami_list.most_common(top_how_many)
    return top_list


def main():
    """
    the business end of this tool.
    loops over the top AMI touple and builds up the entire output.
    """
    for element in top_amis(100):
        print("creation_date:",
              ami_info(element[0])[0], "description:",
              ami_info(element[0])[1], "ami_id:", element[0], element[1],
              "instances use this image")


main()
