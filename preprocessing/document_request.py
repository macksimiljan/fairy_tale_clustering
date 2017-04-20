from lxml import html
import requests


class DocumentRequest(object):

    def __init__(self, url):
        if len(url) < 1:
            raise ValueError('URL cannot be empty!')
        self.url = url
        self.tree = self.start_request()

    def start_request(self):
        raise NotImplementedError("To be implemented!")

    def get_headline(self):
        raise NotImplementedError("To be implemented!")

    def get_text(self):
        raise NotImplementedError("To be implemented!")


class DocumentRequestGrimm(DocumentRequest):

    def start_request(self):
        page = requests.get(self.url)
        return html.fromstring(page.content)

    def get_headline(self):
        headlines = self.tree.xpath("//div[@id = 'gutenb']/h3/text()")
        if len(headlines) != 1:
            raise RuntimeError('There are',len(headlines),'headlines instead of one!')
        return headlines[0].strip()

    def get_text(self):
        paragraphs = self.__get_paragraphs()
        return ' '.join(paragraphs)

    def __get_paragraphs(self):
        paragraphs = self.tree.xpath("//div[@id = 'gutenb']/p/descendant-or-self::node()")
        cleaned_paragraphs = []
        for p in paragraphs:
            p = self.__preprocess_paragraph(p)
            if len(p) > 0:
                cleaned_paragraphs.append(p)
        return cleaned_paragraphs

    def __preprocess_paragraph(self, paragraph):
        paragraph = str(paragraph)
        paragraph = self.__eliminate_tags(paragraph)
        paragraph = paragraph.strip()
        paragraph = paragraph.replace('*', '')
        return paragraph

    def __eliminate_tags(self, paragraph):
        if paragraph.startswith('<') and paragraph.endswith('>'):
            return ''
        else:
            return paragraph
