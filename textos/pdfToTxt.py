# importing required modules 
from pypdf import PdfReader

y="inferno"

# pdffileobj=open("c:/Users/Tadeu/Repos/Github/kla_br/textos/" + y + '.pdf','rb')

# #create reader variable that will read the pdffileobj
# pdfreader=PdfReader(pdffileobj)

# #This will store the number of pages of this pdf file
# x=len(pdfreader.pages)

# for i in range(x):
# #create a variable that will select the selected number of pages
#     pageobj=pdfreader.pages[i]
#     # print(i)
# #(x+1) because python indentation starts with 0.
# #create text variable which will store all text datafrom pdf file
#     # text + " "
#     file1=open(r"c:/Users/Tadeu/Repos/Github/kla_br/textos/" + y + '.txt',"a")
#     # print(" " + pageobj.extractText())
#     file1.write((" " + pageobj.extract_text()).replace("á", "´a").replace("é", "´e").replace("í", "´i").replace("ó","´o").replace("ú", "´u")
#                     .replace("Á", "´A").replace("É", "´E").replace("Í", "´I").replace("Ó", "´O").replace("Ú", "´U")
#                     .replace("à", "`a").replace("è", "`e").replace("ì", "`i").replace("ò", "`o").replace("ù", "`u")
#                     .replace("À", "`A").replace("È", "`E").replace("Ì", "`I").replace("Ò", "`O").replace("Ù", "`U")
#                     .replace("ã", "~a").replace("õ", "~o").replace("Ã", "~A").replace("Õ", "~O")
#                     .replace("â", "^a").replace("ê", "^e").replace("î", "^i").replace("ô", "^o").replace("û", "^u")
#                     .replace("Â", "^A").replace("Ê", "^E").replace("Î", "^I").replace("Ô", "^O").replace("Û", "^U")
#                     .replace("ä", "¨a").replace("ë", "¨e").replace("ï", "¨i").replace("ö", "¨o").replace("ü", "¨u")
#                     .replace("Ä", "¨A").replace("Ë", "¨E").replace("Ï", "¨I").replace("Ö", "¨O").replace("Ü", "¨U")
#                     )



file="c:/Users/Tadeu/Repos/Github/kla_br/textos/" + y + '.txt'
file1=open(r"c:/Users/Tadeu/Repos/Github/kla_br/textos/" + y + '1.txt',"a")
with open(file, encoding='utf8') as f:
    lines = f.read()
# print(" " + pageobj.extractText())
    file1.write(lines.replace("á", "´a").replace("é", "´e").replace("í", "´i").replace("ó","´o").replace("ú", "´u")
                    .replace("Á", "´A").replace("É", "´E").replace("Í", "´I").replace("Ó", "´O").replace("Ú", "´U")
                    .replace("à", "`a").replace("è", "`e").replace("ì", "`i").replace("ò", "`o").replace("ù", "`u")
                    .replace("À", "`A").replace("È", "`E").replace("Ì", "`I").replace("Ò", "`O").replace("Ù", "`U")
                    .replace("ã", "~a").replace("õ", "~o").replace("Ã", "~A").replace("Õ", "~O")
                    .replace("â", "^a").replace("ê", "^e").replace("î", "^i").replace("ô", "^o").replace("û", "^u")
                    .replace("Â", "^A").replace("Ê", "^E").replace("Î", "^I").replace("Ô", "^O").replace("Û", "^U")
                    .replace("ä", "¨a").replace("ë", "¨e").replace("ï", "¨i").replace("ö", "¨o").replace("ü", "¨u")
                    .replace("Ä", "¨A").replace("Ë", "¨E").replace("Ï", "¨I").replace("Ö", "¨O").replace("Ü", "¨U")
                        )
