from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import MedicalStaffModel
from app.schemas import StaffRegister, StaffLogin
from app.services.security import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/api/v1/medical", tags=["Medical"])

@router.post("/register")
def register_staff(req: StaffRegister, db: Session = Depends(get_db)):
    existing = db.query(MedicalStaffModel).filter(MedicalStaffModel.username == req.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username đã tồn tại")
    
    new_staff = MedicalStaffModel(
        username=req.username,
        password_hash=hash_password(req.password),
        role=req.role
    )
    db.add(new_staff)
    db.commit()
    db.refresh(new_staff)
    return {"message": "Đăng ký thành công", "id": new_staff.id}

@router.post("/login")
def login_staff(req: StaffLogin, db: Session = Depends(get_db)):
    staff = db.query(MedicalStaffModel).filter(MedicalStaffModel.username == req.username).first()
    if not staff or not verify_password(req.password, staff.password_hash):
        raise HTTPException(status_code=401, detail="Thông tin đăng nhập không chính xác")
    
    token = create_access_token(username=staff.username, role=staff.role)
    return {"access_token": token, "token_type": "bearer"}
