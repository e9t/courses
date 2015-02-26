# Course pages

## Requirements

    pip install pelican ghp-import

## Generation

    git init
    pelican-quickstart

    > Where do you want to create your new web site? [.]
    > What will be the title of this web site? Course pages - Lucy Park
    > Who will be the author of this web site? Lucy Park
    > What will be the default language of this web site? [en] 
    > Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) y
    > What is your URL prefix? (see above example; no trailing slash) http://lucypark.kr/courses
    > Do you want to enable article pagination? (Y/n) y
    > How many articles per page do you want? [10]  
    > Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n) y
    > Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n) y
    > Do you want to upload your website using FTP? (y/N) n
    > Do you want to upload your website using SSH? (y/N) n
    > Do you want to upload your website using Dropbox? (y/N) n
    > Do you want to upload your website using S3? (y/N) n
    > Do you want to upload your website using Rackspace Cloud Files? (y/N) n
    > Do you want to upload your website using GitHub Pages? (y/N) y
    > Is this your personal page (username.github.io)? (y/N) n

    sudo pelican-themes --install ~/dev/pkgs/python/pelican-themes/aboutwilson --verbose
    pelican source/content  -s source/pelicanconf.py

## Run

    make regenerate; make serve
    make publish
    make github
