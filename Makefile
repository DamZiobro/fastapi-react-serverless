deps:
	serverless --version || (echo -e "ERROR: please install serverless framework" && false)
	serverless plugin install -n serverless-google-cloudrun
	make -C pets-api deps
	make -C pets-frontend deps
	@touch $@

run: deps
	make -C pets-api run &
	make -C pets-frontend run

clean:
	make -C pets-api clean
	make -C pets-frontend clean
	rm -rf deps

build: deps
	make -C pets-frontend build

deploy: build
	sls deploy
