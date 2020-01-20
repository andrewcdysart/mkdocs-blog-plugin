
from distutils.core import setup

setup(
    name="mkdocs-blog-plugin",
    version="0.1.3",
    author="Francesco Maida",
    author_email="francesco.maida@gmail.com",
    packages=["mkdocs_blog"],
    url='https://github.com/fmaida/mkdocs-blog-plugin',
    license="LICENSE.txt",
    description="Keeps a really simple blog section inside your MkDocs site.",
    install_requires=[
        "dateparser",
    ],

    entry_points={
        "mkdocs.plugins": [
            "blog = mkdocs_blog:Blog",
        ]
    }
)

