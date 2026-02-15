import os
import shutil

# Дефинираме пътя към папката, която искаме да почистим (обикновено Downloads)
# Използваме expanduser, за да работи на всяка операционна система
DOWNLOADS_PATH = os.path.expanduser("~/Downloads")

# Речник, който свързва разширенията с папки
FILE_TYPES = {
    "Documents": [".pdf", ".docx", ".txt", ".csv", ".xlsx", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Archives": [".zip", ".tar", ".rar", ".7z"],
    "Installers": [".exe", ".msi", ".dmg", ".pkg"]
}

def organize_files():
    if not os.path.exists(DOWNLOADS_PATH):
        print(f"Path {DOWNLOADS_PATH} not found.")
        return

    for filename in os.listdir(DOWNLOADS_PATH):
        filepath = os.path.join(DOWNLOADS_PATH, filename)

        # Пропускаме, ако е папка
        if os.path.isdir(filepath):
            continue

        # Взимаме разширението на файла
        _, extension = os.path.splitext(filename)
        extension = extension.lower()

        moved = False
        for folder_name, extensions in FILE_TYPES.items():
            if extension in extensions:
                folder_path = os.path.join(DOWNLOADS_PATH, folder_name)
                
                # Създаваме папката, ако не съществува
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                
                # Преместваме файла
                shutil.move(filepath, os.path.join(folder_path, filename))
                print(f"Moved: {filename} -> {folder_name}/")
                moved = True
                break
        
        if not moved and extension:
            # Опционално: местим непознатите файлове в папка "Others"
            others_path = os.path.join(DOWNLOADS_PATH, "Others")
            if not os.path.exists(others_path):
                os.makedirs(others_path)
            shutil.move(filepath, os.path.join(others_path, filename))

if __name__ == "__main__":
    print("Starting file organization...")
    organize_files()
    print("Done!")
