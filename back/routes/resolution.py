from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import FileResponse
import os

router = APIRouter()

@router.get("/api/resolution/{id}")
async def getmovies(id: int):
    video_directory = "./videos"

    videos = [video for video in os.listdir(video_directory) if video.startswith(f"{id}_") and video.endswith(".mp4")]
    resolutions = [video.split("_")[1].split(".")[0] for video in videos]

    return resolutions