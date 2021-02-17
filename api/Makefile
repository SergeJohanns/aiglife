.Phony: build
build:
	docker build -t api .

.Phony: run
run: stop build
	docker run --name api -p 5000:5000 api

.Phony: stop
stop:
	docker stop api || true
	docker container rm api || true