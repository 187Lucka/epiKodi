from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import FileResponse
import os

router = APIRouter()

@router.get("/api/movies/{id}")
async def getmovies(id: int, quality: str = Query("720p")):
    video_directory = "./videos"
    video_filename = f"{id}_{quality}.mp4"
    video_path = os.path.join(video_directory, video_filename)

    if not os.path.exists(video_path):
        raise HTTPException(status_code=404, detail="Movie not found")

    return FileResponse(video_path, media_type='video/mp4')
