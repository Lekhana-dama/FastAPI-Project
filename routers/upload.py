from fastapi import APIRouter,UploadFile,File,HTTPException
from pathlib import Path
import uuid


router=APIRouter(
    prefix="/upload",
    tags=["File upload"]
)
UPLOAD_DIR=Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

MAX_FILE_SIZE=5*1024*1024
@router.post("/")
async def upload_file(file:UploadFile=File(...)):
    if file.content_type not in ["image/jpeg","image/png"]:
        raise HTTPException(
            status_code=400,
            detail="only jpg and PNG files are allowed"
        )
    file_size=0
    extension=Path(file.filename).suffix
    random_file=f"{uuid.uuid4().hex}{extension}"
    file_path=UPLOAD_DIR/file.filename
    with file_path.open("wb") as buffer:
        while chunk:=await file.read(1024*1024):
            file_size+=len(chunk)
            if file_size> MAX_FILE_SIZE:
                buffer.close()
                file_path.unlink(missing_ok=True)
                raise HTTPException(
                    status_code=413,
                    detail="File size must be less than 5MB"
                )
            buffer.write(chunk)

        
    return {
        "message":"file uploaded successfully",
        "filename":random_file,
        "content_type":file.content_type,
        "Size":file_size,
        "URL":f"/uploads/{random_file}"
    }