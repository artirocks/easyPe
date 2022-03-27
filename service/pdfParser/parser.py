# importing required modules 
import PyPDF2
import regex as re
    
# creating a pdf file object 
pdfFileObj = open('/content/drive/MyDrive/BharatBillPay/My_Invoice.pdf', 'rb') 
    
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    
# printing number of pages in pdf file 


# creating a page object 
pageObj = pdfReader.getPage(0) 
    
# extracting text from page 
extractedText = pageObj.extractText()
    
# closing the pdf file object 
pdfFileObj.close()

spaceAdded = ''
spaceAdded += extractedText[0]

for i in range(1, len(extractedText)):

  if (extractedText[i-1].isdigit() and extractedText[i].isdigit())==False and (extractedText[i-1].isdigit() or extractedText[i].isdigit())==True:
    spaceAdded += extractedText[i-1] + ' ' + extractedText[i]
  
  else:
    spaceAdded += extractedText[i]
  
spaceAdded = spaceAdded.replace('  ', ' ')

listText = spaceAdded.split()


print(listText)


for i in listText:
  print(i)