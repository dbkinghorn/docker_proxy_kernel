
from setuptools import setup

setup(name='docker_proxy_kernel',
      version='0.0.1',
      description='Jupyter notebook kernel for running kernels in a docker',
      url='https://github.com/andyneff/docker-proxy-kernel',
      author='Andrew Neff',
      author_email='andrew.neff@visionsystemsinc.com',
      license='MIT',
      packages=[],
      install_requires=['six', 'traitlets', 'ipykernel'],
      scripts=[]
      )
