from setuptools import setup, find_packages


setup(name='pga.basemodel',
      version='0.3',
      description='Columns that should be in every Postgresql SQLAlchemy model. Used as a mixin. Support Postgres only.',
      url='http://github.com/pgallen90/basemodel',
      author='Patrick Allen',
      author_email='patrickgallen@gmail.com',
      license='MIT',
      namespace_packages=['pga'],
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False)
