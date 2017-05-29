# -*- coding: utf-8 -*-

from urllib.parse import urlencode
from urllib.request import Request, urlopen

def checacodCliente(code):
	url = 'http://localhost/check'
	post_fields = {'user':''} 
	#post_fields = {'user':'Admin'} 
	post_fields['code'] = code

	try:
		request = Request(url, urlencode(post_fields).encode())
		json = urlopen(request).read().decode()
		return json
	except Exception as e:
		return e

#para fins de teste
if __name__ == '__main__':
	print(checacodCliente("RXLCZSSXXX9L"))
