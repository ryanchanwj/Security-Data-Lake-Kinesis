# AWS Security Data Lake Log Transformation using Kinesis Data Analytics


<br/>
This guide runs through how a data streaming pipeline that enriches and transforms ingested logs can be deployed in AWS using Kinesis and Glue services. 

<br/>
In this PoC, a python script is used to generate logs which is ingested by a Kinesis Data Stream. The logs simulated contains a “port_number” field. Kinesis Data Analytics transforms the log data in the Kinesis Data Stream and inserts the curated logs into another Kinesis Data Stream. The curated logs will be enriched with a “tag” field with its value dependent on the value of the “port_number” field. Kinesis Firehose Delivery Stream ingests the data from the Kinesis Data Stream for curated logs and streams it into an S3 bucket. The data is partitioned in the S3 bucket by year, month, day and hour. 

<br/>
A detailed walkthrough of the deployment steps can be found here (https://quip-amazon.com/9y2SAbT7CWRS#XQA9AAC7E4R).

<br/><br/>
## CloudFormation Resources

| Logical ID                                                                                                                                 | Type     |
| ------------------------------------------------------------------------------------------------------------------------------------ | -------- |
| [AnalyticsApplication](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html)   | AWS::KinesisAnalyticsV2::Application |
| [AnalyticsServiceExecutionRole](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html)   | AWS::IAM::Role |
| [AthenaWorkgroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html)   | AWS::Athena::WorkGroup |
| [FirehoseServiceExecutionRole	](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html)   | AWS::IAM::Role |
| [FirehoseStream](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html)   | AWS::KinesisFirehose::DeliveryStream |
| [GlueDatabase](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-database.html)   | AWS::Glue::Database |
| [GlueTable](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-table.html)   | AWS::Glue::Table |
| [InputStream](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-stream.html)   | AWS::Kinesis::Stream |
| [OutputStream](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-stream.html)   | AWS::Kinesis::Stream |
| [S3Logs](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html)   | AWS::S3::Bucket |


<br />
