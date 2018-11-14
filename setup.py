import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(
    name='django-anypayment',
    version='0.1',
    packages=['anypayment'],
    description='A Django library to implement payment gateways in hassle free way',
    long_description=README,
    author='sampath nagarajan',
    author_email='mesampathhere@gmail.com',
    url='https://github.com/codyowl/django-anypayment.git',
    license='MIT',
    install_requires=[
        'Django>=1.8,
    ]
)