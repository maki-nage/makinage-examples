import sys

try:
    from setuptools import setup, find_packages
    use_setuptools = True
except ImportError:
    from distutils.core import setup
    use_setuptools = False

try:
    with open('README.rst', 'rt') as readme:
        description = '\n' + readme.read()
except IOError:
    # maybe running setup.py from some other dir
    description = ''

python_requires = '>=3.6'
install_requires = [
    'makinage>=0.8',
]

setup(
    name="makinage_examples",
    version='0.0.0',
    url='https://github.com/maki-nage/makinage-examples.git',
    license='MIT',
    description="ReactiveX for data science",
    long_description=description,
    author='Romain Picard',
    author_email='romain.picard@oakbits.com',
    packages=find_packages(),
    install_requires=install_requires,
    platforms='any',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    project_urls={
        'Documentation': 'https://www.makinage.org/doc/makinage-book/latest/index.html',
    }
)
