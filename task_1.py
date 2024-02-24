from pathlib import Path
import shutil

def copy_files(source_dir, destination_dir = "dist"):
    source_path = Path(source_dir)
    destination_path = Path(destination_dir)

    for source_file in source_path.iterdir():
        try:
            if source_file.is_file():
                # Отримуємо розширення файлу
                file_extension = source_file.suffix[1:]
                # Створюємо піддиректорію за розширенням, якщо її ще не існує
                destination_subdir = destination_path / file_extension
                destination_subdir.mkdir(parents=True, exist_ok=True)
                # Копіюємо файл у відповідну піддиректорію
                shutil.copy(source_file, destination_subdir)
            elif source_file.is_dir():
                # Якщо це директорія, викликаємо функцію рекурсивно
                copy_files(source_file, destination_path)
        except (PermissionError, FileNotFoundError) as e:
                print(f"An error occurred while copying {source_file}: {e}")

if __name__ == "__main__":
    copy_files("picture")