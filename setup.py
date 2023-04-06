from setuptools import setup

setup(
    name='my-cli-tool',
    version='0.1.0',
    py_modules=['my_cli_tool'],
    install_requires=[
        'pydub',
    ],
    entry_points='''
        [console_scripts]
        my-cli-tool=my_cli_tool:cli
    '''
)