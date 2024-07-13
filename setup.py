from setuptools import setup, find_packages

setup(
    name='yoshium',
    version='0.2.1',
    packages=find_packages(),
    requires=["requests", "selenium", "ChromeDriverManager", "bs4"],
    author="yo_charm"
)
