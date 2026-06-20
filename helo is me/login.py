import streamlit as st
import os
import httpx
from authlib.integrations.httpx_client import OAuth2Client

st.set_page_config(page_title="Cổng Trạm Xanh", page_icon="🍊", layout="wide")

# --- CẤU HÌNH THÔNG TIN GOOGLE (Thay bằng thông tin của bạn) ---
# Mẹo: Nên để trong file .env hoặc st.secrets để bảo mật tốt hơn
CLIENT_ID = "713853831283-iogcgp77timt97fg2rljuk2n6q9lgf48.apps.googleusercontent.com"
CLIENT_SECRET = "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"
REDIRECT_URI = "http://localhost:8501/" # Trùng với cấu hình trên Google Cloud

# Các đường dẫn xác thực của Google
AUTHORIZATION_ENDPOINT = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN_ENDPOINT = "https://oauth2.googleapis.com/token"
USERINFO_ENDPOINT = "https://www.googleapis.com/oauth2/v3/userinfo"

# --- Hàm Load CSS Tổng ---
def load_local_css():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    css_path = os.path.join(root_dir, "style.css")
    if not os.path.exists(css_path): css_path = "style.css"
    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_local_css()

# --- CSS Ép màu ô chọn (Giữ nguyên giao diện Kawaii của bạn) ---
st.markdown("""
<style>
div[data-testid="stTabs"] {
    background-color: #ffffff; border: 3px solid var(--pink-300);
    border-radius: 20px; padding: 20px 30px 30px 30px;
    box-shadow: 6px 6px 0 var(--pink-100); margin-top: 10px;
}
div[data-testid="stTextInput"] input {
    border-radius: 12px !important; border: 2px solid var(--pink-200) !important;
    background-color: #FFF3E0 !important; color: #5D4037 !important;
    font-weight: 500; padding: 12px !important;
}
.divider {
    display: flex; align-items: center; text-align: center;
    color: #A1887F; font-weight: bold; font-size: 14px; margin: 20px 0;
}
.divider::before, .divider::after {
    content: ''; flex: 1; border-bottom: 1px dashed var(--pink-300);
}
.divider::before { margin-right: .5em; }
.divider::after { margin-left: .5em; }
</style>
""", unsafe_allow_html=True)

# --- XỬ LÝ BACKEND OAUTH GOOGLE ---
# Khởi tạo state để lưu thông tin user
if "user_info" not in st.session_state:
    st.session_state.user_info = None

# Kiểm tra xem có tham số 'code' từ Google trả về trên URL không
query_params = st.query_params
if "code" in query_params and st.session_state.user_info is None:
    auth_code = query_params["code"]
    
    # Đổi Auth Code lấy Access Token
    client = OAuth2Client(CLIENT_ID, CLIENT_SECRET, redirect_uri=REDIRECT_URI)
    try:
        token = client.fetch_token(TOKEN_ENDPOINT, code=auth_code, grant_type="authorization_code")
        # Dùng token để lấy thông tin cá nhân của User
        userinfo_response = client.get(USERINFO_ENDPOINT)
        st.session_state.user_info = userinfo_response.json()
        # Xóa tham số code trên URL cho sạch app
        st.query_params.clear()
    except Exception as e:
        st.error(f"Lỗi xác thực: {e}")

# --- GIAO DIỆN CHÍNH ---
st.markdown("<h1 style='text-align: center; color: var(--pink-900);'>🍊 Cánh Cửa Vào Trạm Xanh</h1>", unsafe_allow_html=True)

# Hiển thị trạng thái đăng nhập hoặc Form
_, center_col, _ = st.columns([1, 1.5, 1])

with center_col:
    # NẾU ĐÃ ĐĂNG NHẬP THÀNH CÔNG
    if st.session_state.user_info:
        user = st.session_state.user_info
        st.markdown(f"""
        <div style="text-align: center; background: white; border: 3px solid var(--pink-300); padding: 30px; border-radius: 20px; box-shadow: 6px 6px 0 var(--pink-100);">
            <img src="{user.get('picture')}" style="border-radius: 50%; width: 100px; border: 3px solid var(--pink-400);"><br><br>
            <h3>🌸 Chào mừng Trạm Trưởng <b>{user.get('name')}</b>!</h3>
            <p style="color: #795548;">Email: {user.get('email')}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🚪 Đăng xuất khỏi hệ thống", use_container_width=True, type="primary"):
            st.session_state.user_info = None
            st.rerun()
        st.switch_page("pages/ap.py")

    # NẾU CHƯA ĐĂNG NHẬP
    else:
        tab_login, tab_signup = st.tabs(["🌸 Đăng nhập", "🎀 Đăng ký mới"])
        
        with tab_login:
            st.markdown("<h3 style='text-align: center;'>💖 Mừng cậu quay lại!</h3>", unsafe_allow_html=True)
            user_login = st.text_input("Tên trạm trưởng:", placeholder="Nhập tên...", key="login_user")
            pwd_login = st.text_input("Mật mã bí mật:", type="password", placeholder="Nhập mật khẩu...", key="login_pwd")
            
            if st.button("🚀 Khởi động Trạm Xanh", use_container_width=True, type="primary"):
                if user_login and pwd_login:
                    st.success(f"🎉 Đăng nhập thành công với tài khoản {user_login}!")
                else: st.warning("⚠️ Điền thiếu thông tin cậu ơi!")
            
            # --- NÚT ĐĂNG NHẬP BẰNG GOOGLE CHẠY THẬT ---
            st.markdown('<div class="divider">HOẶC</div>', unsafe_allow_html=True)
            
            # Khởi tạo link đăng nhập Google
            client = OAuth2Client(CLIENT_ID, redirect_uri=REDIRECT_URI)
            uri, state = client.create_authorization_url(AUTHORIZATION_ENDPOINT, scope="openid email profile")
            
            # Sử dụng thẻ HTML <a> giả lập nút bấm để hướng người dùng sang trang login Google
            st.markdown(f"""
            <a href="{uri}" target="_self" style="text-decoration: none;">
                <div style="background-color: #ffffff; border: 2px solid var(--pink-300); color: #5D4037; 
                            padding: 10px; border-radius: 10px; text-align: center; font-weight: bold;
                            box-shadow: 3px 3px 0 var(--pink-100); cursor: pointer;">
                    🌐 Tiếp tục bằng tài khoản Google
                </div>
            </a>
            """, unsafe_allow_html=True)

        with tab_signup:
            st.markdown("<h3 style='text-align: center;'>✨ Gia nhập đội quân Xanh!</h3>", unsafe_allow_html=True)
            # (Phần form đăng ký thủ công giữ nguyên...)
            st.text_input("Chọn tên trạm trưởng:", key="reg_user")
            st.text_input("Tạo mật mã bí mật:", type="password", key="reg_pwd")
            if st.button("🎀 Tạo tài khoản", use_container_width=True):
                st.success("Tạo tài khoản thành công!")