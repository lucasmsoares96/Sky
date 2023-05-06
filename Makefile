run:
	python -m sky input.sky
	
init:
	python3 -m venv .venv
	. ./.venv/bin/activate && \
	pip install -r requirements.txt
	
clean:
	git clean -n
	git clean -Xdf
	
cache_clean:
	git rm --cached -r .
	
antlr:
	antlr4 -Dlanguage=Python3 ./sky/Sky.g4 -visitor -o ./sky/antlr/
	cp ./sky/antlr/sky/* ./sky/antlr/
	rm -rf ./sky/antlr/sky
	
antlr_clean:
	rm -rf ./sky/antlr
	mkdir ./sky/antlr
	touch ./sky/antlr/__init__.py