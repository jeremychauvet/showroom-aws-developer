import json
import sys
import boto3
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

patch_all()


@xray_recorder.capture("# Add a book to library")
def add_book(event, context):

    # Can be set as environment variable or retrieve via SSM.
    aws_region          = "eu-central-1"
    dynamodb_table_name = "Book"

    try:
        # Convert string to JSON.
        body = json.loads(event["Records"][0]["body"]["book"])

        # Check if mandatory data are defined in payload.
        isbn = is_defined("ISBN", body['isbn'])
        title = is_defined("book title", body['isbn'])
        author = is_defined("book author", body['author'])
        stock = is_defined("book stock", body['stock'])

        # Load AWS SDK client for DynamoDB.
        client = boto3.resource('dynamodb', region=aws_region)
        table = client.Table(dynamodb_table_name)

        # Insert data in table.
        response = table.put_item(
            Item={
                'ISBN': isbn,
                'BookTitle': title,
                'BookAuthor': author,
                'BookStock': stock
            }
        )

        print(response)

    except:
        print("[ERROR] " + str(sys.exc_info()[1]))

def is_defined(item, value) -> str:
    try:
        print("Validading if " + item + " is set.")
        return value
    except:
        print("[ERROR] " + item + " is not defined in payload.")
        sys.exit(-1)
