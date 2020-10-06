import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="streamdeck-jfm",
    version="0.1.0",
    author="Jesper Fussing Mørk ",
    author_email="jfm@moerks.dk",
    description="A simple daemon for controlling the Elgato StreamDeck devices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jfm/streamdeck-daemon",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
