# EC2-Instance-Start-Stop-Python3-AWS-Lambda

EC2 Instance Start/Stop Python3 AWS Lambda
A Serverless Application that starts and stops your EC2 instance with the help of tags , cron expressions and AWS Lambda.

Serverless Framework (https://serverless.com/) aims to ease the pain of creating, deploying, managing and debugging Lambda function. 

It integrates well with CI/CD tools 

It has CloudFormation support so your entire stack can be deployed using this Framework 

This iterates over all region in AWS and checks tags and stops or start EC2 at scheduled time


**Supported cron format**

```
*    *    *    *    *    *
┬    ┬    ┬    ┬    ┬    ┬
│    │    │    │    │    |
│    │    │    │    │    └ day of week (0 - 7) (0 or 7 is Sun)
│    │    │    │    └───── month (1 - 12)
│    │    │    └────────── day of month (1 - 31)
│    │    └─────────────── hour (0 - 23)
│    └──────────────────── minute (0 - 59)
└───────────────────────── second (0 - 59, optional)

```

## Getting Started

Instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

sls create --template aws-python3 --path ec2-start-stop
cd ec2-start-stop
sls deploy -v

**To invoke a function:**

sls invoke -f ec2-start -l

sls invoke -f ec2-stop -l

**To see logs:**

sls logs -f ec2-start -t

sls logs -f ec2-stop -t


### Prerequisites

What things you need to install the software and how to install them

```
**Installing serverless**

Install dependencies (Node & AWS CLI)

Install the serverless framework 

npm install -g serverless 

Setting up AWS for user 
Download credentials and setup serverless to use these credentials 

```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
**To invoke a function:**

sls invoke -f ec2-start -l

sls invoke -f ec2-stop -l

**To see logs:**

sls logs -f ec2-start -t

sls logs -f ec2-stop -t

```

And repeat

```
until finished
```


## Running the tests

This can be integrated with Continuous Integration frameworks

This can be integrated with Continuous Delivery frameworks

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

Future Enhancements 

```
This can be integrated with Continuous Integration frameworks

This can be integrated with Continuous Delivery frameworks

Improve CRON Job to only run on weekdays

Looping strategy if we have over 100 EC2 instances

Improve Logs to display in message in case no instances are to be stopped or started


```

