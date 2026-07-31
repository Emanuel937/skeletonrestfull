import uuid
import os
from fastapi import UploadFile

UPLOAD_DIR = "uploads/media"

def save_media_file(file: UploadFile) -> str:
    
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    ext       = file.filename.split(".")[-1]
    file_id   = str(uuid.uuid4())
    filename  = f"{file_id}.{ext}"
    file_path = os.path.join(UPLOAD_DIR, filename)
    #---------------------------------------------
    # 
    #---------------------------------------------
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())
    return file_path
