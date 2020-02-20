# NYTAC-toolkit
A toolkit to process New York Times Annotated Corpus ([LDC2008T19](https://catalog.ldc.upenn.edu/LDC2008T19)).
## Environment Requirements
* python 3.6
## Data 
* New York Times Annotated Corpus ([LDC2008T19](https://catalog.ldc.upenn.edu/LDC2008T19))

## Usage

1. Purchase data.
2. Uncompress the file and move it in this folder.
3. There are five subfiles in the folder: `data`, `docs`, `dtd`, `tools` and `index.html`. The data files in the `data` are compressed in the format `tgz`. In order to facilitate subsequent analysis process, use the following commad the unpack these files.
```
python untar.py
```
4. Start to extract `xml` files.
```
python extract.py 
```
## Result
The result of extraction is stored in `JSON` and one article per line. The specific format is as follows.
```json
{
    "docid": "1851160",
    "publication_date": "2007-06-01",
    "title": "Paid Notice: Deaths   ADLOWITZ, MARGARET",
    "full_text": [
        "ADLOWITZ--Margaret. Beloved sister of the late Ruth Lapin, Sylvia Hessek, Sam Adlow and Herman Adlowitz. Loving aunt to many nieces and nephews."
    ]
}
```

The example is in `example`  folder.

***Note***: Some articles' body text is empty and the corresponding `full_text` is an empty list.

## Reference Link
* https://github.com/rgormisky/LatentDirichletAllocation

## Related Link
* https://www.jianshu.com/p/cbba3e2dbdcd
* https://www.jianshu.com/p/35d21a1f22a9
* https://www.cnblogs.com/ifantastic/archive/2013/04/12/3017110.html
* https://www.cnblogs.com/insane-Mr-Li/p/9963875.html
