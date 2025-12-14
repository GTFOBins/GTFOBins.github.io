MAKEFLAGS += --always-make

serve:
	@echo '# Building the Docker image'
	@docker build ./ -t gtfobins
	@echo '# Building and serving the website'
	@docker run \
		--rm \
		--name gtfobins \
		--user "$$UID" \
		--publish 4000:4000 \
		--volume "$$PWD:/GTFOBins/" \
		gtfobins \
		bundle exec jekyll serve --host 0.0.0.0

lint:
	@echo '# Setting up the virtual environment'
	@python3 -m venv ./linter/.venv/
	@echo '# Installing dependencies'
	@. ./linter/.venv/bin/activate && PIP_USER= pip install --quiet --upgrade pip -r ./linter/requirements.txt
	@echo '# Running linter'
	@. ./linter/.venv/bin/activate && ./linter/linter.py
	@echo '# All good!'

clean:
	@echo '# Cleaning up Docker'
	@docker kill gtfobins &>/dev/null || true
	@docker rmi gtfobins &>/dev/null || true
	@echo '# Cleaning up filesystem'
	@rm -fr ./linter/.venv/
	@rm -fr ./_site/
	@rm -fr ./.jekyll-cache/
