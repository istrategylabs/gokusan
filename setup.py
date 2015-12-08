from setuptools import setup, find_packages

setup(
    name='s3deploy',
    version='0.0.1',
    author='Julian Gindi',
    author_email='julian@isl.co',

    url='https://github.com/istrategylabs/s3deploy',
    license='LGPL',
    description='A lightweight s3 deployment system for static sites',
    long_description=__doc__,
    keywords=['aws', 's3', 'command-line', 'CLI', 'deploy'],

    packages=find_packages(),
    scripts=[],
    entry_points={
        'console_scripts': [
            's3deploy = s3deploy.cli:main',
        ]
    },

    install_requires=[
        'boto3 >= 1.2.2',
        'PyYAML >= 3.11',
    ],
    # extras_require={
    #     'yaml': ['pyyaml', ]
    # },
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',

    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
)
