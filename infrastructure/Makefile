.PHONY: init plan apply validate estimate-cost destroy

init:
	terraform init

plan: init
	terraform plan

apply:
	terraform apply

validate:
	pre-commit run --all-files

estimate-cost:
	terraform plan -out plan.save && \
	terraform show -json plan.save > plan.json && \
	infracost --tfjson ./plan.json

destroy:
	terraform destroy
