from typing import Optional

from sqlalchemy import Float, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker

DB_URL = "sqlite:///produkty.db"


class Base(DeclarativeBase):
    pass


class Produkt(Base):
    __tablename__ = "produkty"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nazwa_produktu: Mapped[str] = mapped_column(String, nullable=False)
    cena: Mapped[float] = mapped_column(Float, nullable=False)
    image_url: Mapped[Optional[str]] = mapped_column(String, nullable=True)


engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


PRODUCTS = [
    Produkt(id=1, nazwa_produktu="Mleko", cena=4.50, image_url="https://images.unsplash.com/photo-1550583724-b2692b85b150?auto=format&fit=crop&w=800&q=80"),
    Produkt(id=2, nazwa_produktu="Chleb", cena=6.20, image_url="https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=800&q=80"),
    Produkt(id=3, nazwa_produktu="Jajka", cena=8.90, image_url="https://images.unsplash.com/photo-1518569656558-1f25e69d93d7?auto=format&fit=crop&w=800&q=80"),
    Produkt(id=4, nazwa_produktu="Maslo", cena=11.30, image_url="https://images.unsplash.com/photo-1589987600846-7d80d88926d8?auto=format&fit=crop&w=800&q=80"),
    Produkt(id=5, nazwa_produktu="Jogurt", cena=5.70, image_url="https://images.unsplash.com/photo-1488477181946-6428a0291777?auto=format&fit=crop&w=800&q=80"),
    Produkt(id=6, nazwa_produktu="Ser", cena=13.40, image_url="https://images.unsplash.com/photo-1486297678162-eb2a19b0a32d?auto=format&fit=crop&w=800&q=80"),
    Produkt(id=7, nazwa_produktu="Pomarancze", cena=9.10, image_url="https://images.unsplash.com/photo-1611080626919-7cf5a9dbab5b?auto=format&fit=crop&w=800&q=80"),
    Produkt(id=8, nazwa_produktu="Cukier", cena=3.80, image_url="https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?auto=format&fit=crop&w=800&q=80"),
]


def init_db() -> None:
    Base.metadata.create_all(bind=engine)

    db: Session = SessionLocal()
    try:
        for produkt in PRODUCTS:
            existing = db.get(Produkt, produkt.id)
            if existing is None:
                db.add(produkt)
            else:
                existing.nazwa_produktu = produkt.nazwa_produktu
                existing.cena = produkt.cena
                existing.image_url = produkt.image_url
        db.commit()
    finally:
        db.close()
