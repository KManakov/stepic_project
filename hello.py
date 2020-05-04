def wsgi_application(environ, start_response):
    status = "200 OK"
    headers = [
        ('Content-Type', 'text/plain')
    ]
    data = environ['QUERY_STRING'].split('&')
    body = '\n'.join(data).encode('utf-8')
    start_response(status, headers)
    return [body]

