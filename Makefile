.PHONY: serve serve-public bundle

serve:
	bundle exec jekyll serve

serve-public:
	bundle exec jekyll serve --host 0.0.0.0

bundle:
	bundle install
