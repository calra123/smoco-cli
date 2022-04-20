from setuptools import setup
setup(
    name = 'smoco-cli',
    version = '0.1.0',
    packages = ['smoco'],
    entry_points = {
        'console_scripts': [
            "smoco-cli = smoco.__main__:main"
        ]
    })
