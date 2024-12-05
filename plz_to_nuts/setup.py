from setuptools import setup

setup(
    name='plz_to_nuts',
    version='0.1.0',
    packages=['plz_to_nuts'],
    entry_points={
        'console_scripts': [
            'plz_to_nuts = plz_to_nuts.__main__:main'
        ]
    }
)
