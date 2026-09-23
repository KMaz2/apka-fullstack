from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import SessionLocal, Produkt

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/produkty")
def pobierz_produkty():
    db: Session = SessionLocal()
    rows = db.query(Produkt).all()
    db.close()

    return [
        {
            "id": produkt.id,
            "nazwa_produktu": produkt.nazwa_produktu,
            "cena": produkt.cena,
            "image_url": produkt.image_url,
        }
        for produkt in rows
    ]