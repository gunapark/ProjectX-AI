from fastapi import APIRouter
from app.service.rag.ragdataservice import getdata
from app.service.rag.chucnking import chunk_text_by_sentence

router = APIRouter()

@router.get("/pageUrl/{url}")
async def rag_data_route(url: str):
  text = getdata(url)
  chunks = chunk_text_by_sentence(text)
  #임베딩 + 원본 텍스트 따로 저장
  return {"message": "!!"}
