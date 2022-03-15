import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='cp-imports',
    version='0.0.6',
    author='Steven Hopkins',
    author_email='srhopkins@gmail.com',
    description='Tools to track Cloud Posse imports in stack configs',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/srhopkins/cp-imports',
    license='MIT',
    packages=['imports'],
    install_requires=[],
    entry_points = {
        'console_scripts': [
            'cp-imports=imports.imports:main',
            ],
    }
)
