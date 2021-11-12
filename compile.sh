#!/usr/bin/env bash

TARGET="${1}"
#poster.tex
WHITELIST="
	article.tex
	"

if [[ "$TARGET" = "all" ]] || [[ "$TARGET" == "" ]]; then
	for ITER_TARGET in *.tex; do
		if [[ $WHITELIST =~ (^|[[:space:]])$ITER_TARGET($|[[:space:]]) ]];then
			ITER_TARGET=${ITER_TARGET%".tex"}
			./compile.sh "${ITER_TARGET}"
		fi
	done
else
	pdflatex -shell-escape "${TARGET}.tex" || { echo "Initial pdflatex failed"; exit $ERRCODE; }
	pythontex "${TARGET}.tex" || { echo "PythonTeX failed"; exit $ERRCODE; }
	pdflatex -shell-escape "${TARGET}.tex" || { echo "pdflatex failed after PythonTeX"; exit $ERRCODE; }
	bibtex "${TARGET}" || { echo "bibtex failed"; exit $ERRCODE; }
	pdflatex -shell-escape "${TARGET}.tex" || { echo "pdflatex failed after bibtex"; exit $ERRCODE; }
	pdflatex -shell-escape "${TARGET}.tex"

#  python scripts_/upload.py "$(pwd)/$(basename "${TARGET}.pdf")"
fi

