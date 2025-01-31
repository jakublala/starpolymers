import setuptools
import versioneer

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="starpolymers",
    author="Debesh Mandal",
    description="Package for creating polymers for simulation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/debeshmandal/starpolymers",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.5",
    package_data = {'starpolymers' : ['io/input_files/*.in']},
    include_package_data=True,
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
)
