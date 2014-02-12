detailedResume = 'Arvind_Pereira_CV_Detailed.tex'
plainResume = 'arvind_pereira.tex'
shortResume = 'Arvind_Pereira_CV.tex'

compileTex = './compileTex.sh'


all: PlainResume DetailedResume ShortResume

PlainResume:
	$(compileTex) $(plainResume)

DetailedResume:
	$(compileTex) $(detailedResume)
	
ShortResume:
	$(compileTex) $(shortResume)

clean:
	rm *.aux *.out *.pdf *.log *.blg *.bbl
