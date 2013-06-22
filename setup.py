#! /usr/bin/env python

from setuptools import setup


setup(
    name='mdx_lead_trail',
    version='0.1',
    author='Hendra',
    author_email='hendra2392@gmail.com',
    description='Python-Markdown extension to add special class name to first and last element of the document',
    url='',
    py_modules=['mdx_lead_trail'],
    install_requires=['Markdown>=2.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML'
    ]
)
