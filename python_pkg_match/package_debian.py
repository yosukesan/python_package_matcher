
class PackageDebian:
    
    def __init__(self, url):
        self._url = url

    def query(self, target):
        from https import https_query

        #https://sources.debian.org/api/search/query
        addr = self._url + "/search/" + target 
        return https_query(addr)
