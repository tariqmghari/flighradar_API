from setuptools import setup, find_packages

setup(
    name='Flight radar unofficial API',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    author='Tariq',
    description='Library to get data from flight_radar website',
    url='https://github.com/tariqmghari/flighradar_APIy',
)