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

Create Bucket 
 
aws s3 mb s3://sambucketec2stopstart --region eu-west-1

Create Package 

sam package --template-file ./lambda.yml --output-template-file sam-template.yml --s3-bucket sambucketec2stopstart

Deploy Package

sam deploy --template-file sam-template.yml --stack-name ec2-kick-off-end --capabilities CAPABILITY_IAM

 Deploying
 ------------


 ![alt text](https://pictures142857.s3.ap-south-1.amazonaws.com/sam.PNG)
