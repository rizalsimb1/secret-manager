from setuptools import setup, find_packages
setup(
    name="secret-manager",
    version="0.1.0",
    packages=find_packages(),
    entry_points={"console_scripts": ["devkit=src.main:app"]},
    install_requires=["typer[all]>=0.12.0", "rich>=13.7.0"],
    python_requires=">=3.11",
)
