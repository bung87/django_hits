from setuptools import setup, find_packages

setup(
    name = "django_hits",
    version = "0.2.0-1",
    description = 'Count visitors/views for your page',
    author = 'David Danier',
    author_email = 'david.danier@team23.de',
    url = 'https://github.com/ddanier/django_hits',
    #long_description=open('README.rst', 'r').read(),
    packages = [
        'django_hits',
        'django_hits.south_migrations',
        'django_hits.templatetags',
    ],
    install_requires = [
        'Django >=1.3',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
)

