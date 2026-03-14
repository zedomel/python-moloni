from setuptools import setup

from moloni.__version__ import __version__

setup(
    name="python-moloni-fix",
    version=__version__,
    install_requires=["requests", "cachetools>=4.2", "pydantic"],
    extras_require={
        "aws-caching": ["aws-secretsmanager-caching", "boto3"],
        "aws": ["boto3"],
    },
    packages=["moloni.api", "moloni.base", "moloni"],
    url="https://github.com/zedomel/python-moloni",
    license="MIT",
    author="José Augusto Salim",
    author_email="zedomel@gmail.com",
    description="Python wrapper for the Moloni API"
)
