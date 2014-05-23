from setuptools import setup, find_packages

def get_long_description():
    lines = open('README.rst').read().splitlines()
    end = lines.index('Getting Started')
    return '\n' + '\n'.join(lines[:end]) + '\n'

setup(
    name='rope',
    use_scm_version={
        'version_scheme': 'guess-next-dev',
        'local_scheme': 'dirty-tag',
        'write_to': 'rope/_version.py'
    },
    setup_requires=[
        'setuptools>=18.0',
        'setuptools-scm>1.5.4'
    ],
    description='a python refactoring library...',
    long_description=get_long_description(),
    author='Ali Gholami Rudi',
    author_email='ali@rudi.ir',
    maintainer='Matej Cepl',
    maintainer_email='mcepl@cepl.eu',
    url='https://github.com/python-rope/rope',
    packages=find_packages(exclude=['ropetest*']),
    license='GNU GPL',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Environment :: X11 Applications',
        'Environment :: Win32 (MS Windows)',
        'Environment :: MacOS X',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: Software Development'
    ],
    test_suite='ropetest',
)
