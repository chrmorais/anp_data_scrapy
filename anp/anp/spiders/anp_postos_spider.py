from scrapy.spider import Spider
from scrapy.http import FormRequest
from scrapy.selector import Selector

from anp.items import ANPItem

class ANPPostosSpider(Spider):
    name = "anp_postos"
    allowed_domains = ["anp.gov.br"]
    start_urls = [
	"http://www.anp.gov.br/postos/consulta.asp"
    ]


    def parse(self, response):
        return [FormRequest.from_response(response,
                    formdata={'sEstado': 'AC', 'sTipodePosto': '0', 'hPesquisar': 'PESQUISAR'},
                    callback=self.after_post, dont_click=True)]

    def after_post(self, response):
        sel = Selector(response)
        urls = sel.xpath("//input[starts-with(@name, 'i')]/@value")
        for url in urls:
            cod = url.extract()
            yield FormRequest.from_response(response, formname='frmResultado',
                    formdata={'estado': 'AC', 'Cod_inst': cod, 'municipio': '0'},
                    callback=self.after_second_post, dont_click=True)

    def after_second_post(self, response):
        sel = Selector(response)
        item = ANPItem()
        item['id'] = sel.xpath("//td/font[contains(translate(., 'CPF', 'cpf'), 'cpf')]/../../td[2]/font/text()").extract()[0]
        return item
