#!/usr/bin/env python3
"""
top-ami
generate a human readable list of most popular AWS ami images used for running instances.
"""


import boto3
from collections import Counter
import argparse
import json
import sys

parser = argparse.ArgumentParser()
parser.add_argument("AWS_PROFILE", default='default', nargs="?", help="which aws profile configured in ~/.aws/credentials should we use?")

args = parser.parse_args()

boto_connection = boto3.session.Session(profile_name=args.AWS_PROFILE)
"""
replace 'default', with what ever aws account profile you want to use in your
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
    pass it an AMI id, returns list ["creation_date", "description"]
    if there is anything wrong with returning creation_date, chances are, the ami was deleted.
    """
    image = ec2.Image(ami_id)
    try:
        info = [image.creation_date, image.description]
        return info
    except Exception:
        return ["missing_image", "missing_image"]
        pass



def all_amis():
    """
    Return a list of ALL AMI IDs on the account that match filters in 'instances'
    """
    ami_list = []
    for instance in instances:
        ami_list.append(instance.image_id)
    return ami_list


def top_amis():
    """
    Get a tuple of popular AMI ids and popularity count
    """
    input_ami_list = Counter(all_amis())
    top_list = input_ami_list.most_common(100)
    return list(top_list)


def main():
    """
    This is the business end of "top-ami"
    loops over the top AMI list and builds up the entire output.
    The output is a valid json that can be accessed with jq.
    """
    nice_top_ami_list = [[*row] for row in top_amis()]
    """
    We flatten the touple to a list.
    """

    top_ami_json = []
    for ami_id in nice_top_ami_list:
        single_ami_json = {
        "creation_date": ami_info(ami_id[0])[0],
        "ami_id": str(ami_id[0]),
        "count": str(ami_id[1]),
        "description": ami_info(ami_id[0])[1]
        }

        top_ami_json.append(single_ami_json)

    json_data = json.dumps(top_ami_json)
    print(json_data)



if __name__ == "__main__":
    sys.exit(main())
