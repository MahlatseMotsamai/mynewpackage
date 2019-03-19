from setuptools import setup, find_packages

setup(
    name='mynwepackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<MahlatseMotsamai>/<mynwepackage>',
    author='<MahlatseMotsamai>',
    author_email='<mpmotsamai4@gmail.com>'
)
