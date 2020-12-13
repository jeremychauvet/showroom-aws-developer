resource "aws_sqs_queue" "order" {
  name                      = "order.fifo"
  fifo_queue                = true
  delay_seconds             = var.sqs_delay_seconds
  max_message_size          = var.sqs_max_message_size
  message_retention_seconds = var.sqs_message_retention_seconds

  redrive_policy = jsonencode({
    deadLetterTargetArn = aws_sqs_queue.order-dlq.arn
    maxReceiveCount     = 4
  })

  kms_master_key_id                 = "alias/aws/sqs"
  kms_data_key_reuse_period_seconds = 300

  tags = var.tags
}

resource "aws_sqs_queue" "order-dlq" {
  name                      = "order-dlq.fifo"
  fifo_queue                = true
  delay_seconds             = var.sqs_delay_seconds
  max_message_size          = var.sqs_max_message_size
  message_retention_seconds = var.sqs_message_retention_seconds

  kms_master_key_id                 = "alias/aws/sqs"
  kms_data_key_reuse_period_seconds = 300

  tags = var.tags
}
