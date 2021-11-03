from setuptools import find_packages, setup

VERSION = '0.0.2'
DESCRIPTION = 'Download videos from Vimeo'
long_description = 'A package that downloads public and private videos from Vimeo'

# If the README.md file exists, use it as the long description
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='vimeodownload.py',
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='jamiegyoung',
    url='https://github.com/jamiegyoung/vimeodownload.py',
    keywords=['python', 'video', 'vimeo', 'download'],
    packages=find_packages(),
    install_requires=['requests>=2,<3'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Internet',
        'Topic :: Multimedia :: Video',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
