# Function order

## Description

This function is invoke when a customer buy a book. It validate customer data (no empty data for example), and put it in DynamoDB table.
By validating customer data, we talk about credit score. This must be equal or greater to 720 to order a book on our platform.

## Parameters

| Parameter         | Type   | Example               |
|-------------------|--------|-----------------------|
| customerFirstName | String | Victor                |
| customerLastName  | String | Hugo                  |
| customerEmail     | String | victor.hugo@gmail.com |
| basket            | Map    | {}                    |

## Output

TODO

## How to test

TODO
