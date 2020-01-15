import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="belc_log",
    version="0.0.1",
    author="Francis Josue De la Cruz",
    author_email="francis.delacruz@hundred.com.pe",
    description="A small api log example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/1311543/belc-dlk-api-log-archetype.git",
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3.4',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests'
    ],
    python_requires='>=3.*, <4'
)
