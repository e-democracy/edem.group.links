# coding=utf-8
import os
from setuptools import setup, find_packages
from version import get_version

version = get_version()

setup(name='edem.group.links',
    version=version,
    description="Provides a WYSIWYG editor for the Links tab of groups",
    long_description=open("README.txt").read() + "\n" +
                      open(os.path.join("docs", "HISTORY.txt")).read(),
    classifiers=[
      "Development Status :: 5 - Production/Stable",
      "Environment :: Web Environment",
      "Framework :: Zope2",
      "Intended Audience :: Developers",
      "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
      "Natural Language :: English",
      "Operating System :: POSIX :: Linux"
      "Programming Language :: Python",
      "Topic :: Software Development :: Libraries :: Python Modules",
      ],
    keywords='',
    author='Bill Bushey',
    author_email='bill.bushey@e-democracy.org',
    url='http://forums.e-democracy.org/',
    license='other',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['edem', 'edem.group'], 
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'setuptools',
        'edem.skin',
        'gs.content.form.base',
        'gs.group.base',
        'gs.group.home',
        'gs.viewlet',
        # -*- Extra requirements: -*-
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,)


