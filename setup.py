# -*- coding: utf-8 -*-

import glob
from setuptools import setup, find_packages

requires = ['docutils']

setup(
    name='bootstrap-rst',
    version='0.1',
    url='https://github.com/rougier/bootstrap-rst',
    # # PyPI url
    # download_url='',
    license='MIT',
    author='Nicolas P. Rougier',
    author_email='Nicolas.Rougier@inria.fr',
    description='Generates (X)HTML bootstrap-ready documents from standalone reStructuredText sources.',
    long_description="\n%s" % open('README.rst').read(),
    zip_safe=False,
    classifiers=[
        # 'Development Status :: 4 - Beta',
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # 'Framework :: Sphinx :: Extension',
        #'Framework :: Sphinx :: Theme',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    # packages=find_packages(),
    packages=['doc', 'bootstrap'],
    # package_dir={"": "src"},
    py_modules=['bootstrap', 'directives', 'roles'],
    include_package_data=True,
    install_requires=requires,
    # namespace_packages=['sphinxcontrib'],
    # install_requires=['docutils'],
    entry_points={
        'console_scripts': [
            'bootstrap-rst = bootstrap:main',
            'rst2bootstrap3 = bootstrap:traditional_main',
            'rst2bootstrap4 = bootstrap:traditional_main',
            'rst2bootstrap-carousel = bootstrap:traditional_main'
            ]},
    data_files=[
        ('', glob.glob('*.css')),
        ('', glob.glob('*.tmpl'))],
)
