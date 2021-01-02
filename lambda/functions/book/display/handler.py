import sys
import os
import boto3
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

patch_all()


@xray_recorder.capture("# Display books available in library")
def display_book(event, context):

    # Get lambda parameters from environment variables defined in severless.yml.
    aws_region = os.getenv("AWS_REGION_NAME")
    dynamodb_table_name = os.getenv("DYNAMODB_TABLE_NAME")

    try:
        # Load AWS SDK client for DynamoDB.
        client = boto3.resource("dynamodb", region_name=aws_region)
        table = client.Table(dynamodb_table_name)

        response = table.scan()

        print(response)

    except:
        print("[ERROR] " + str(sys.exc_info()[1]))
