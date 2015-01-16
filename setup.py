
from setuptools import setup

setup(
    name='pageloadtimer',
    version='0.1.0',
    author='Corey Goldberg',
    author_email='cgoldberg@gmail.com',
    py_modules=['pageloadtimer',],
    url='https://github.com/cgoldberg/pageloadtimer',
    license='MIT',
    description='Automated Web Page Load Timer',
    long_description=open('README.rst').read(),
    install_requires=[
        'pyvirtualdisplay >= 0.1.5',
        'easyprocess >= 0.1.6',
        "selenium >= 2.44.0",
    ],
)
