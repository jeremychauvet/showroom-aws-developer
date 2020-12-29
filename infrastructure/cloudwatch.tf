ressource "aws_cloudwatch_dashboard" "default" {
  dashboard_name = "CloudWatch-Default"
  dashboard_body = file("./files/cloudwatch/CloudWatch-Default.json")
}
