import json
import sys


def order(event, context):
    try:
        # Deal with JSON formatted with single quote instead of double quotes.
        event = event.replace("'", '"')
        # Convert string to JSON.
        body = json.loads(event["Records"][0]["body"])
        # If credit score superior or equal to 660, order is accepted.
        if int(body["credit_score"]["score"]) >= 660:
            print("[INFO] Order accepted")
        else:
            print(
                "[INFO] Order rejected : credit score under 660 (actual : "
                + body["credit_score"]["score"]
                + ")."
            )

    except:
        print("[ERROR] " + str(sys.exc_info()[1]))
