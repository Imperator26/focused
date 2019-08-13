import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="focused",
    version="0.1.0",
    author="Federico A. Corazza",
    author_email="federico.corazza@live.it",
    description=".",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Imperator26/focused",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "requests==2.22.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
