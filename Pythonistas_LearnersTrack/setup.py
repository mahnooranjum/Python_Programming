from setuptools import setup 
from Cython.Build import cythonize 

setup(
    ext_modules=cythonize('t5_statictyping.pyx')
)