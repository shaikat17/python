# importing the modules
import PyPDF2, pyttsx3

# PDF file
path = open('your_PDF.pdf', 'rb')

# creating a PDF File Reader object
pdfReader = PyPDF2.PdfFileReader(path)

# Get an engine instance for the speech synthesis 
speak = pyttsx3.init()

for pages in range(pdfReader.numPages):
  text = pdfReader.getPage(pages).extractText()
  speak.say(text)
  speak.runAndWait()
  
 speak.stop()
