from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="quality-toolkit",
    version="2.2.0",
    packages=find_packages(),
    entry_points={},
    install_requires=[
        'psycopg2-binary==2.9.5',
        'requests==2.28.2',
        'pytz==2022.7.1',
        'python-tds==1.12.0',
        'selenium==4.8.2',
        'python-keycloak-client==0.2.3',
        'pysftp==0.2.9',
        'playwright==1.31.1'],
    author="VpTech",
    author_email="vptech@veepee.com",
    description="Toolkit for the quality in order to help writing tests",
    keywords="Quality toolkit",
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/veepee-oss/quality-toolkit"
)
