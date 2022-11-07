from setuptools import setup, find_packages

setup(
    name='nyu_cv_final_project',
    version='0.0.1',
    description='NYC CV Final Project',
    author='NYU',
    author_email='zz2960@nyu.edu',
    url='https://github.com/dizys/nyu-cv-final-project',
    packages=find_packages(),
    install_requires=[
        'torch',
        'torchvision',
        'Pillow',
        'transformers',
        'diffusers',
    ],
)
