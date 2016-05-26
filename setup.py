import setuptools


def requirements_from_file(file_name):
    requirement = []
    with open(file_name, 'rb') as f:
        requirement.extend(f.read().split('\n'))

    return requirement


classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: Implementation :: CPython',
    'Topic :: Communications',
    'Topic :: Communications :: Email',
    'Topic :: Software Development :: Libraries'
]

setuptools.setup(
        name='python-email-normalizer',
        version='0.1.4',
        description='Normalize email addresses',
        long_description=open('README.md').read(),
        author='Rubtsov Dmitry',
        author_email='rubtsov.dmv@gmail.com',
        url='https://github.com/r-dmv/python-email-normalizer',
        packages=['email_normalizer'],
        install_requires=requirements_from_file('requirements.txt'),
        tests_require=requirements_from_file('test-requirements.txt'),
        license=open('LICENSE').read(),
        classifiers=classifiers,
        package_data={'': ['LICENSE', 'README.md']},
        include_package_data=True,
)
