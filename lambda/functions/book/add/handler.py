import json
import sys
import boto3
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

patch_all()


@xray_recorder.capture("# Add a book to library")
def add_book(event, context):

    # Can be set as environment variable or retrieve via SSM.
    aws_region = "eu-central-1"
    dynamodb_table_name = "Book"

    try:
        # Convert string to JSON.
        body = json.loads(event["Records"][0]["body"])

        # Check if mandatory data are defined in payload.
        isbn = body["book"]["isbn"]
        title = body["book"]["title"]
        author = body["book"]["author"]
        stock = body["book"]["stock"]

        # # Load AWS SDK client for DynamoDB.
        client = boto3.resource("dynamodb", region=aws_region)
        table = client.Table(dynamodb_table_name)

        # Insert data in table.
        response = table.put_item(
            Item={
                "ISBN": isbn,
                "BookTitle": title,
                "BookAuthor": author,
                "BookStock": stock,
            }
        )

        print(response)

    except KeyError as e:
        print("[ERROR] The following key is not existing in payload : " + str(e))

    except:
        print("[ERROR] " + str(sys.exc_info()[1]))
