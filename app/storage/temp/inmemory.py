import tempfile
import hashlib
from typing import Dict, Any
from starlette.responses import FileResponse


class InMemoryDocumentStore:

    def __init__(self):
        self._objects: Dict[str, Dict[str, Any]] = {}

    async def put(
        self,
        key: str,
        name: str,
        content_type: str,
        data: bytes
    ) -> Dict[str, Any]:
        file_hash = hashlib.sha256(data).hexdigest()
        self._objects[key] = {
            "bytes": data,
            "content_type": content_type,
            "name": name,
            "hash": file_hash,
            "size": len(data)
        }

        return {
            "key": key,
            "hash": file_hash,
            "size": len(data)
        }
    
    async def get(
        self,
        key: str
    ) -> Dict[str, Any]:
        if key not in self._objects:
            raise KeyError("Not found")
        return self._objects[key]
    
    async def delete(
        self,
        key: str
    ) -> None:
        self._objects.pop(key, None)

    async def preview_response(
        self,
        key: str
    ) -> FileResponse:
        obj = await self.get(key)
        data = obj["bytes"]
        content_type = obj["content_type"]

        file_ext = _get_file_ext(content_type)
        with tempfile.NamedTemporaryFile(delete=False, suffix=file_ext) as tmp:
            tmp.write(data)
            path = tmp.name

        return FileResponse(path, media_type=content_type)
        

def _get_file_ext(
    content_type: str
) -> str:
    ext_mapping = {
        "application/pdf": ".pdf",
        "image/png": ".png",
        "image/jpeg": ".jpg",
        "image/gif": ".gif",
        "text/plain": ".txt"
    }
    return ext_mapping.get(content_type, "")