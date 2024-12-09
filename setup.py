from setuptools import setup, find_packages

install_requires = [
    "beautifulsoup4[lxml]~=4.12",
    "openpyxl",
    "httpx[http2]",
    "dateutils",
    "anticaptchaofficial",
    "capsolver",
    "2captcha-python",
    "filetype"
]

setup(
    name='tweetype',
    version='2.0.7',
    license='MIT',
    description='An easy Twitter Scraper (forked and modified by FuseFairy)',
    author='Tayyab Kharl, FuseFairy',
    author_email='tayyabmahr@gmail.com, dd8611706@gmail.com',
    url='https://github.com/FuseFairy/tweetype',
    keywords=['TWITTER', 'TWITTER SCRAPE', 'SCRAPE TWEETS'],
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)
