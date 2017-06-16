help:
	@echo "Some notes as to run this stuff"
	@echo "deploy-dev    - deploy the dev environment"


deploy-dev:
	@zappa deploy dev

run-local:
	@env/bin/python app.py

unit-test:
	@env/bin/nosetests

api-curl:
	curl 'https://api.api.ai/api/query?v=20150910&query=turn%20the%20heating%20on&lang=en&sessionId=7905137b-d087-4526-af12-794649c98607&timezone=2017-06-16T01:02:54+0200' -H 'Authorization:Bearer 9c0cd6521d8045c5816f8509a30ec195'
