from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from app.services.security import MEDCARE_SECRET_KEY, ALGORITHM

router = APIRouter(prefix="/api/v1/prescriptions", tags=["Prescriptions"])
security = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(credentials.credentials, MEDCARE_SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token đã hết hạn")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token không hợp lệ")

def require_doctor(payload: dict = Depends(verify_token)):
    if payload.get("role") != "doctor":
        raise HTTPException(status_code=403, detail="Không đủ quyền hạn. Chỉ bác sĩ mới được phép thực hiện.")
    return payload

@router.post("")
def create_prescription(payload: dict = Depends(require_doctor)):
    return {"message": "Tạo đơn thuốc thành công", "doctor": payload.get("sub")}

@router.get("/view")
def view_prescriptions(payload: dict = Depends(verify_token)):
    return {"message": "Danh sách đơn thuốc", "viewer": payload.get("sub"), "role": payload.get("role")}
