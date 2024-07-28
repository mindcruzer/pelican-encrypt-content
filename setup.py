from setuptools import setup, find_namespace_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pelican-encrypt-content",
    version="1.0",
    author="Sean Stewart",
    author_email="sean@mindcruzer.com",
    description="A pelican plugin to password protect articles and posts.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mindcruzer/pelican-encrypt-content",
    packages=find_namespace_packages(include=['pelican.*']),
    package_data={"": ["*.html"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Framework :: Pelican"
    ],
    install_requires=['pycryptodome>=3.9.7,<4'],
    python_requires='>=3.8'
)
