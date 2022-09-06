import pathlib
import re
import setuptools


def read_version():
    with open(pathlib.Path(__file__).parent.joinpath('parus/__init__.py')) as fp:
        m = re.search(r"^__version__ = '([\d]+(?:\.[\d]+)*((a|b|rc)[\d]+)?(\.post[\d]+)?(\.dev[\d]+)?)'", fp.read())
        if m:
            return m.group(1)
        raise RuntimeError('version not fount')


setuptools.setup(
    name='parus',
    description='Google Drive CLI tool',
    version=read_version(),
    python_requires='>=3.7.5',
    install_requires=[
        'google-api-python-client>=2.58.0',
        'google-auth-httplib2>=0.1.0',
        'google-auth-oauthlib>=0.5.2',
    ],
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': ['parus = parus.main:entry_point'],
    },
    url='https://github.com/kikuchi-m/parus',
    author='Kikuchi Motoki',
    author_email='wildflower.pink0102@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
    ],
)
