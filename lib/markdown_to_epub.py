import os
import pypandoc
from pathlib import Path

from .singleton import Singleton

class MarkdownToEPUB(metaclass=Singleton):
    """
    A converter that converts markdown to EPUB
    """

    CACHE_DIR_PATH = Path(__file__).parent / 'markdown_to_epub_cache.d.local'

    def __init__(self):
        os.makedirs(MarkdownToEPUB.CACHE_DIR_PATH, exist_ok=True)

    def __call__(self, path: Path, name : str = None) -> Path:
        """
        Process a Markdown and return the path of the processed document, which is the resultant epub.
        """

        file_cache_key = path.name if name == None else name
        file_cache_content_path = MarkdownToEPUB.CACHE_DIR_PATH / f"{file_cache_key}.epub"

        if not file_cache_content_path.exists():
            pypandoc.convert_file(path, "epub", outputfile=file_cache_content_path)
        
        return file_cache_content_path

    def purge() -> None:
        for p in MarkdownToEPUB.CACHE_DIR_PATH.glob("*"):
            if p.exists(): os.removedirs(p)