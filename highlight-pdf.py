import fitz  # PyMuPDF

def highlight_text_in_pdf(input_pdf_path, output_pdf_path, search_text):
    # Buka file PDF
    doc = fitz.open(input_pdf_path)

    # Split pencarian text dengan chunks 6-9 kata
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
    doc.save(output_pdf_path)

    return page_with_max_highlights


input_pdf_path = 'UU.pdf'
output_pdf_path = 'output.pdf'
input_text = (
    "Pasal 72 (1) Untuk kepentingan pemeriksaan dalam perkara tindak pidana Pencucian Uang, penyidik, penuntut umum, atau hakim berwenang meminta Pihak Pelapor untuk memberikan keterangan secara tertulis mengenai Harta Kekayaan dari: a. orang yang telah dilaporkan oleh PPATK kepada penyidik; b. tersangka; atau c. terdakwa. (2) Dalam meminta keterangan sebagaimana dimaksud pada ayat (1), bagi penyidik, penuntut umum, atau hakim tidak berlaku ketentuan peraturan perundang undangan yang mengatur rahasia bank dan kerahasiaan Transaksi Keuangan lain. (3) Permintaan keterangan sebagaimana dimaksud pada ayat (1) harus diajukan dengan menyebutkan secara jelas mengenai: a. nama dan jabatan penyidik, penuntut umum, atau hakim; b. identitas orang yang terindikasi dari hasil analisis atau pemeriksaan PPATK, tersangka, atau terdakwa; c. uraian singkat tindak pidana yang disangkakan atau didakwakan; dan d. tempat Harta Kekayaan berada. (4) Permintaan sebagaimana dimaksud pada ayat (3) harus disertai dengan: a. laporan polisi dan surat perintah penyidikan; b. surat penunjukkan sebagai penuntut umum; atau c. surat penetapan majelis hakim."
)

page_with_max_highlights = highlight_text_in_pdf(input_pdf_path, output_pdf_path, input_text)

print(f"Index Halaman dengan highlight paling banyak: {page_with_max_highlights}")


