from module import pdf_referensi_tools as pdf_tools

# Contoh penggunaan PDFHighlighter
input_pdf = 'UU.pdf'
output_pdf = 'output.pdf'
input_text = (
    "contoh input text"
)

highlighter = pdf_tools.PDFHighlighter(input_pdf, output_pdf)
page_with_max_highlights = highlighter.highlight_text(input_text)
print(f"Index Halaman dengan highlight paling banyak: {page_with_max_highlights}")

# Contoh penggunaan LegalTextFormatter

formatter = pdf_tools.LegalTextFormatter()
formatted_text = formatter.format_output(input_text)
print(formatted_text)