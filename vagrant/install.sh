#!/bin/bash
vagrant up 
curl -O https://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.10.1.tar.gz
tar xzf virtualenv-1.10.1.tar.gz
rm virtualenv-1.10.1.tar.gz
python virtualenv-1.10.1/virtualenv.py --no-site-packages venv
rm -rf virtualenv-1.10.1
venv/bin/pip install -r requirements.txt
./update.sh
