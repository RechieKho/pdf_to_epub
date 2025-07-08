import os
from pathlib import Path
from docling_core.types.doc import ImageRefMode
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption

from .singleton import Singleton

class PDFToMarkdown(metaclass=Singleton):
    """
    A converter that converts PDF to markdown.
    """

    CACHE_DIR_PATH = Path(__file__).parent / 'pdf_to_markdown_cache.d.local'

    def __init__(self, image_scale=2.0):
        pipeline_options = PdfPipelineOptions()
        pipeline_options.images_scale = image_scale
        pipeline_options.generate_page_images = True
        pipeline_options.generate_picture_images = True
        pipeline_options.allow_external_plugins = True

        self._converter = DocumentConverter(
            format_options={
                InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options),
            }
        )

        os.makedirs(PDFToMarkdown.CACHE_DIR_PATH, exist_ok=True)
    
    def __call__(self, path: Path, name : str = None) -> Path:
        """
        Process a PDF and return the path of the processed document, which is the resultant markdown.
        """

        file_cache_key = path.name if name == None else name
        file_cache_dir_path = PDFToMarkdown.CACHE_DIR_PATH / f"{file_cache_key}.d"
        file_cache_content_path = file_cache_dir_path / "content.md"

        if not file_cache_content_path.exists():
            processed_doc = self._converter.convert(path)
            os.makedirs(file_cache_dir_path, exist_ok=True)
            processed_doc.document.save_as_markdown(file_cache_content_path, artifacts_dir=file_cache_dir_path, image_mode=ImageRefMode.REFERENCED)
        
        return file_cache_content_path
    
    def purge() -> None:
        for p in PDFToMarkdown.CACHE_DIR_PATH.glob("*"):
            if p.exists(): os.removedirs(p)