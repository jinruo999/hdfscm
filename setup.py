from setuptools import setup

with open('README.rst') as f:
    long_description = f.read()

setup(name='jupyter-hdfscm',
      version='0.1.0',
      license='BSD',
      maintainer='Jim Crist',
      maintainer_email='jiminy.crist@gmail.com',
      description='Jupyter ContentsManager for HDFS',
      long_description=long_description,
      url='http://github.com/jcrist/hdfscm',
      project_urls={
          'Source': 'https://github.com/jcrist/hdfscm',
          'Issue Tracker': 'https://github.com/jcrist/hdfscm/issues'
      },
      keywords='jupyter contentsmanager HDFS Hadoop',
      classifiers=['Topic :: System :: Systems Administration',
                   'Topic :: System :: Distributed Computing',
                   'License :: OSI Approved :: BSD License',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 3'],
      packages=['hdfscm'])
