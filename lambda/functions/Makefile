.PHONY: deploy validate
INSTALL_CMD=pip3 install -r requirements.txt

deploy:
	serverless deploy

validate:
	pre-commit run --all-files

# Function order

.PHONY: install-order test-order

install-order:
	cd order && $(INSTALL_CMD)

test-order: install-order
	serverless invoke local --function order --path order/test/accepted_order_payload.json
	serverless invoke local --function order --path order/test/rejected_order_payload.json
