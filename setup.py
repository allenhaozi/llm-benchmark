import os

from setuptools import find_packages, setup


# 读取文件
def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename), encoding="utf-8") as f:
        long_description = f.read()
    return long_description


setup(
    # 基本信息
    name="llm-benchmark",  # project name, global unique name
    version="1.0.0",  # version
    author="allen",  # project develop
    author_email="allenhaozi@gmail.com",  # email
    description="use for llm dev test tools",  # description
    long_description=read_file("README.md"),  # detail description for pypi
    long_description_content_type="text/markdown",  # file format
    platforms="python3",  # platform
    url="https://github.com/allenhaozi/llm-benchmark",  # repo site
    # configuration
    # include src expect tests
    packages=find_packages("src", exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_dir={"": "src"},  # find_packages define code directory
    package_data={
        # include .txt all of them
        "": ["*.txt"]
    },
    exclude_package_data={},
    # python version
    python_requires=">=3",
    # pypi
    install_requires=[
        "flask >= 2.0.1",
    ],
    # auto generate executable files
    # Unix /path/to/python/bin
    entry_points={
        "console_scripts": [
            "print_args = example_package_01.example:print_args",  # entrenched to function
        ],
    },
)
