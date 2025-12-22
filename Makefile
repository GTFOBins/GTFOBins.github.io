NAME := gtfobins
PORT := 4000

.PHONY: serve
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

.PHONY: vet
vet: ./linter/.venv/
	@echo '# Running linter'
	@. ./linter/.venv/bin/activate && python -m linter --check-only
	@echo '# All good!'

.PHONY: format
format: ./linter/.venv/
	@if [ "$$(git ls-files --modified --others --exclude-standard)" ]; then \
		echo '# Stage your changes first'; \
		false; \
	fi
	@echo '# Running linter'
	@. ./linter/.venv/bin/activate && python -m linter
	@echo '# All good!'

.PHONY: clean
clean:
	@echo '# Cleaning up Docker'
	@docker kill "$(NAME)" &>/dev/null || true
	@docker rmi "$(NAME)" &>/dev/null || true
	@echo '# Cleaning up the filesystem'
	@rm -fr ./linter/.venv/
	@rm -fr ./_site/

./linter/.venv/:
	@echo '# Setting up the virtual environment'
	@python3 -m venv ./linter/.venv/
	@echo '# Installing dependencies'
	@. ./linter/.venv/bin/activate \
		&& PIP_USER= pip install --quiet --upgrade pip -r ./linter/requirements.txt
