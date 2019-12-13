from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="sonar",
    version="0.1",
    author="Michele Gaiarin",
    author_email="michele.gaiarin@gmail.com",
    description="It is a sonar.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ilgaiaz/sonarQt",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'serial'
    ]
)
