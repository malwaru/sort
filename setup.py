import setuptools

def get_requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()

setuptools.setup(
    name="sort",
    version="1.0.0",
    author="Malika Navaratna",
    author_email='malikawarunamal@gmail.com',
    license="LICENSE",
    description="Python package of the SORT",   
    packages=setuptools.find_packages(exclude=["tests"]),
    python_requires=">=3.6",
    install_requires=get_requirements(),   
    data_files=[('', ['requirements.txt'])],
    include_package_data=True,
    options={'bdist_wheel': {'python_tag': 'py36.py37.py38'}},
)

