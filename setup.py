from distutils.core import setup
import os

setup(
    name         = 'goto',
    version      = '1.0.5',
    author       = 'Bianca Subion',
    author_email = 'biancasubion@gmail.com',
    license      = 'GPL3',
    description  = 'Awesome url shortener'
    url          = 'https://github.com/biancasubion/goto',
    install_requires = [
        'Flask >= 0.11.1',
    ]
)
