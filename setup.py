from setuptools import setup, find_packages

setup(
    name='flightradar',
    version='1.1',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    author='Tariq',
    description='Library to get data from flight_radar website',
    url='https://github.com/tariqmghari/flighradar_API',
)