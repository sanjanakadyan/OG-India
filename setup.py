try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.md') as f:
        longdesc = f.read()

version = '0.0.0'

config = {
    'description': 'General equilibribum, overlapping generations model for India',
    'long_description': longdesc,
    'url': 'https://github.com/TPRU-India/OG-India/',
    'download_url': 'https://github.com/TPRU-India/OG-India/',
    'version': version,
    'license': 'CC0 1.0 Universal public domain dedication',
    'packages': ['ogindia'],
    'include_package_data': True,
    'name': 'ogindia',
    'install_requires': ['taxcalc', 'dask', 'scipy', 'matplotlib', 'mkl'],
    'package_data': {
                     'ogindia': [
                               'parameters_metadata.json',
                               'default_parameters.json',
                               'data/ability/*',
                               'data/demographic/*',
                               'data/labor/*',
                               'data/wealth/*']
                     },
    'classifiers': [
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: CC0 1.0 Universal public domain dedication',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    'tests_require': ['pytest']
}

setup(**config)
