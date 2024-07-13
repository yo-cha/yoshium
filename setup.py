from setuptools import setup, find_packages

setup(
    name='yoshium',
    version='0.3.0',
    packages=["yoshium"],
    requires=["requests", "selenium", "ChromeDriverManager", "bs4"],
    author="yo_charm"
)
