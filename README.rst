ANP Crawler
-----------

install::

    sudo apt-get install python-devel python-virtualenv libffi-dev libxml2-dev libxslt-dev htop vim
    pip install -r requirements.txt

run::

    scrapy crawl anp_postos -o items.csv -t csv 
