from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in shopify/__init__.py
from shopify import __version__ as version

setup(
	name="shopify",
	version=version,
	description="shopify connector",
	author="vignesh",
	author_email="vigneshmanimsc@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
