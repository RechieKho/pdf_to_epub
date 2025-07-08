import argparse
from lib import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser( 
        prog='pdf_to_epub', 
        description='Convert PDF files to EPUB files.'
    )
    parser.add_argument('filepath')
    parser.add_argument('-c', '--clean-first', action='store_true')
    args = parser.parse_args()
    CLEAN_FIRST = args.clean_first
    FILEPATH = Path(args.filepath)

    if CLEAN_FIRST:
        purge()

    print(convert(FILEPATH))
    
