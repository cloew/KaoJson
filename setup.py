from distutils.core import setup

setup(name='kao_json',
      version='0.3.1',
      description='Python JSON Conversion Library',
      author='Chris Loew',
      author_email='cloew123@gmail.com',
      #url='http://www.python.org/sigs/distutils-sig/',
      packages=['kao_json',
                'kao_json.builders',
                'kao_json.config',
                'kao_json.providers'],
      install_requires = ['kao_decorators',
                          'kao_dict']
     )