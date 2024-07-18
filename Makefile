.PHONY: serve
serve:
	docker build ./ -t gtfobins
	docker run \
	    --rm \
	    --name gtfobins \
	    --user "$$UID" \
	    --publish 4000:4000 \
	    --volume "$$PWD:/GTFOBins/" \
	    gtfobins \
	    bundle exec jekyll serve --host 0.0.0.0

.PHONY: lint
lint:
	@python3 -m venv ./linter/.venv/
	@PIP_USER= . ./linter/.venv/bin/activate \
	    && pip install --quiet --upgrade pip \
	    && pip install --quiet -r ./linter/requirements.txt \
	    && ./linter/linter.py

.PHONY: clean
clean:
	-docker rmi gtfobins
	-rm -fr ./linter/venv/
