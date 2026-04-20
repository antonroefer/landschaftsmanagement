from __future__ import annotations

import argparse
from pathlib import Path

from docling.document_converter import DocumentConverter


def convert_pdfs_in_directory(input_dir: Path, overwrite: bool = False) -> None:
    """Convert all PDFs in a directory to Markdown files next to each PDF."""
    if not input_dir.exists():
        raise FileNotFoundError(f"Input directory does not exist: {input_dir}")

    pdf_files = sorted(input_dir.glob("*.pdf"))
    if not pdf_files:
        print(f"No PDF files found in: {input_dir}")
        return

    converter = DocumentConverter()

    for pdf_file in pdf_files:
        md_file = pdf_file.with_suffix(".md")

        if md_file.exists() and not overwrite:
            print(f"Skipping existing Markdown: {md_file.name}")
            continue

        try:
            result = converter.convert(str(pdf_file))
            markdown = result.document.export_to_markdown()
            md_file.write_text(markdown, encoding="utf-8")
            print(f"Converted: {pdf_file.name} -> {md_file.name}")
        except Exception as exc:
            print(f"Failed to convert {pdf_file.name}: {exc}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert PDFs in a folder to Markdown using Docling."
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=Path("references") / "course-notes",
        help="Folder that contains PDF files.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing Markdown files.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    convert_pdfs_in_directory(input_dir=args.input_dir, overwrite=args.overwrite)


if __name__ == "__main__":
    main()
