from pathlib import Path

from .pdf_to_markdown import PDFToMarkdown
from .markdown_to_epub import MarkdownToEPUB

pdf_to_markdown_converter = PDFToMarkdown()
markdown_to_epub_converter = MarkdownToEPUB()

def purge() -> None:
    pdf_to_markdown_converter.purge()
    markdown_to_epub_converter.purge()

def convert(path: Path) -> Path:
    return markdown_to_epub_converter(pdf_to_markdown_converter(path), path.name)