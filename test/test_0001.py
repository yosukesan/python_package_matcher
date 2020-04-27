
import sys
sys.path.append("../")

from python_pkg_match import PackageMatcher



def test_debian():
    deb = PackageMatcher("debian")
    target = "pypi"
    print (deb.query(target))

def test_pypi():
    pypi = PackageMatcher("pypi")
    target = "pypi"
    print (pypi.query(target))
