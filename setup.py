#-*- coding: utf-8 -*-
from setuptools import setup
import os

CLASSIFIERS = []

setup(
    author="Arturo Fernandez Montoro",
    author_email="arturo@bsnux.com",
    name='django-simple-thumbs',
    version='0.0.1',
    description='A Django application to provide thumbnails in your application or project',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    url='https://github.com/bsnux/django-simple-thumbs/',
    license='BSD License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
)
