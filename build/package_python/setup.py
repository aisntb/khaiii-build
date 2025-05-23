# -*- coding: utf-8 -*-


"""
Kakao Hangul Analyzer III

__version__ = '0.4'
__author__ = 'Kakao Corp.'
__copyright__ = 'Copyright (C) 2018-, Kakao Corp. All rights reserved.'
__license__ = 'Apache 2.0'
__maintainer__ = 'Jamie'
__email__ = 'jamie.lim@kakaocorp.com'
"""


###########
# imports #
###########
from distutils.command.build import build
import os
import shutil
import subprocess
import zipfile

from setuptools import setup


#############
# constants #
#############
_SRC_NAME = 'khaiii-0.4'


#########
# types #
#########
class CustomBuild(build):
    """
    custom handler for 'build' command
    """
    def run(self):
        """
        run build command
        """
        with zipfile.ZipFile('{}.zip'.format(_SRC_NAME), 'r') as src_zip:
            src_zip.extractall()
        build_dir = '{}/build'.format(_SRC_NAME)
        os.makedirs(build_dir, exist_ok=True)
        subprocess.check_call('cmake ..', cwd=build_dir, shell=True)
        subprocess.check_call('make all resource', cwd=build_dir, shell=True)
        shutil.rmtree('khaiii/lib', ignore_errors=True)
        shutil.copytree('{}/lib'.format(build_dir), 'khaiii/lib')
        shutil.rmtree('khaiii/share', ignore_errors=True)
        shutil.copytree('{}/share'.format(build_dir), 'khaiii/share')
        shutil.rmtree(_SRC_NAME)
        build.run(self)


#############
# functions #
#############
def readme():
    """
    read content from README.md file
    Returns:
        long description (content of README.md)
    """
    return open('/home/hisnty/khaiii/README.md', 'r', encoding='UTF-8').read()


#########
# setup #
#########
setup(
    name='khaiii',
    version='0.4',
    description='Kakao Hangul Analyzer III',
    long_description=readme(),
    url='https://github.com/kakao/khaiii',
    author='Kakao Corp.',
    author_email='jamie.lim@kakaocorp.com',
    classifiers=[
        'Development Status :: 5 - Stable',
        'License :: OSI Approved :: Apache 2.0',
        'Programming Language :: Python :: 3',
    ],
    license='Apache 2.0',
    packages=['khaiii', ],
    include_package_data=True,
    install_requires=[],
    setup_requires=['pytest-runner', ],
    tests_require=['pytest', ],
    zip_safe=False,
    cmdclass={'build': CustomBuild}
)
