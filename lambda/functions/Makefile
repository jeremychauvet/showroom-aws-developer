.PHONY: deploy validate
INSTALL_CMD=python3 -m pip install -r requirements.txt

deploy:
	serverless deploy
	@rm -fr ./.serverless/*.zip

validate:
	pre-commit run --all-files

# Function order

.PHONY: install-order test-order

install-order:
	cd order && $(INSTALL_CMD)

test-order: install-order
	serverless invoke local --function order --path order/test/accepted_order_payload.json
	serverless invoke local --function order --path order/test/rejected_order_payload.json

# Function displayBook

.PHONY: install-display-book test-display-book

install-display-book:
	cd book/display && $(INSTALL_CMD)

test-display-book: install-display-book
	serverless invoke local --function display_book
