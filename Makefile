deps:
	serverless --version || (echo -e "ERROR: please install serverless framework" && false)
	serverless plugin install -n serverless-google-cloudrun
	make -C todo-api deps
	make -C todo-frontend deps
	@touch $@

run: deps
	make -C todo-api run &
	make -C todo-frontend run

clean:
	make -C todo-api clean
	make -C todo-frontend clean
	rm -rf deps

build: deps
	make -C todo-frontend build

deploy: build
	sls deploy
