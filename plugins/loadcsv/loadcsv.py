#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Template CSV loader
-------------------
Authored by Lucy Park <me@lucypark.kr>, 2015
Released under the BSD 2-Clause License (http://opensource.org/licenses/BSD-2-Clause)
"""

import re

from pelican import signals

def csv_loader(csv_elem, encoding='utf-8', linefeed='\n', delim=',', classes=['table']):
    if "'''" in csv_elem:
        doc = csv_elem.split("'''")[1]
    else:
        filepath = csv_elem.split("'")[1]
        print filepath
        with open(filepath, 'r') as f:
            doc = f.read().decode(encoding)

    if classes:
        csv_string = '<table class="%s">' % ' '.join(classes)
    else:
        csv_string = '<table>'
    for i, row in enumerate(filter(None, doc.split(linefeed))):
        if i==0:
            csv_string += '<tr><th>%s</th></tr>' % '</th><th>'.join(row.split(delim))
        else:
            csv_string += '<tr><td>%s</td></tr>' % '</td><td>'.join(row.split(delim))
    csv_string += '</table>'

    return csv_string

def loadcsv(data_passed_from_pelican):
    """A function to read through each page and post as it comes through from Pelican, find all instances of triple-backtick (```...```) code blocks, and add an HTML wrapper to each line of each of those code blocks"""

    if data_passed_from_pelican._content: # If the item passed from Pelican has a "content" attribute (i.e., if it's not an image file or something else like that)
    # NOTE: `data_passed_from_pelican.content` seems to be read-only, whereas `data_passed_from_pelican._content` is able to be overwritten. (Mentioned by Jacob Levernier in his Better Code-Block Line Numbering Plugin)
        page_content = data_passed_from_pelican._content
    else:
        return # Exit the function, essentially passing over the (non-text) file.

    all_csv_elements = re.findall('{% csv .*? %}', page_content, re.DOTALL) # re.DOTALL puts python's regular expression engine ('re') into a mode where a dot ('.') matches absolutely anything, including newline characters.

    if(len(all_csv_elements) > 0):
        updated_page_content = page_content

    for csv_elem in all_csv_elements:
        replacement = csv_loader(csv_elem)
        updated_page_content = updated_page_content.replace(csv_elem, replacement)

        data_passed_from_pelican._content = updated_page_content

def register():
    signals.content_object_init.connect(loadcsv)
