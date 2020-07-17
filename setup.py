from setuptools import setup

setup(
    name="pydocmd",
    version="1.0",
    description="Generate python module / script documentation in Markdown format",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/fboender/pydocmd",
    author="Ferry Boender",
    author_email="ferry.boender@gmail.com",
    license="MIT",
    packages=["pydocmd"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=True,
    scripts=['pydocmd/pydocmd']
)
