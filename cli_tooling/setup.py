from setuptools import setup, find_packages
from pathlib import Path

cwd = Path(__file__).parent
req_path = cwd / 'requirements.txt'
reqs = req_path.read_text().split('\n')

setup(
    name="cli_print",
    version="1.0.0",
    packages=find_packages(),
    install_requires=reqs,
    include_package_data=True,
    package_data={
            'cli_print': ['images/*']
            },
    entry_points={'console_scripts': ['cli_print=cli_print.cli:cli_function']}
    )
