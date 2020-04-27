

from package_debian import PackageDebian
from package_pypi import PackagePyPI
  
if __name__ == "__main__": 

    import sys

    argvs = sys.argv

    if len(argvs) != 2:
        print("Usage: python3 pkg_match ${package_name}")
        exit(-1)

    pypi = PackagePyPI("https://pypi.org/pypi")

    package = argvs[1]
    res = pypi.query(package)

    import json
    data = json.loads(res.decode('utf-8'))
    pypi_url = data['info']['project_urls']['Homepage']

    import subprocess
    apt_res = subprocess.run(["apt-cache", "search", package], capture_output=True)
    deb_pkgs = apt_res.stdout.decode('utf-8').split('\n')
    pkg_names = list(map(lambda x: x.split(' ')[0], deb_pkgs))

    import re
    info = []
    for p in pkg_names:
        apt_show = subprocess.run(["apt-cache", "show", p], capture_output=True).stdout.decode('utf-8')
        deb_url = re.findall("Homepage:(.*)", apt_show)

        print(p, *deb_url)
