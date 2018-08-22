import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chronotrack",
    version="0.0.3",
    author="Romeno",
    author_email="RomenoEx@gmail.com",
    description="chronotrack API python interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Romeno/chronotrack",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)