# from distutils.core import setup
from setuptools import setup, find_packages

setup(name='Task2',
      version='1.0',
      description='Automate test framework for FE, BE and API ',
      author='Jojo Songoa',
      author_email='jojosongoas@gmail.com',
      url='https://www.jojosongoa.com/',
      packages=find_packages(),
      zip_safe=False,
      install_requires=[
            "pytest==6.2.5",
            "pip==20.3.4",
            "attrs==21.2.0",
            "toml==0.10.2",
            "py==1.10.0",
            "lxml==4.6.3",
            "idna==2.10",
            "six==1.15.0",
            "behave==1.2.6",
            "parse==1.19.0",
            "certifi==2020.12.5",
            "selenium==3.141.0",
            "urllib3==1.25.11",
            "setuptools==49.2.1",
            "cython==3.0.0a9",
            "chardet==3.0.4",
            "requests==2.26.0",
            "python-dotenv==0.20.0",
            "pymysql==0.9.3",
            "webdriver_manager"
      ]
      )