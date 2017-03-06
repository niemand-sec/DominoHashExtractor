# DominoHashExtractor v1.0

Coded By Joel Noguera - @niemand_sec

Lotus Notes clients store user credentials in the user.id file. This small scripts extracts the hash of the user from a user.id file in JTR format. 

You can submit just one file using the `-f` option, or submit a file with a list of all the user.id file names.

# Usage

```
usage: extractor.py [-h] [-l LIST] [-f FILE]

OPTIONS:
  -h, --help            show this help message and exit
  -l LIST, --list LIST  File Name of the list of user.id files
  -f FILE, --file FILE  File Name of only one user.id file

Example: python extractor.py -l ListFile python extractor.py -f FileName
```

