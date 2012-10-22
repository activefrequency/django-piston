#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup, find_packages
    
import os

setup(
    name = "django-piston",
    version = "0.2.3",
    url = 'http://bitbucket.org/jespern/django-piston/wiki/Home',
	download_url = 'http://bitbucket.org/jespern/django-piston/downloads/',
    license = 'BSD',
    description = "Piston is a Django mini-framework creating APIs.",
    author = 'Jesper Noehr',
    author_email = 'jesper@noehr.org',
    packages = find_packages(),
    # Removing 'piston' as a namespaced package - see discussion on:
    #   https://bitbucket.org/jespern/django-piston/issue/173/
    # Note that this means that other packages can't install themselves
    # in the piston namespace (i.e. piston.*)
    # namespace_packages = ['piston'],
    include_package_data = True,
    zip_safe = False,
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
