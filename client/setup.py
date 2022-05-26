from setuptools import find_packages, setup

from honeypot import __version__

requirements = [
    # 'cryptography==3.0',
    "Twisted==22.4.0",
    "pyasn1==0.4.5",
    "docker==5.0.0",
    "simplejson==3.16.0",
    "requests==2.21.0",
    "zope.interface==5.0.0",
    "PyPDF2==1.26.0",
    "fpdf==1.7.2",
    "passlib==1.7.1",
    "Jinja2==2.11.3",
    "ntlmlib==0.72",
    "bcrypt==3.1.7",
    "hpfeeds==3.0.0",
]


setup(
    name="honeypot",
    version=__version__,
    url="https://github.com/darlling",
    author="20175415-何万有",
    author_email="microinner@outlook.com",
    description="Honeypot daemon",
    long_description="A low interaction honeypot intended to be run on internal networks.",
    install_requires=requirements,
    license="BSD",
    packages=find_packages(exclude="test"),
    scripts=["bin/honeypotd", "bin/honeypot.tac"],
    platforms="any",
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Framework :: Twisted",
        "Topic :: System :: Networking",
        "Topic :: Security",
        "Topic :: System :: Networking :: Monitoring",
        "Natural Language :: English",
        "Operating System :: Unix",
        "Operating System :: POSIX :: Linux",
        "Operating System :: POSIX :: BSD :: FreeBSD",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: BSD License",
    ],
)
