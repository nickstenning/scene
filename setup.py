from setuptools import setup, find_packages

setup(
    name='scene',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Pillow==1.7.5'
    ],
    entry_points={
        'console_scripts': [
            'scenedemo = scene.command:demo'
        ]
    }
)
