from setuptools import setup, find_packages

setup(
    name="eventstream",
    packages=find_packages(),
    version="0.1",
    entry_points={
        "console_scripts":[
            "manage=eventstream.manage:main",
        ],
    },
)
