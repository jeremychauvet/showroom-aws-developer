# aws-developer-showroom

This repository is a showroom to demonstrate how AWS can solve developements issues, with services like Lambda, SQS, DynamoDB or Api Gateway.

## Automation

![CodeQL](https://github.com/jeremychauvet/aws-developer-showroom/workflows/CodeQL/badge.svg?branch=main)

## Context

To be realistic, we have set a business context for this showroom. Our client is a leader in online book selling. We call it "MyOnlineBookStore".

## Architecture

This project is based on a serverless architecture. This design is also event driven.

![architecture](./docs/MyOnlineBookStore_architecture.png "Architecture")

### Back-office

* Lambda are used as compute power.
  * Language : Python 3.8
  * Framework : Serverless
* DynamoDB is used as database.

### Front-office

* VueJS app

## Development advice

We recommand to use [pyright](https://github.com/microsoft/pyright) extension for VSCode.
This plugin use file pyrightconfig.json at projet root, feel free to adjust it to your needs.

## Special thanks

* [Fernando Medina Corey](https://github.com/fernando-mc) for his [code](https://github.com/fernando-mc/aws-http-api-python-cognito) on Cognito
* [Mark Wolfe](https://github.com/wolfeidau) for this [code](https://github.com/wolfeidau/cognito-vue-bootstrap) about Cognito authentication with VueJS.
