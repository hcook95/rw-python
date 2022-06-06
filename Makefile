SHELL := /bin/bash

.PHONY: setup
setup:
	cd setup; source setup.sh

clean:
	rm -rf *.log *.jou checkpoints/*.log checkpoints/*.jou checkpoints/.Xil hd_visual .Xil .vscode
	rm -rf routeThrus data venv activate rapidwright-2022.1.1-standalone-lin64.jar