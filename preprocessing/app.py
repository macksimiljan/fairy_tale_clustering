from preprocessing.document_request import DocumentRequest

r = DocumentRequest('http://gutenberg.spiegel.de/buch/kinder-und-hausmarchen-7018/5')
r.start_request()
print('headline:', r.get_headline())
print('text:', r.get_text())