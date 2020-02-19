#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Version : Python 3.6

import tarfile
import os
import argparse


def untar(path_src, path_des):
    """
    untar tar file
    """
    tar = tarfile.open(path_src, 'r:gz')
    names = tar.getnames()
    for name in names:
        tar.extract(name, path_des)
        print('{}/{}'.format(path_des, name))
    tar.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.description = 'untar subfile in `New York Times Annotated Corpus`'
    parser.add_argument('--path_dir', type=str, default='./nyt_corpus/data', help='dir for corpus `data` folder')
    args = parser.parse_args()

    print('start to untar ...')
    for year in range(1987, 2008):
        for month in range(1, 13):
            path_src = os.path.join(args.path_dir, '{}/{:0>2d}.tgz'.format(year, month))
            path_des = os.path.join(args.path_dir, '{}'.format(year))
            if os.path.exists(path_src):
                untar(path_src, path_des)
