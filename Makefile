.PHONY: serve
serve:
	docker build ./ -t gtfobins
	docker run \
	    --rm \
	    --name gtfobins \
	    --user "${UID}" \
	    --publish 4000:4000 \
	    --volume "${PWD}:/site/" \
	    gtfobins \
	    bundle exec jekyll serve --host 0.0.0.0

.PHONY: lint
lint:
	linter/linter.py
