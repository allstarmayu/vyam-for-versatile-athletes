import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Vyam - For Versatile Athletes! Created by Maddy"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "Vyam API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=True
    )