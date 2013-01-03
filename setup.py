from distutils.core import setup

'''
To install (if this is the breanch "piptest"):
pip install git+git://github.com/industrydive/totalsendclient.git@piptest

'''
setup(
    name='TotalSend',
    version='0.0.1',
    author='Eli Dickinson',
    author_email='eli@industrydive.com',
    packages=['totalsend'],
    url='https://github.com/industrydive/totalsendclient/',
    description='Using TotalSend API.',
    long_description='No longer description needed.',
    install_requires=[],
)
