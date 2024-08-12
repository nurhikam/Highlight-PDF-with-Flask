import fitz # PyMuPDF
import re   # Regex

class PDFHighlighter:
    def __init__(self, input_pdf_path, output_pdf_path):
        self.input_pdf_path = input_pdf_path
        self.output_pdf_path = output_pdf_path

    def highlight_text(self, search_text):
        doc = fitz.open(self.input_pdf_path)

        # Split pencarian text dengan chunks
        search_words = search_text.split()
        min_chunk_length = 6
        max_chunk_length = 9
        search_chunks = []

        i = 0
        while i < len(search_words):
            chunk = search_words[i:i + max_chunk_length]
            if len(chunk) >= min_chunk_length:
                search_chunks.append(' '.join(chunk))
            i += max_chunk_length

        # Variabel untuk menyimpan halaman dengan highlight paling banyak
        max_highlights = 0
        page_with_max_highlights = None

        # Iterasi halaman di PDF
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)

            # Mencari dan meng-highlight setiap chunk pada halaman
            highlights_count = 0
            for chunk in search_chunks:
                text_instances = page.search_for(chunk)
                if text_instances:
                    highlights_count += len(text_instances)
                    for inst in text_instances:
                        highlight = page.add_highlight_annot(inst)
                        highlight.update()

            # Save halaman dengan highlight paling banyak
            if highlights_count > max_highlights:
                max_highlights = highlights_count
                page_with_max_highlights = page_num

        # Save PDF yang sudah dihighlight
        doc.save(self.output_pdf_path)

        return page_with_max_highlights


class LegalTextFormatter:
    @staticmethod
    def format_legal_text(text):
        text = re.sub(r'(?<!dalam )\bPasal (\d+)', r'\nPasal \1\n', text)
        text = re.sub(r'(?<!ayat )\((\d+)\)\s', r'\n(\1) ', text)

        text = re.sub(r':\s*', ':\n    ', text)
        text = re.sub(r';\s*', ';\n    ', text)
        text = re.sub(r';\s*atau', '; atau\n   ', text)
        text = re.sub(r';\s*dan', '; dan\n   ', text)

        text = text.replace('\n \n', '\n')
        return text

    @staticmethod
    def normalize_enter_removed(text):
        result = text.replace('\n', ' ')
        return result.strip()

    @staticmethod
    def normalize_space(text):
        result = ' '.join(filter(None, text.split(' ')))
        return result.strip()

    @staticmethod
    def format_output(text):
        text = LegalTextFormatter().normalize_enter_removed(text)
        text = LegalTextFormatter().normalize_space(text)
        text = LegalTextFormatter().format_legal_text(text)
        return text
