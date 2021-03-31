.PHONY: serve
serve:
	bundle exec jekyll serve

.PHONY: serve-publicly
serve-public:
	bundle exec jekyll serve --host 0.0.0.0

.PHONY: bundle
bundle:
	bundle install

.PHONY: lint
lint:
	linter/linter.py
