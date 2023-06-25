from setuptools import setup, find_packages

setup(
    name="my_minipack",
    version="1.0.0",
    packages=find_packages(),
    author="Charles Berganza",
    author_email="cberganz@student.42.fr",
    description="A small example package",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
    ],
)
