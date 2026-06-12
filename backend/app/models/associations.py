from sqlalchemy import Column, Integer, ForeignKey

from app.models.base import Base

class RolStack(Base):
    __tablename__ = "rol_stack"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_rol = Column(Integer, ForeignKey("rol.id"))
    id_stack = Column(Integer, ForeignKey("global_stack.id"))

class OfferStack(Base):
    __tablename__ = "offer_stack"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_offer = Column(Integer, ForeignKey("offer.id"))
    id_stack = Column(Integer, ForeignKey("global_stack.id"))

class ResourceStack(Base):
    __tablename__ = "resource_stack"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_resource = Column(Integer, ForeignKey("resource.id"))
    id_stack = Column(Integer, ForeignKey("global_stack.id"))