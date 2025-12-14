MAKEFLAGS += --always-make

NAME := gtfobins
PORT := 4000

serve:
	@echo '# Building the Docker image'
	@docker build ./ -t "$(NAME)"
	@echo '# Building and serving the website'
	@docker run \
		--rm \
		--name "$(NAME)" \
		--publish "$(PORT):$(PORT)" \
		--volume "$$PWD/:/GTFOBins/" \
		"$(NAME)"

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
	@docker kill "$(NAME)" &>/dev/null || true
	@docker rmi "$(NAME)" &>/dev/null || true
	@echo '# Cleaning up filesystem'
	@rm -fr ./linter/.venv/
	@rm -fr ./_site/
