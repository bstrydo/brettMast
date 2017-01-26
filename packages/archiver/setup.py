from setuptools import setup

setup(
    name='lektor-archiver',
    version='0.1',
    author=u'Brett Strydom',
    author_email='bstrydo@thoughtworks.com',
    license='MIT',
    py_modules=['lektor_archiver'],
    entry_points={
        'lektor.plugins': [
            'archiver = lektor_archiver:ArchiverPlugin',
        ]
    }
)
