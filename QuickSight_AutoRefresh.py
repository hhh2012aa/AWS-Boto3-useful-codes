import boto3
import calendar
import time
import datetime


#-----------------  Input your custom value in "<>" before running -----------

client = boto3.client(
    'quicksight',
    region_name= <Region>
)

for i in client.list_data_sets(AwsAccountId= <AWS ACCOUNT>)["DataSetSummaries"]:
    if i["Name"] == <Dataset Name>:
        ID_ = i["DataSetId"]

while True:
    ingestionID = calendar.timegm(time.gmtime())
    print("Refresh Date:", datetime.datetime.now())
    response = client.create_ingestion(
        DataSetId= ID_,
        IngestionId=str(ingestionID),
        AwsAccountId= <AWS ACCOUNT>
    )
    time.sleep(80)
