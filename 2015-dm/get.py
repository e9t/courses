#! /usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import os

file_url = 'http://147.46.94.182:8888/~epark/tmp/mnist-original.mat'
file_path = 'mldata'

os.makedirs(file_path)
urllib.urlretrieve(file_url, '%s/mnist-original.mat' % file_path)

print("File successfully downloaded")
