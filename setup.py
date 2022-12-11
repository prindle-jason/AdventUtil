import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='adventutil',
    version='0.0.1',
    author='Jason Prindle',
    author_email='prindle.jason@gmail.com',
    description='Personal Utility Package for adventofcode.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/prindle-jason/AdventUtil',
    project_urls = {
        "Bug Tracker": "https://github.com/prindle-jason/AdventUtil/issues"
    },
    license='MIT',
    packages=['adventutil'],
    install_requires=['requests'],  
)