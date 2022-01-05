for i in {1..2}
do
pdflatex report 
done
rm -r *.aux *.bbl *.blg *.log *.out
