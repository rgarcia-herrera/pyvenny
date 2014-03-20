from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='pyvenny',
      version='0.1',
      description='Venn diagram plot of four sets, like venny.',
      long_description=readme(),
      # classifiers=[
      #   'Development Status :: 0 - Alpha',
      #   'License :: OSI Approved :: GPLv3',
      #   'Programming Language :: Python :: 2.7',
      #   'Topic :: Text Processing :: Linguistic',
      # ],
      url='http://github.com/CSB-IG/pyvenny',
      author='Rodrigo Garcia',
      author_email='rgarcia@inmegen.gob.mx',
      license='GPLv3',
      packages=['pyvenny'],
      install_requires=[ 'Jinja2' ],
      zip_safe=False)
