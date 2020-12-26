.PHONY: deploy validate test-order

deploy:
	serverless deploy

validate:
	pre-commit run --all-files

test-order:
	serverless invoke local --function order
