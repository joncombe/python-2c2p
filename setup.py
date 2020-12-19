# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

setup(
    name='python-2c2p',
    version='0.0.4',
    author=u'Jon Combe',
    author_email='jon@salebox.io',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    url='https://github.com/joncombe/python-2c2p',
    license='BSD licence, see LICENCE file',
    description='Python class to connect with 2c2p.com redirect API (version 7.5)',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    zip_safe=False,
)
