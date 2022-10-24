site_map = xmltodict.parse(requests.get('--your sitemap url--').text)
urls = [url['loc'] for url in site_map['urlset']['url']]
return urls
#If you want to see the urls uncomment the next line.
#print("\n".join(urls))
