# EC2-Instance-Start-Stop-Python3-AWS-Lambda
EC2 Instance Start/Stop Python3 AWS Lambda
A Serverless Application that starts and stops your EC2 instance with the help of tags , cron expressions and AWS Lambda.

**# Usage**
You tag your instances with when you whant them stared or stoped. 

Times are always in UTC
Supported cron format

 ?????????????? minute (0 - 59)
 ? ?????????????? hour (0 - 23)
 ? ? ?????????????? day of month (1 - 31)
 ? ? ? ?????????????? month (1 - 12)
 ? ? ? ? ?????????????? day of week (0 - 6) (Sunday to Saturday;
 ? ? ? ? ?                                       7 is also Sunday on some systems)
 ? ? ? ? ?
 ? ? ? ? ?
 * * * * *  schedule command to execute

