import os
import zipfile

def extract_all_zip_files(directory: str) -> None:
    for foldername, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.lower().endswith('.zip'):
                zip_path = os.path.join(foldername, filename)
                extract_folder = os.path.join(foldername, filename[:-4])  # Remove .zip extension

                if os.path.exists(extract_folder):
                    print(f"Skipping: {zip_path} (already extracted to {extract_folder})")
                    continue

                os.makedirs(extract_folder, exist_ok=True)
                try:
                    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                        zip_ref.extractall(extract_folder)
                    print(f"Extracted: {zip_path} to {extract_folder}")
                except zipfile.BadZipFile:
                    print(f"Bad zip file: {zip_path}")

def main():
    ###USER INPUT###
    parent_directory = r"M:\ZipTest"
    extract_all_zip_files(parent_directory)

if __name__ == "__main__":
    main()