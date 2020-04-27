

def https_query(url):
    import urllib.request
   
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        body = res.read()

    return body
