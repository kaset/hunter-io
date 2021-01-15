import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Hunter-io", # Replace with your own username
    version="0.0.1",
    author="rdn rys",
    author_email="2521angka@gmail.com",
    description="proyek Nomor 001",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kaset/hunter-io",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)