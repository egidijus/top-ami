
.DEFAULT_GOAL := go

SHELL := /usr/bin/env bash
# BUILD_DATE := $(shell date -u +%Y-%m-%d-%H%M)

EXECUTABLES = virtualenv python3 pip jq

thepackages := $(foreach exec,$(EXECUTABLES),\
        $(if $(shell which $(exec)),some string,$(error "Mate, I cannot find " $(exec) " in PATH, either intstall $(exec) or update your paths")))

export


# directory where python3 venv will live
directory = ./venv

# create venv if venv not present
python_bootstrap: | $(directory)
	@echo "Installing venv and python packages"
	source ./venv/bin/activate; \
	pip install -r pip-requirements.txt

$(directory):
	@echo "Folder $(directory) does not exist"
	virtualenv -p python3 $@

run:
	source ./venv/bin/activate; \
	python top-ami.py

go: python_bootstrap run

