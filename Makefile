# make file to automate all the annoying commands

default: authorea

ps: updated_article.tex bibliography/biblio.bib
	latex updated_article
        # ignore the exit status of bibtex by adding a hyphen
	- bibtex updated_article
	latex updated_article
	latex updated_article
	dvips updated_article.dvi
	ps2pdf updated_article.ps

authorea: abstract.tex acknowledgements.tex authors.tex header.tex posttitle.tex Section1.tex Section2.tex Section3.tex Section4.tex Section5.tex Section6.tex Section7.tex Section8.tex title.tex bibliography/biblio.bib
	rm -f *~ *.log *.aux *.dvi *.out *.bbl *.blg
	/home/matthew/repositories/authorea-scripts/local_build.py --build-dir /home/matthew/repositories/living_rev_article -f article.tex --relative-links --no-build /home/matthew/repositories/living_rev_article
	pdflatex article.tex
	- bibtex article
	pdflatex article.tex
	pdflatex article.tex

authorea_ps: abstract.tex acknowledgments.tex authors.tex header.tex posttitle.tex Section1.tex Section2.tex Section3.tex Section4.tex Section5.tex Section6.tex Section7.tex Section8.tex title.tex bibliography/biblio.bib
	rm -f *~ *.log *.aux *.dvi *.out *.bbl *.blg
	/home/matthew/repositories/authorea-scripts/local_build.py --build-dir /home/matthew/repositories/living_rev_article -f article.tex --relative-links --no-build /home/matthew/repositories/living_rev_article
	latex article.tex
	- bibtex article
	latex article.tex
	latex article.tex
	dvips article.dvi
	ps2pdf article.ps

clean:
	@echo "Cleaning directory of backups and logs"
	rm -f *~ *.log *.aux *.dvi *.out *.bbl *.blg
	
