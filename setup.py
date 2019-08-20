from setuptools import setup, find_packages
from opulence.common import __version__

setup(
    name='Opulence',
    version=__version__,
    author="Louis Jurczyk",
    author_email="louis@jurczyk.fr",
    description='Open source intelligence intelligent framework',
    packages=["opulence.common",
              "opulence.collectors"
              "opulence.facts"],
    package_dir={"opulence.common": "opulence/common",
                 "opulence.collectors": "opulence/collectors",
                 "opulence.facts": "opulence/facts"},
    namespace_packages=["opulence"]
)
