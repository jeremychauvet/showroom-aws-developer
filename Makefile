.PHONY: init plan apply validate estimate-cost destroy docker

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

docker:
	docker-compose up -d --build
