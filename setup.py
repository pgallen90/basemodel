from setuptools import setup

setup(name='base_model',
      version='0.2',
      description='Columns that should be in every Postgresql SQLAlchemy model. Used as a mixin. Support Postgres only.',
      url='http://github.com/pgallen90/base_model',
      author='Patrick Allen',
      author_email='patrickgallen@gmail.com',
      license='MIT',
      packages=['base_model'],
      zip_safe=False)