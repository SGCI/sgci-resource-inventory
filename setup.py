from setuptools import setup

setup(
    name="sgci-resource-inventory",
    install_requires=[
        'requests',
        'simplejson',
        'sphinx-jsonschema',
        'msmb_theme'],
    extras_require={
        'tests': [
            'nose',
            'pycodestyle >= 2.1.0'],
        'docs': [
            'sphinx >= 1.4',
            'sphinx_rtd_theme',
            'sphinx-jsonschema',
            'msmb_theme']}
)
