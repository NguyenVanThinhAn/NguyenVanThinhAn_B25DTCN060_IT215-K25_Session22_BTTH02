# Kịch bản kiểm thử (Test Cases)

## Case 1: Bác sĩ đăng nhập thành công và gọi API tạo đơn thuốc
1. **Đăng ký bác sĩ**: `POST /api/v1/medical/register`
   - Body: `{"username": "dr_john", "password": "securepass123", "role": "doctor"}`
   - Result: HTTP 200, tạo tài khoản thành công.
2. **Đăng nhập bác sĩ**: `POST /api/v1/medical/login`
   - Body: `{"username": "dr_john", "password": "securepass123"}`
   - Result: Trả về `access_token` (JWT).
3. **Tạo đơn thuốc**: `POST /api/v1/prescriptions`
   - Headers: `Authorization: Bearer <access_token>`
   - Result: HTTP 200, `"Tạo đơn thuốc thành công"`.

## Case 2: Dược sĩ đăng nhập thành công nhưng gọi API tạo đơn thuốc bị từ chối
1. **Đăng ký dược sĩ**: `POST /api/v1/medical/register`
   - Body: `{"username": "phar_mary", "password": "pharmacistpass", "role": "pharmacist"}`
   - Result: HTTP 200.
2. **Đăng nhập dược sĩ**: `POST /api/v1/medical/login`
   - Body: `{"username": "phar_mary", "password": "pharmacistpass"}`
   - Result: Trả về `access_token`.
3. **Tạo đơn thuốc (bị từ chối)**: `POST /api/v1/prescriptions`
   - Headers: `Authorization: Bearer <access_token>`
   - Result: HTTP 403 Forbidden (`"Không đủ quyền hạn"`).
4. **Xem đơn thuốc (thành công)**: `GET /api/v1/prescriptions/view`
   - Headers: `Authorization: Bearer <access_token>`
   - Result: HTTP 200, hiển thị danh sách đơn thuốc.

## Case 3: Chặn token giả mạo (Fake Signature / Invalid Token)
1. **Sửa đổi token hợp lệ**: Lấy `access_token` từ bước đăng nhập, thay đổi một vài ký tự ở phần signature (phần cuối cùng sau dấu chấm).
2. **Gọi API bất kỳ**: `GET /api/v1/prescriptions/view`
   - Headers: `Authorization: Bearer <fake_access_token>`
   - Result: HTTP 401 Unauthorized (`"Token không hợp lệ"`).
