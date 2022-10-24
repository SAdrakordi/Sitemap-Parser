site_map = xmltodict.parse(requests.get('https://pakhshjoorchin.com/product-sitemap2.xml').text)
urls = [url['loc'] for url in site_map['urlset']['url']]
print("\n".join(urls))
