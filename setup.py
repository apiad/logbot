import setuptools

long_description = """
# LogBot [![](https://img.shields.io/pypi/v/logbot-telegram.svg?style=flat-square)](https://pypi.org/project/logbot-telegram/) [![](https://img.shields.io/pypi/pyversions/logbot-telegram.svg?style=flat-square)](https://pypi.org/project/logbot-telegram/)

A Telegram bot that you can log to from Python and manage long running processes.
Check the [Readme](https://github.com/apiad/logbot) for use and installation instructions.
"""

setuptools.setup(
    name="logbot-telegram",
    version="0.1.5",
    author="Alejandro Piad",
    author_email="apiad@apiad.net",
    description="A Telegram bot that you can log to from Python and manage long running processes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/apiad/logbot",
    packages=['logbot'],
    install_requires=[
        'python-telegram-bot==11.1.0',
        'sanic==18.12.0',
        'emoji==0.5.1',
        'requests==2.21.0'
    ],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
