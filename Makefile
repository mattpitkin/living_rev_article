# make file to automate all the annoying commands

default: ps

ps: updated_article.tex refs.bib
	latex updated_article
        # ignore the exit status of bibtex by adding a hyphen
	- bibtex updated_article
	latex updated_article
	latex updated_article
	dvips updated_article.dvi
	ps2pdf updated_article.ps
	
clean:
	@echo "Cleaning directory of backups and logs"
	rm -f *~ *.log *.aux *.dvi *.out *.bbl *.blg
	
