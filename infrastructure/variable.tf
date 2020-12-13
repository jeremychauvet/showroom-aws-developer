variable "sqs_delay_seconds" {
  description = "If you create a delay queue, any messages that you send to the queue remain invisible to consumers for the duration of the delay period. The default (minimum) delay for a queue is 0 seconds. The maximum is 15 minutes."
  type        = number
  default     = 0
}

variable "sqs_max_message_size" {
  description = "Maximum message size allow in queue"
  type        = number
  default     = 2048
}

variable "sqs_message_retention_seconds" {
  description = "Amazon SQS automatically deletes messages that have been in a queue for more than maximum message retention period. The default message retention period is 4 days. The maximum is 14 days."
  type        = number
  default     = 86400
}

variable "tags" {
  type = map(string)
  default = {
    Project   = "MyOnlineBookStore"
    CreatedBy = "Terraform"
  }
}
