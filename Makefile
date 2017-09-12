.PHONY: setup
setup:
	virtualenv -p python3 venv
	source venv/bin/activate && pip install -r requirements.txt
	npm install

.PHONY: migrations
migrations:
	./manage.py makemigrations

.PHONY: db
db: migrations
	./manage.py migrate

.PHONY: local
local: db
	./manage.py runserver

.PHONY: super
super: db
	./manage.py createsuperuser

.PHONY: js
js:
	npm run build-js

.PHONY: css
css:
	npm run build-css

.PHONY: static
static: js css
