import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="affiliate_link_checker",
    version="0.0.1",
    author="Kristen Keller",
    description="Scrape and check affiliate links",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    package_dir={'': 'pkg'}
)
