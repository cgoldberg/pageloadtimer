
from setuptools import setup

setup(
    name='navtimer',
    version='0.1.0',
    author='Corey Goldberg',
    author_email='cgoldberg@gmail.com',
    py_modules=['navtimer',],
    url='https://github.com/cgoldberg/navtimer',
    license='MIT',
    description='Automated Metric Collection from Web Navigation Timing API',
    long_description=open('README.rst').read(),
    install_requires=[
        'pyvirtualdisplay >= 0.1.5',
        'easyprocess >= 0.1.6',
        "selenium >= 2.44.0",
    ],
)
