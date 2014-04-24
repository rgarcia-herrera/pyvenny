from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='pyvenny',
      version='0.2rc',
      description='Venn diagram plot of four sets, like venny.',
      long_description=readme(),
      classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Visualization',
      ],
      url='http://github.com/CSB-IG/pyvenny',
      author='Rodrigo Garcia',
      author_email='rgarcia@inmegen.gob.mx',
      license='GPLv3',
      packages=['pyvenny'],
      install_requires=[ 'Jinja2' ],
      scripts=['bin/vennyplot'],
      include_package_data=True,
      zip_safe=False)
