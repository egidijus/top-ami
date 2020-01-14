# top-ami
generate a human readable list of most popular AWS ami images used for running instances.

use with python 3.x
requires boto3, argparse

takes one argument of the AWS profile you want to use.

```
python top-ami.py profile
```

## example output

```
./top-ami.py prod
('creation_date:', '2020-01-13:01:00.000Z', 'description:', None, 'ami_id:', 'ami-66666666', 119, 'instances use this image')
('creation_date:', '2020-01-13:01:00.000Z', 'description:', None, 'ami_id:', 'ami-66666666', 52, 'instances use this image')
('creation_date:', '2020-01-13:01:00.000Z', 'description:', None, 'ami_id:', 'ami-66666666', 9, 'instances use this image')
```
