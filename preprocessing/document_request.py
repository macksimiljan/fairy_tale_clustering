from lxml import html
import requests

class DocumentRequest(object):
	
	def __init__(self, url):
		if len(url) < 1:
			raise ValueError('URL cannot be empty!')
		self.url = url

	def start_request(self):
		page = requests.get(self.url)
		self.tree = html.fromstring(page.content)

	def get_headline(self):
		headlines = self.tree.xpath("//div[@id = 'gutenb']/h3/text()")
		if len(headlines) != 1:
			raise RuntimeError('There are',len(headlines),'headlines instead of one!')
		return headlines[0].strip()

	def get_paragraphs(self):
		paragraphs = self.tree.xpath("//div[@id = 'gutenb']/p/text()")
		cleaned_paragraphs = []
		for p in paragraphs:
			p = p.strip()
			if len(p) > 0:
				cleaned_paragraphs.append(p)
		return cleaned_paragraphs

# tags in tags werden nicht übernommen.

r = DocumentRequest('http://gutenberg.spiegel.de/buch/kinder-und-hausmarchen-7018/5')
r.start_request()
print('headline:',r.get_headline())
paragraphs = r.get_paragraphs()
for p in paragraphs:
	print('paragraph:',p)



