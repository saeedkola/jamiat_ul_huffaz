from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in jamiat_ul_huffaz/__init__.py
from jamiat_ul_huffaz import __version__ as version

setup(
	name="jamiat_ul_huffaz",
	version=version,
	description="Huffaz Competition",
	author="Element Labs",
	author_email="saeed@elementlabs.xyz",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
