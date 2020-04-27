
class PackagePyPI:

    def __init__(self, url):
        self._url = url

    def query(self, target):
        from https import https_query
        addr = self._url + "/" + target + "/json" 
        return https_query(addr)
