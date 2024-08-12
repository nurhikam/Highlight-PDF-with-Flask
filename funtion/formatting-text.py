import re

def format_legal_text(text):
    text = re.sub(r'(?<!dalam )\bPasal (\d+)', r'\nPasal \1\n', text)
    text = re.sub(r'(?<!ayat )\((\d+)\)\s', r'\n(\1) ', text)

    text = re.sub(r':\s*', ':\n    ', text)
    text = re.sub(r';\s*', ';\n    ', text)
    text = re.sub(r';\s*atau', '; atau\n   ', text)
    text = re.sub(r';\s*dan', '; dan\n   ', text)

    text = text.replace('\n \n', '\n')
    return text

def normalize_enter_removed(text):
    result = text.replace('\n', ' ')
    return result.strip()

def normalize_space(text):
    result = ' '.join(filter(None, text.split(' ')))
    return result.strip()

# Contoh input
text = """
Pasal 48 (1) Direksi Bank dan KCBLN yang akan melakukan Integrasi wajib mengumumkan ringkasan rancangan Integrasi kepada masyarakat paling lambat: a. 2 (dua) hari kerja setelah diterima pemberitahuan dari OJK mengenai dapat dilanjutkannya proses pelaksanaan Integrasi berdasarkan hasil penelaahan yang dilakukan OJK sebagaimana dimaksud dalam Pasal 47; dan b. 30 (tiga puluh) hari sebelum pemanggilan RUPS Bank. (2) Pengumuman ringkasan rancangan Integrasi sebagaimana dimaksud pada ayat (1) paling sedikit memuat: a. ringkasan dari rancangan Integrasi sebagaimana dimaksud dalam Pasal 45; dan b. informasi bahwa rancangan Integrasi belum memperoleh persetujuan RUPS Bank. (3) Pengumuman sebagaimana dimaksud pada ayat (1) wajib dilakukan paling sedikit melalui: a. 1 (satu) surat kabar harian berbahasa Indonesia yang berperedaran nasional; dan b. Situs Web Bank dan KCBLN. (4) Bukti pengumuman sebagaimana dimaksud pada ayat (3) wajib disampaikan kepada OJK paling lambat 2 (dua) hari kerja setelah pengumuman.
Pasal 49 Direksi Bank dan KCBLN yang akan melakukan Integrasi wajib mengumumkan rencana Integrasi secara tertulis kepada karyawan dari Bank dan KCBLN yang melakukan Integrasi, bersamaan dengan pengumuman ringkasan rancangan Integrasi sebagaimana dimaksud dalam Pasal 48.



Pasal 63 Persetujuan atau penolakan OJK atas permohonan persetujuan prinsip sebagaimana dimaksud dalam Pasal 62 ayat (1) mengacu pada mekanisme yang diatur dalam peraturan perundang-undangan mengenai bank umum atau bank umum syariah.
Pasal 64 Direksi KCBLN yang akan melakukan Konversi wajib mengumumkan rencana Konversi secara tertulis kepada karyawan paling lambat 10 (sepuluh) hari sejak penyampaian permohonan izin Konversi sebagaimana dimaksud dalam Pasal 62.
Pasal 65 (1) Permohonan untuk memperoleh izin usaha Bank sebagai Bank hasil Konversi disampaikan oleh KCBLN kepada OJK setelah diperoleh persetujuan prinsip pendirian Bank sebagai Bank hasil Konversi. (2) Pemenuhan persyaratan dalam pengajuan permohonan untuk mendapatkan izin usaha Bank sebagai bank hasil Konversi sebagaimana dimaksud pada ayat (1) mengacu pada persyaratan untuk memperoleh izin usaha sebagaimana diatur dalam peraturan perundangundangan mengenai bank umum atau bank umum syariah, kecuali diatur khusus dalam Peraturan OJK ini. (3) Persyaratan sebagaimana dimaksud pada ayat (2), dilengkapi konsep berita acara pengalihan hak dan kewajiban dari KCBLN kepada Bank sebagai Bank hasil Konversi.
Pasal 66 (1) Rencana pelaksanaan Konversi KCBLN wajib diumumkan kepada masyarakat paling lambat 2 (dua) hari kerja setelah diperolehnya persetujuan prinsip pendirian Bank sebagai Bank hasil Konversi. (2) Pengumuman sebagaimana dimaksud pada ayat (1) wajib dilakukan paling sedikit melalui: a. 1 (satu) surat kabar harian berbahasa Indonesia yang berperedaran nasional; dan b. Situs Web KCBLN. (3) Bukti pengumuman sebagaimana dimaksud pada ayat (2) wajib disampaikan kepada OJK paling lambat 2 (dua) hari kerja setelah pengumuman.
Pasal 67 (1) Kreditur dapat mengajukan keberatan kepada KCBLN atas pelaksanaan Konversi dalam jangka waktu paling lambat 14 (empat belas) hari setelah pengumuman pelaksanaan Konversi sebagaimana dimaksud d
"""

text = normalize_enter_removed(text)
text = normalize_space(text)
formatted_text = format_legal_text(text)
print(formatted_text)
