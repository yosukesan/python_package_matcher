
from abc import ABCMeta, abstractmethod

from package_debian import PackageDebian
from package_pypi import PackagePyPI
from package_error import PackageError

class PackageMatcher(metaclass=ABCMeta):

    def __init__(self):

        self._error = PackageError()

    @abstractmethod
    def query(self, target):

        self.query(target)
