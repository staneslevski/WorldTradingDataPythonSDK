import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


def build_requirements_array():
    with open("requirements.txt", "r") as f:
        _requirements_array = []
        for line in f:
            _requirements_array.append(line)
        return _requirements_array


requirements_array = build_requirements_array()

setuptools.setup(
    name="worldtradingdata",
    version="0.1.5",
    author="Tom Stanley",
    author_email="tstanleyuk@icloud.com",
    description="Python SDK to interact with www.worldtradingdata.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/staneslevski/WorldTradingDataPythonSDK",
    packages=setuptools.find_packages(),
    keywords=['finance', 'trading', 'data', 'world trading data'],
    install_requires=requirements_array,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Financial and Insurance Industry"
    ],
)
