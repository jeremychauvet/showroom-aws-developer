import sys
import os
import json
import boto3
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

patch_all()
subsegment = xray_recorder.begin_subsegment("annotations")


@xray_recorder.capture("# Display books available in library")
def display_book(event, context):

    # Get lambda parameters from environment variables defined in severless.yml.
    aws_region = os.getenv("AWS_REGION_NAME")
    dynamodb_table_name = os.getenv("DYNAMODB_TABLE_NAME")

    try:
        # Load AWS SDK client for DynamoDB.
        subsegment.put_annotation("[INFO]", "Init DynamoDB client")
        client = boto3.resource("dynamodb", region_name=aws_region)
        table = client.Table(dynamodb_table_name)

        subsegment.put_annotation("[INFO]", "Starting table scan")
        # Get temporary all items with a scan, bad for performance, but development related.
        response = table.scan()
        return {
            "isBase64Encoded": False,
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,GET",
            },
            "body": json.dumps(response["Items"]),
        }

    except:
        print("[ERROR] " + str(sys.exc_info()[1]))
