# also available through the world wide web at this URL:
# http://opensource.org/licenses/OSL-3.0
# If you did not receive a copy of the license and are unable to obtain it
# Copyright (c) 2008 - 2013, EllisLab, Inc. (http://ellislab.com/)
# http://opensource.org/licenses/OSL-3.0 Open Software License (OSL 3.0)

if __name__=='__main__':
    from setuptools import find_namespace_packages, find_packages, setup
    from setuptools import Command

    PKG_DIR = 'centerface'
    PYTHON_REQUIRES = '>=3.6'

    setup(
        name                 = 'centerface',
        version              = '0.1.0',
        python_requires      = PYTHON_REQUIRES,
        packages             = find_namespace_packages(include=[f'{PKG_DIR}']), #, exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
        install_requires     = ['opencv-python','numpy'],
        include_package_data = True,
        package_data         = {
            "centerface" : ["*.onnx"],
        }
    )
