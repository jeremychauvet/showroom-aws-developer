.PHONY: ci clean build deploy install

ci: clean build deploy

clean:
	rm -rf dist

install:
	yarn install

build: install
	yarn build

deploy:
	aws s3 sync dist/ s3://$(S3_HOSTING_BUCKET)/ --delete --acl public-read
	aws cloudfront create-invalidation --distribution-id $(DISTRIBUTION_ID) --paths '/*'
