from setuptools import setup

setup(name='pyvenny',
      version='0.1',
      description='Venn diagram plot of four sets, like venny.',
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
