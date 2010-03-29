from setuptools import setup, find_packages

setup(
    name='forgetmenot',
    version='0.0.1',
    url='http://bitbucket.org/trevor/forgetmenot',
    description='Simple flash card program',
    author='Trevor Caira',
    author_email='trevor@caira.com',
    packages=find_packages(),
    include_package_data=True,
    entry_points={'console_scripts': ['forgetmenot = forgetmenot:main']},
    zip_safe=True,
)
