from setuptools import setup

setup(
    name='app-example',
    version='0.0.1',
    author='Petr',
    author_email='hidden@gmail.com',
    description='FastApi app',
    install_requires=[
        'fastapi',
        'uvicorn',
        'loguru',
        'pandas',
        'sklearn'
    ],
    scripts=['app/main.py']
)
