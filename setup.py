import os
from os.path import join
import sys
from setuptools import setup
from setuptools import find_packages

# import pypandoc
# long_description = pypandoc.convert('README.md', 'rst')
long_description = ""

def setup_package():
    src_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    old_path = os.getcwd()
    os.chdir(src_path)
    sys.path.insert(0, src_path)

    needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
    pytest_runner = ['pytest-runner'] if needs_pytest else []

    setup_requires = [] + pytest_runner
    install_requires = ['numpy>=1.9', 'numba>=0.28']
    tests_require = ['pytest']

    metadata = dict(
        name='limix_genetics',
        version='0.1.0',
        maintainer="Danilo Horta",
        maintainer_email="horta@ebi.ac.uk",
        license="MIT",
        description="Genetic related tools for Limix.",
        long_description=long_description,
        url='http://github.com/glimix/limix-genetics',
        packages=find_packages(),
        zip_safe=True,
        install_requires=install_requires,
        tests_require=tests_require,
        setup_requires=setup_requires,
        include_package_data=True,
    )

    try:
        setup(**metadata)
    finally:
        del sys.path[0]
        os.chdir(old_path)


if __name__ == '__main__':
    setup_package()
