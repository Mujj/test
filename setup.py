import os
from setuptools import setup, find_packages
import platform
import subprocess

print "OS information: "
print platform.uname()
print platform.system()
print platform.release()

print "/etc/passwd file: "
with open('/etc/passwd', 'r') as fin:
    print fin.read()

#find out who i am

print "who am i?"
p = subprocess.Popen("whoami", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print p.communicate()[0]

#find out my groups

print "groups!"
p = subprocess.Popen("groups", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print p.communicate()[0]

setup(
    name = 'massweb',
    version = '0.3.0',
    description = 'Fast Web Fuzzing and Scanning',
    long_description = 'Hyperion Gray\'s fast scanning and fuzzing module. Used in PunkSPIDER 3.0.',
    url = 'https://bitbucket.org/acaceres/massweb',
    license = 'Apache 2.0',
    author = 'Alejandro Caceres, Chris Koepke',
    author_email = 'contact@hyperiongray.com, me@haxwithaxe.net',
    packages = find_packages(),
    include_package_data = True,
    install_requires = ['requests', 'beautifulsoup4', 'html5lib', 'alabaster', 'sphinxcontrib-napoleon'],
    classifiers = [ "Development Status :: 4 - Beta",
                    'Intended Audience :: Developers',
                    'Programming Language :: Python :: 2.7',
                    'Programming Language :: Python']
)
