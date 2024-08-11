.DEFAULT_GOAL := help

CURRENT_DIR := $(CURDIR)

MODULE1=$(CURRENT_DIR)/module-1
MODULE1_CRITICAL_THINKING=$(MODULE1)/critical-thinking

MODULE2=$(CURRENT_DIR)/module-2
MODULE2_MILESTONE=$(MODULE2)/milestone

MODULE3=$(CURRENT_DIR)/module-3
MODULE3_MILESTONE=$(MODULE3)/milestone

MODULE4=$(CURRENT_DIR)/module-4
MODULE4_CRITICAL_THINKING=$(MODULE4)/critical-thinking
MODULE4_MILESTONE=$(MODULE4)/milestone

PP=$(CURRENT_DIR)/portfolio-project

.PHONY: help
help:
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*' $(MAKEFILE_LIST) | sort

.PHONY: m1
m1: ## executes module 1 critical thinking
	@echo "executing module 1 critical thinking ..."
	@cd $(MODULE1_CRITICAL_THINKING) && ./machine-info.sh
	@echo "completed module 1 critical thinking."

.PHONY: m2p
m2p: ## executes module 2 portfolio milestone
	@echo "executing module 2 portfolio milestone ..."
	@cd $(MODULE2_MILESTONE) && ./numbers.sh
	@echo "completed module 2 portfolio milestone."

.PHONY: m3p
m3p: ## executes module 3 portfolio milestone
	@echo "executing module 3 portfolio milestone ..."
	@cd $(MODULE3_MILESTONE) && ./numbers.sh
	@echo "executing python variant"
	@cd $(MODULE3_MILESTONE) && ./numbers.py
	@cd $(MODULE3_MILESTONE) && ./numbers-mp.py
	@echo "completed module 3 portfolio milestone."

.PHONY: m4
m4: ## executes module 4 critical thinking
	@echo "executing module 4 critical thinking ..."
	@cd $(MODULE4_CRITICAL_THINKING) && ./first_fit.py
	@echo "completed module 4 critical thinking."
