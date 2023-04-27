from setuptools import setup, find_packages

setup(
    name="pollstats",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # List your package's dependencies here
    ],
    author="Vijayanand",
    author_email="vijayanand563@gmail.com",
    description="A short description of your package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Vijayanand-debug/pollstats",
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
