deps:
	@nodejs --version &> /dev/null || (echo "ERROR: please install node.js")
	@npm --version &> /dev/null || (echo "ERROR: please install npm")
	@npx --version &> /dev/null || (echo "ERROR: please install npx" && false)
	@ls .env || (echo "ERROR: .env file does not exists - please see .env.example as the template")
	@npm install
	@touch $@

run: deps
	npm run dev

build: deps
	npm run build

clean: 
	rm -rf deps node_modules .next out build
