#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Version : Python 3.6

import json
import argparse
import re
import os
import xml.etree.ElementTree as ET


def get_text(block):
    block_text = []
    for elem in block.findall('p'):
        text = elem.text
        if text is None:
            continue
        text = re.sub(r'\n+', ' ', text)
        text = re.sub(r'\s+', ' ', text)
        block_text.append(text)
    return block_text


def extract_xml(filename, publication_date):
    tree = ET.parse(filename)
    root = tree.getroot()
    head = root.find('head')
    body = root.find('body')

    title = head.findtext('title')
    docid = '{:0>7s}'.format(head.find('docdata').find('doc-id').attrib['id-string'])

    body_block = body.find('body.content').findall('block')
    if (len(body_block)) == 0:
        full_text = []
    else:
        for block in body_block:
            if block.attrib['class'] == 'full_text':
                full_text = get_text(block)
                break

    return dict(
        docid=docid,
        publication_date=publication_date,
        title=title,
        full_text=full_text,
    )


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.description = 'untar subfile in `New York Times Annotated Corpus`'
    parser.add_argument('--path_dir', type=str, default='./nyt_corpus/data', help='dir for corpus `data` folder')
    parser.add_argument('--path_des', type=str, default='./nyt_corpus.json', help='path for extracting results')
    args = parser.parse_args()

    print('start to extract ...')
    fw = open(args.path_des, 'w', encoding='utf-8')
    for year in range(1987, 2008):
        for month in range(1, 13):
            for day in range(1, 32):
                file_dir = os.path.join(args.path_dir, '{}/{:0>2d}/{:0>2d}'.format(year, month, day))
                if not os.path.exists(file_dir):
                    continue
                publication_date = '{:0>4d}-{:0>2d}-{:0>2d}'.format(year, month, day)
                file_list = os.listdir(file_dir)
                file_list = sorted(file_list, key=lambda x: int(x[:-4]), reverse=False)
                for filename in file_list:
                    path_src = os.path.join(file_dir, filename)
                    print(path_src)
                    res = extract_xml(path_src, publication_date)
                    json.dump(res, fw, ensure_ascii=False)
                    fw.write('\n')
    fw.close()
