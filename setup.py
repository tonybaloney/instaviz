import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="instaviz",
    version="0.6.0",
    description="Read the latest Real Python tutorials",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/tonybaloney/instaviz",
    author="Anthony Shaw",
    author_email="anthonyshaw@apache.org",
    license="ASF",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["instaviz"],
    include_package_data=True,
    install_requires=["bottle", "jinja2", "pygments", "dill", "pyreadline"]
)
