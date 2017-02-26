import setuptools
import os


__version__ = "0.0.1"
__author__ = "Nyaundi Brian"


with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setuptools.setup(
    name='convert2php',
    packages=setuptools.find_packages(),
    entry_points={
          'console_scripts': [
              'convert2php = src.php2python:main'
          ]
      },
    version=__version__,
    description='A python script to convert simple php code to python',
    author='Nyaundi Brian',
    author_email='ndieksman@gmail.com',
    url='https://github.com/danleyb2/php2python',
    download_url='https://github.com/danleyb2/php2python/tarball/0.0.1',
    keywords=['php', 'python', 'convert'],
    include_package_data=True,
    zip_safe=False,
    license='MIT',
    long_description=README,
    platforms='any',
    install_requires=[],
    classifiers=[
         #'Development Status :: 1 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
)
