from setuptools import setup, find_packages

setup(
    name="newsopen-easey",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # List your package's dependencies here
    ],
    author="Vijayanand",
    author_email="x22147802@student.ncirl.ie",
    description="A short description of your package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/x22147802/pollstats",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
