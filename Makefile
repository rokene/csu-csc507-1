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

MODULE6=$(CURRENT_DIR)/module-6
MODULE6_CRITICAL_THINKING=$(MODULE6)/critical-thinking

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

.PHONY: m4p
m4p: ## executes module 4 portfolio milestone
	@echo "executing module 4 portfolio milestone ..."
	@echo "cleaning up old data files"
	@cd $(MODULE4_MILESTONE) && rm *.txt
	@echo "generating base numbers files"
	@cd $(MODULE4_MILESTONE) && ./numbers.sh
	@cd $(MODULE4_MILESTONE) && ./numbers.py
	@echo "doubling numbers"
	@cd $(MODULE4_MILESTONE) && ./double_numbers.sh
	@echo "doubling numbers using python 3 diff methods"
	@cd $(MODULE4_MILESTONE) && ./double_numbers.py
	@echo "completed module 4 portfolio milestone."

.PHONY: m6
m6: ## executes module 6 critical thinking
	@echo "executing module 6 critical thinking ..."
	@cd $(MODULE6_CRITICAL_THINKING) && \
		rm *.txt*; \
		./numbers.py && \
		./analysis.py
	@echo "completed module 6 critical thinking."

.PHONY: pp
pp: ## executes portfolio project
	@echo "pp: starting portfolio project"
	@cd $(PP) && \
		echo "pp: clean up" && \
		rm *.txt && \
		echo "pp: starting analysis" && \
		./generate_data.py && \
		./analysis.py
	@echo "pp: completed portfolio project"
