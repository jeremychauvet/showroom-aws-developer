import json
import sys
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

patch_all()


@xray_recorder.capture("# Display books available in library")
def display_book(event, context):
    try:
        # Mock.
        body = {
            "status": 200,
        }

        return json.dumps(body)

    except:
        print("[ERROR] " + str(sys.exc_info()[1]))
