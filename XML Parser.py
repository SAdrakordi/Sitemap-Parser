site_map = xmltodict.parse(requests.get('--your sitemap url--').text)
urls = [url['loc'] for url in site_map['urlset']['url']]
print("\n".join(urls))
