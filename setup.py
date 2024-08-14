from setuptools import find_packages , setup

setup(
    name = "Summary",
    version =  '0.0.1',
    author= 'TienLe',
    author_email='tle38413@gmail.com',
    install_requires = ["streamlit" , "transformers"],
    packages=find_packages()
)