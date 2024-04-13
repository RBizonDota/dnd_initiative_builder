import codecs

from setuptools import setup, find_packages

setup(
    name="dynini",
    version="0.1",
    packages=find_packages(),
    install_requires=["pydantic", "click", "pyyaml", "prettytable"],
    license="MIT",
    long_description=codecs.open("README.md", "r", "utf_8_sig").read(),
    zip_safe=False,
    entry_points={
        "console_scripts": ["dnd_ini=src.app:app"],
    },
)
