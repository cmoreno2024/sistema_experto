from setuptools import setup, find_packages

setup(
    name='sistema_experto_hotel',
    version='0.1.0',
    description='Sistema experto para la asignación de habitaciones en hoteles de Ushuaia',
    author='Tu Nombre',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'experta',
    ],
)
