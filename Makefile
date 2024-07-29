.DEFAULT_GOAL := help

CURRENT_DIR := $(CURDIR)

MODULE1=$(CURRENT_DIR)/module-1
MODULE1_CRITICAL_THINKING=$(MODULE1)/critical-thinking

MODULE2=$(CURRENT_DIR)/module-2
MODULE2_MILESTONE=$(MODULE2)/milestone

MODULE3=$(CURRENT_DIR)/module-3
MODULE3_CRITICAL_THINKING=$(MODULE3)/critical-thinking

MODULE5=$(CURRENT_DIR)/module-5
MODULE5_CRITICAL_THINKING=$(MODULE5)/critical-thinking

MODULE7=$(CURRENT_DIR)/module-7
MODULE7_CRITICAL_THINKING=$(MODULE7)/critical-thinking

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

# .PHONY: m3
# m3: ## executes module 3 critical thinking
# 	@echo "executing module 3 critical thinking ..."
# 	@cd $(MODULE3_CRITICAL_THINKING); ./app.py
# 	@echo "completed module 3 critical thinking."

# .PHONY: m5
# m5: ## executes module 5 critical thinking
# 	@echo "executing module 5 critical thinking ..."
# 	@cd $(MODULE5_CRITICAL_THINKING); ./app.py
# 	@echo "completed module 5 critical thinking."

# .PHONY: m7
# m7: ## executes module 7 critical thinking
# 	@echo "executing module 7 critical thinking ..."
# 	@cd $(MODULE7_CRITICAL_THINKING); ./app.py
# 	@echo "completed module 7 critical thinking."

# .PHONY: pp
# pp: ## executes portfolio project
# 	@echo "executing portfolio project ..."
# 	@cd $(PP); ./app.py
# 	@echo "completed portfolio project."
