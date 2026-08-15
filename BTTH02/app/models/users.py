from sqlalchemy import Column, Integer, String
from app.database import Base

class MedicalStaffModel(Base):
    __tablename__ = "medical_staffs"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(150), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False)
