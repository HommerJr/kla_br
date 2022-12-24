# importing required modules 
import PyPDF2 

for y in range(17):    
    #create file object variable
    #opening method will be rb

    pdffileobj=open(str(y) + '.pdf','rb')
    
    #create reader variable that will read the pdffileobj
    pdfreader=PyPDF2.PdfFileReader(pdffileobj)
    
    #This will store the number of pages of this pdf file
    x=pdfreader.numPages

    text=""

    for i in range(x):
    #create a variable that will select the selected number of pages
        pageobj=pdfreader.getPage(i)
        # print(i)
    #(x+1) because python indentation starts with 0.
    #create text variable which will store all text datafrom pdf file
        # text + " "
        file1=open(r"texto para analise.txt","a")
        # print(" " + pageobj.extractText())
        file1.write(" " + pageobj.extractText())
