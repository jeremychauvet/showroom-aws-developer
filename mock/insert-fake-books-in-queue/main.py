#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-

import sys
import boto3
import json
from time import sleep
from faker import Faker

# This function insert fake datas in queue defined bellow.
client = boto3.client("sqs", region_name="eu-central-1")

# Variables.
QUEUE_NAME = "book"
NUMBER_OF_MESSAGES_TO_SEND = 10


def insert_messages_in_queue():
    try:
        get_queue_url_response = client.get_queue_url(QueueName=QUEUE_NAME)
        queue_url = get_queue_url_response["QueueUrl"]

        # Import library to insert fake datas.
        fake = Faker()

        for message_number in range(NUMBER_OF_MESSAGES_TO_SEND):
            payload = {
                "book": {
                    "isbn": str(fake.isbn13()),
                    "title": str(fake.sentence(nb_words=5)),
                    "author": str(fake.name()),
                    "stock": 0,
                }
            }
            # Convert dictionnary in JSON.
            payload = json.dumps(payload)
            # Sent message to queue.
            send_message_response = client.send_message(
                QueueUrl=queue_url, MessageBody=payload
            )

            if send_message_response["ResponseMetadata"]["HTTPStatusCode"] == 200:
                print(
                    "[INFO] Message "
                    + str(message_number)
                    + " of "
                    + str(NUMBER_OF_MESSAGES_TO_SEND)
                    + " sent successfully."
                )
                sleep(2)
            else:
                print(
                    "[ERROR] Message not sent successfully. Output : "
                    + str(send_message_response)
                )
                sys.exit(1)

    except:
        print("[ERROR] " + str(sys.exc_info()[1]))


if __name__ == "__main__":
    insert_messages_in_queue()
