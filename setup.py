from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    README = f.read()

setup(
    ### Metadata
    name='amsalgorithmus_at',
    version='0.1.1',
    description='Insert Description',
    long_description=README,
    url='',
    license='',
    author='Andreas Demmelbauer, Max Wolschlager',
    author_email='andreas@notice.at, comms@meks.io',
    maintainer='Andreas Demmelbauer, Max Wolschlager',
    maintainer_email='andreas@notice.at, comms@meks.io',
    classifiers=[
        'Development Status :: Prototyping',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    ### Scripts
    scripts=[
    ],
    ### Dependencies
    install_requires=[
        # 'python-dotenv',
        # 'django-sass-processor',
        # 'django-compressor==2.4.1',
        # 'django-inline-svg==0.1.1',
        # 'django-simple-captcha>=0.5',
        # 'libsass==0.21.0',
        # 'weasyprint<53',
        # 'Django~=2.2',
    ],
    extras_require={
        'dev': [
            'ptvsd', # debugger
            'autopep8' # formatter 
        ],
        'prod': []
    },
    dependency_links=[
    ],
    ### Contents
    packages=find_packages(),
)
