import sys
from pathlib import Path


JPEG_IMAGES = []
JPG_IMAGES = []
SVG_IMAGES = []
PNG_IMAGES = []
MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []
OTHER = []
ARCHIVES = []
AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []
DOC_DOCUMENTS = []
DOCX_DOCUMENTS = []
TXT_DOCUMENTS = []
PPTX_DOCUMENTS = []
PDF_DOCUMENTS = []
XLSX_DOCUMENTS = []
CSV_DOCUMENTS = []
FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()

REGISTER_EXTENSIONS = {
    'JPEG': JPEG_IMAGES,
    'JPG': JPG_IMAGES,
    'PNG': PNG_IMAGES,
    'SVG': SVG_IMAGES,
    'MP3': MP3_AUDIO,
    'AMR': AMR_AUDIO,
    'WAV': WAV_AUDIO,
    'OGG': OGG_AUDIO,
    'GZ': ARCHIVES,
    'TAR': ARCHIVES,
    'ZIP': ARCHIVES,
    'MP4': MP4_VIDEO,
    'MOV': MOV_VIDEO,
    'MKV': MKV_VIDEO,
    'AVI': AVI_VIDEO,
    'DOC': DOC_DOCUMENTS,
    'DOCX': DOCX_DOCUMENTS,
    'PPTX': PPTX_DOCUMENTS,
    'TXT': TXT_DOCUMENTS,
    'PDF': PDF_DOCUMENTS,
    'XLSX': XLSX_DOCUMENTS,
    'CSV': CSV_DOCUMENTS
}

def get_extensions(filename: str) -> str:
    # перетворюємо розширення файлу в назву папки .txt -> TXT
    return Path(filename).suffix[1:].upper()  # .txt.upper() -> .TXT  [1:] -> txt.upper() -> TXT


# C:/Users/pc/Desktop/заняття/hw_tigran/lesson15_16/task1.txt -> item.name -> task1.txt
def scan(folder: Path) -> None:
    for item in folder.iterdir():
        # якщо це папка то додаємо в список FOLDERS і переходимо до наступного елементу
        if item.is_dir():
            # перевіряємо щоб ця папка не була тою в яку ми складаємо наші файли
            if item.name not in ('achives', 'video', 'audio', 'documents', 'images', 'OTHER'):
                FOLDERS.append(item)
                # скануємо вкладену папку(рекурсія)
                scan(item)
            # перейти до наступного елементу в нашій папці
            continue

        # пішла робота з файлом
        ext = get_extensions(item.name) # беремо розширення 'TXT'
        fullname = folder / item.name  # C:/Users/pc/Desktop/заняття/hw_tigran/lesson15_16(folder) / task1.txt(item.name)
        if not ext: # якщо у файла немає розширення додати до невідомих
            OTHER.append(fullname)
        else:
            try:
                # взяти список куди покласти повний шлях до файлу
                container = REGISTER_EXTENSIONS[ext]  # REGISTER_EXTENSIONS[ext] -> REGISTER_EXTENSIONS['TXT'] -> TXT_DOCUMENTS, []
                EXTENSIONS.add(ext)  # 'TXT'
                container.append(fullname)
            except KeyError:
                # якщо ми не зареєстрували розширення в REGISTER_EXTENSIONS, то додати в UNKNOWN
                UNKNOWN.add(ext)
                OTHER.append(fullname)


if __name__ == "__main__":
    folder_for_scan = sys.argv[1]
    print(f'Start in folder: {folder_for_scan}')

    scan(Path(folder_for_scan))
    print(f'Images jpeg: {JPEG_IMAGES}')
    print(f'Images jpg: {JPG_IMAGES}')
    print(f'Images png: {PNG_IMAGES}')
    print(f'Images svg: {SVG_IMAGES}')

    print(f'Audio mp3: {MP3_AUDIO}')
    print(f'Audio wav: {WAV_AUDIO}')
    print(f'Audio amr: {AMR_AUDIO}')
    print(f'Audio ogg: {OGG_AUDIO}')

    print(f'Documents txt: {TXT_DOCUMENTS}')