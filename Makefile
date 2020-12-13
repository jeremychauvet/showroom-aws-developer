.PHONY: init plan apply estimate-cost destroy validate

init:
	cd infrastructure && terraform init

plan:
	cd infrastructure && terraform plan

apply:
	cd infrastructure && terraform apply

validate:
	pre-commit run --all-files

estimate-cost:
	cd infrastructure && \
	terraform plan -out plan.save && \
	terraform show -json plan.save > plan.json && \
	infracost --tfjson ./plan.json

destroy:
	cd infrastructure && terraform destroy
