import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="autofilter-peteywoufes",
    version="0.1",
    packages=['autofilter'],
    author="Peter Rolfe",
    author_email="peter.jhrolfe@protonmail.com",
    description="Labels, filters and groups using the Gmail API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/peteywoufes/autofilter",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)