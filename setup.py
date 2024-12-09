from setuptools import setup, find_packages

setup(
    name="tweety-ns",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "beautifulsoup4[lxml]>=4.12,<5.0",
        "openpyxl",
        "httpx[http2]",
        "python-dateutil",
        "anticaptchaofficial",
        "capsolver",
        "2captcha-python",
        "filetype"
    ],
)
