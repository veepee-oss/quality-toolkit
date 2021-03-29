from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="quality-toolkit",
    version="1.1.0-beta.1",
    packages=find_packages(),
    entry_points={},
    install_requires=[
        'requests',
        'pytz',
        'python-tds',
        'psycopg2-binary',
        'selenium',
        'python-keycloak-client'],
    author="jmfiaschi",
    author_email="jmfiaschi@veepee.com",
    description="Toolkit for the quality in order to help writing tests",
    keywords="Quality toolkit",
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/veepee-oss/quality-toolkit"
)
