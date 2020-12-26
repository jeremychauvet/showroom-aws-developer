import json


def order(event, context):
    print("[INFO] Event : " + str(event))

    if event.body.credit_score.score:
        print("[DEBUG] Credit score : " + event.credit_score.score)
