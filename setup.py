import setuptools

with open("Readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="logbot-telegram",
    version="0.1.0",
    author="Alejandro Piad",
    author_email="apiad@apiad.net",
    description="A Telegram bot that you can log to from Python and manage long running processes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/apiad/logbot",
    packages=['logbot'],
    install_requires=[
        'python-telegram-bot==11.1.0',
        'sanic==18.12.0'
    ],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
