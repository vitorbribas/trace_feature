from setuptools import setup

setup(

      name='trace_feature',
      packages = 'trace_feature',
      version='0.1',
      description='A lib to trace bdd features.',
      url='https://github.com/BDD-OperationalProfile/trace_feature',
      download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz'
      author='Rafael Fazzolino',
      author_email='fazzolino29@gmail.com',
      license='MIT',
      packages=['trace_feature', 'trace_feature.core', 'trace_feature.core.ruby', 'trace_feature.core.features'],
      zip_safe=False,
      py_modules=['trace_feature'],
      install_requires=[
            'Click',
      ],
      entry_points='''
            [console_scripts]
            trace-feature=trace_feature.trace_feature:trace
      '''
)