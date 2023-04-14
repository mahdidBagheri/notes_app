from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from notesapp.notes import router as notes_router

app = FastAPI(title='notes app', description='my notes app', version='1.0')

app.include_router(notes_router.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)