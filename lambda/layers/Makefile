.PHONY: build aws-xray-sdk
LAYERS_PATH=./
TMP_PATH=$(LAYERS_PATH)/tmp
OUTPUT_PATH=$(LAYERS_PATH)/output

build: aws-xray-sdk

# AWS SDK SDK
ARTIFACT_NAME=aws-xray-sdk.zip
aws-xray-sdk:
	rm -f $(LAYERS_PATH)/$(ARTIFACT_NAME) || true
	mkdir -p $(TMP_PATH) && mkdir -p $(OUTPUT_PATH)/python
	pip install --upgrade --target $(TMP_PATH) aws-xray-sdk
	mv $(TMP_PATH)/* $(OUTPUT_PATH)/python
	cd $(OUTPUT_PATH) && zip -r $(ARTIFACT_NAME) python/ && mv $(ARTIFACT_NAME) ../$(ARTIFACT_NAME) && cd -
	rm -fr $(TMP_PATH)
	rm -fr $(OUTPUT_PATH)
