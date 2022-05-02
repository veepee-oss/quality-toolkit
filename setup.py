from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="quality-toolkit",
    version="1.7.0",
    packages=find_packages(),
    entry_points={},
    install_requires=[
        'psycopg2-binary~=2.8',
        'requests~=2.25',
        'pytz~=2022.1',
        'python-tds~=1.10',
        'selenium~=4.1.0',
        'python-keycloak-client~=0.2',
        'pysftp~=0.2'],
    author="VpTech",
    author_email="vptech@veepee.com",
    description="Toolkit for the quality in order to help writing tests",
    keywords="Quality toolkit",
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/veepee-oss/quality-toolkit"
)
