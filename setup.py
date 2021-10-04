from distutils.core import setup

setup(

      name='trace_feature',
      packages=['trace_feature', 'trace_feature.core', 'trace_feature.core.ruby', 'trace_feature.core.features'],
      version='0.5',
      description='A lib to trace bdd features.',
      url='https://github.com/vitorbribas/trace_feature',
      download_url = 'https://github.com/vitorbribas/trace_feature/archive/refs/tags/v_05.tar.gz',
      author='Rafael Fazzolino',
      author_email='fazzolino29@gmail.com',
      license='MIT',
      keywords = ['BDD', 'Trace'],
      py_modules=['trace_feature'],
      install_requires=[
            'Click==7.0',
            'gherkin-official==4.1.3',
            'requests==2.21.0'
      ],
      entry_points='''
            [console_scripts]
            trace-feature=trace_feature.trace_feature:trace
      '''
)
