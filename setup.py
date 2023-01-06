from setuptools import setup

with open("requirements.txt", "r") as fh:
    requirements = [line.strip() for line in fh]

setup(
    name="cymuk",
    version="v0.2.0",
    url="https://github.com/itsdmd/cymuk",
    author="Đức Đào",
    author_email="duc.dao.431@gmail.com",
    description="Control Your Mouse Using Keyboard",
    long_description="README.md",
    keywords="mouse, keyboard, automation",
    license="MIT",
    classifiers=["Programming Language :: Python :: 3"],
    python_requires=">=3.0",
    install_requires=requirements,
)
