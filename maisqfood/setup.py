from setuptools import setup, find_packages

def read(filename):
    return [req.strip() for req in open(filename).readlines()]

setup(
    name="maisqfood",
    version="0.1.0",
    desciption="Delivery APP",
    packages=find_packages(),
    include_package_data=True,
    install_requeres=read("requeriments.txt"),
    extras_require={
        "dev": read("requeriments-dev.txt")
    }
)
