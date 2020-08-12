import boto3
import calendar
import time

client = boto3.client(
    'quicksight',
    region_name= <region>
)

for i in client.list_data_sets(AwsAccountId= <YourAWSAccount> )["DataSetSummaries"]:
    if i["Name"] == <Dataset Name>:
        print(i["DataSetId"])
        ID_ = i["DataSetId"]

#to create unique number
ingestionID = calendar.timegm(time.gmtime())

while True:
  response = client.create_ingestion(
      DataSetId= ID_,
      IngestionId=str(ingestionID),
      AwsAccountId=<YourAWSAccount>
  )
  time.sleep(<Refresh Interval>)
