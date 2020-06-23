from cgi import parse_qs
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from template import html

def application(environ, start_response):
	d=parse_qs(environ['QUERY_STRING'])
	a=d.get('a',[''])[0]
	b=d.get('b',[''])[0]
	if '' not in [a,b]:
		a,b=int(a),int(b)
		c=a+b
		d=a*b
	else:
		c='N/A'
		d='N/A'
	response_body=html%{
		'c':c, 'd':d,
	}
	response_headers=[
		('Content-Type','text/html'),
		('Content-Length', str(len(response_body)))
	]
	start_response('200 OK',response_headers)
	return [response_body]

