"""
NXToolkit Installer using setuptools
"""
import os
from setuptools import setup


base_dir = os.path.dirname(__file__)

about = {}
with open(os.path.join(base_dir, "nxtoolkit", "__about__.py")) as f:
    exec(f.read(), about)

setup(
    name=about["__title__"],
    version=about["__version__"],
    packages=["nxtoolkit"],
    author=about["__author__"],
    author_email=about["__email__"],
    url=about["__uri__"],
    license=about["__license__"],
    install_requires=["requests",
                      "websocket-client",
                      "gitpython",
                      "flask-sqlalchemy",
                      "flask-admin",
                      "flask-bootstrap",
                      "flask-wtf",
                      "flask",
                      "pymysql",
                      "tabulate"],
    description="This library allows basic Cisco Nexus configuration.",
)
