import setuptools

setuptools.setup(
    name="custo",
    version="0.1.0",
    url="https://github.com/filipwodnicki/custo",
    author="Filip Wodnicki",
    author_email="hello@filipwodnicki.com",
    description="Cutting Stock Problem (1D) algorithms implemented with Python 3.",
    long_description=open('README.md').read(),
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)