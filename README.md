# top-ami
Print out a json list of most popular AWS AMIs used by you running instances.


## How ?

Make will install all the packages in a virtual environment and run top-ami

Run `make`


## More details on how

Prerequisites:

* python3x
* boto3
* argparse
* pip
* virtualenv
* aws credentials configured

You can do things the difficult way and install packages from [pip-requirements.txt](pip-requirements.txt) 

```
pip install -r pip-requirements.txt
```


Then you should be able to simply run:

```
python top-ami.py
```

The only argument top-ami accepts, is the "profile" for aws credentials.
By default, top-ami will always use `default` profile.

## example output

```
./top-ami.py prod
[
  {"creation_date": "2020-01-13:01:00.000Z", "ami_id": "ami-66666666", "count": 5, "description": "super special ami"},
  {"creation_date": "2020-01-13:01:00.000Z", "ami_id": "ami-66666666", "count": 3, "description": "super special ami"},
  {"creation_date": "2020-01-13:01:00.000Z", "ami_id": "ami-66666666", "count": 2, "description": "super special ami"},
  {"creation_date": "2020-01-13:01:00.000Z", "ami_id": "ami-66666666", "count": 1, "description": "super special ami"}
]
```
