# setup.py
from setuptools import setup

setup(
    name='upperTolower',
    version='0.1',
    py_modules=['texttransform'],
    entry_points={
        'console_scripts': [
            'upperTolower = text_transform:main',
        ],
    },
    description='A simple tool to convert uppercase sentences to lowercase and vice versa and also create correct cases for sentences.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Genevevieve',
    author_email='',
    url='https://github.com/Genevieveok/texttransform',
)


from setuptools import setup

setup(
    name='texttransform',
    version='0.1',
    py_modules=['text_transform'],
    entry_points={
        'console_scripts': [
            'texttransform = text_transform:main',
        ],
    },
    description='A tool to convert sentences between uppercase and lowercase and to format sentences correctly.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Genevieve',
    author_email='genevieve.okon@rocketmail.com',
    url='https://github.com/Genevieveok/texttransform',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

