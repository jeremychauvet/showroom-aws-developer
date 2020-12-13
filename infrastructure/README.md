## Requirements

No requirements.

## Providers

| Name | Version |
|------|---------|
| aws | n/a |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| sqs\_delay\_seconds | If you create a delay queue, any messages that you send to the queue remain invisible to consumers for the duration of the delay period. The default (minimum) delay for a queue is 0 seconds. The maximum is 15 minutes. | `number` | `0` | no |
| sqs\_max\_message\_size | Maximum message size allow in queue | `number` | `2048` | no |
| sqs\_message\_retention\_seconds | Amazon SQS automatically deletes messages that have been in a queue for more than maximum message retention period. The default message retention period is 4 days. The maximum is 14 days. | `number` | `86400` | no |
| tags | n/a | `map(string)` | <pre>{<br>  "CreatedBy": "Terraform",<br>  "Project": "MyOnlineBookStore"<br>}</pre> | no |

## Outputs

No output.
