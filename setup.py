from setuptools import setup, find_packages

setup(
    name="PythonK",
    version="1.0.0",
    description="Simplify the library of Python code.The code for the lib is neat.",
    long_description=open("README.md", encoding="UTF-8").read(),
    long_description_content_type="text/markdown",
    author="NAK",
    author_email="18114055256@163.com",
    url="https://github.com/JimmyJimmy666/PythonK.git",
    license="MIT",
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.6",
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)