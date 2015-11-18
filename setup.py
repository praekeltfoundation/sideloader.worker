from setuptools import setup, find_packages

setup(name='sideloader.worker',
      version='0.1.0',
      description='Sideloader Rhumba worker',
      classifiers=[
          "Programming Language :: Python",
      ],
      author='Praekelt Foundation',
      author_email='dev@praekeltfoundation.org',
      url='http://github.com/praekeltfoundation/sideloader.worker',
      license='MIT',
      keywords='deb,rpm,virtualenv',
      packages=find_packages(exclude=['docs']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'rhumba',
        'Twisted',
        'redis',
        'psycopg2',
        'pyopenssl',
        'PyYAML',
      ],
    )
