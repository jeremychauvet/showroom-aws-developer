# Insert fake book data in queue

This function insert fake datas in SQS queue "book".

## Prerequisites

* You must create a "default" [named profile](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html).
* You must install [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html).
* Python 3

## How to run

At project root, please run `make insert-fake-books-in-queue`.

## Output example

```bash
{
  "book": {
    "isbn": "978-0-85035-680-9",
    "title": "Try indicate each marriage actually at.",
    "author": "Justin Gonzalez",
    "stock": 0
  }
}
```
