# PDFToEPUB

> _"I got an ebook but life bombarded me with PDFs that is incompatible with my ebook."_
>
> From Richie Kho

PDFToEPUB is a small python application that does exactly as its name, convert PDF to EPUB.
This project is born from the frustration of unable to read PDFs on my ebook while tired of some document conversion services that doesn't handle PDF well.

The software is decent with plain text with images and tables.
However, it is not very good with lists and headings.
But at least the plain text are readable, which satisfies my need.
The sample PDF file and resulting EPUB file are included under `sample` directory.

## Usage

To set this thing up, you'll need to install some dependencies.
It is up to your preferences to install it in a virtual environemnt or globally.

```sh
pip install -r requirements.txt
```

Then you'll be able to run the program.

```sh
python <DIRECTORY_TO_THIS_REPOSITORY> <PATH_TO_PDF_FILE>
```

It will return the path of the resulting epub file, which you can copy it out.

The file generated are all cached, to remove the cache in prior, use `--clean-first` flag (or `-c`).
