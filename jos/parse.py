def _issues(html):
    return html.xpath('id("issuesToc")//a/@href')

def _pdfs(html):
    html.xpath('//div[@class="fullContentLink"]/a/@href')
