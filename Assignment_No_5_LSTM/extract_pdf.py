import PyPDF2

pdf = PyPDF2.PdfReader('LAB ASSIGNMENT 5_ LSTM-Based AI Agent for Sequence Prediction (2).pdf')
text = ''
for page in pdf.pages:
    text += page.extract_text()
print(text)