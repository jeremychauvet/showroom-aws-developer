import json
import sys
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

patch_all()


@xray_recorder.capture('# Validate order')
def order(event, context):
    try:
        subsegment = xray_recorder.begin_subsegment('annotations')
        # Convert string to JSON.
        body = json.loads(event["Records"][0]["body"])
        credit_score = int(body["credit_score"]["score"])
        # If credit score superior or equal to 660, order is accepted.
        if credit_score >= 660:
            print("[INFO] Order accepted")
            subsegment.put_annotation('order_status', 'accepted')
            subsegment.put_annotation('credit_score', credit_score)
        else:
            print(
                "[INFO] Order rejected : credit score under 660 (actual : "
                + credit_score
                + ")."
            )
            subsegment.put_annotation('order_status', 'rejected')
            subsegment.put_annotation('credit_score', credit_score)
        xray_recorder.end_subsegment()

    except:
        print("[ERROR] " + str(sys.exc_info()[1]))
