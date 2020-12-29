# Architecture Decision Record for Apis

## Status

Accepted - 28/12/20 - Jeremy Chauvet

## Context

Our backend is composed by a serie of Lambdas. As these Lambda will be consumed by an front office, they must be securely exposed. AWS managed Api Gateway is a solution that we will use, but we must choose between multiple types of API :

- REST API
- HTTP API

## Decision

HTTP APIs are optimized for serverless workloads and HTTP backends—they offer up to 71% cost savings and 60% latency reduction compared to REST APIs from API Gateway

We choose **HTTP API**
