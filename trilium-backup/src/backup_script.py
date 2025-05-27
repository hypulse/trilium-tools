from trilium_py.client import ETAPI
from datetime import datetime
import os
import zipfile

api_origin_url = os.getenv("API_ORIGIN")
api_access_token = os.getenv("API_TOKEN")

current_datetime_formatted = datetime.now().strftime("%Y%m%d-%H%M%S")
backup_folder_path = f"/backups/{current_datetime_formatted}"
os.makedirs(backup_folder_path, exist_ok=True)
backup_file_path = os.path.join(backup_folder_path, "backup.zip")

trilium_client = ETAPI(api_origin_url, api_access_token)
trilium_client.export_note("root", "html", backup_file_path)

with zipfile.ZipFile(backup_file_path, "r") as zip_ref:
    zip_ref.extractall(backup_folder_path)

os.remove(backup_file_path)
