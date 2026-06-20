import streamlit as st
import os
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Bản Đồ Giải Cứu", page_icon="📍", layout="wide")

# --- Hàm Load CSS Tổng ---
def load_local_css():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    css_path = os.path.join(root_dir, "style.css")
    if not os.path.exists(css_path):
        css_path = "style.css"
    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_local_css()

# --- CSS Ép màu ô chọn (Selectbox / Input) thành Trắng + Chữ Nâu ---
st.markdown("""
<style>
/* Can thiệp vào ô input, textarea và selectbox của Streamlit */
div[data-baseweb="select"] > div, 
input[type="text"], 
textarea {
    background-color: #ffffff !important;
    color: #5D4037 !important; /* Màu nâu đất */
    border-radius: 8px !important;
    border: 1px solid var(--pink-300) !important;
}

/* Đổi màu chữ bên trong khối selectbox */
div[data-baseweb="select"] span, 
div[data-baseweb="select"] div {
    color: #5D4037 !important;
}

/* Đổi màu nền và chữ của danh sách xổ xuống (Dropdown list) */
ul[role="listbox"] {
    background-color: #ffffff !important;
}
ul[role="listbox"] li {
    color: #5D4037 !important;
    background-color: #ffffff !important;
}
ul[role="listbox"] li:hover {
    background-color: #FFF3E0 !important; /* Nền cam nhạt khi di chuột vào */
}
</style>
""", unsafe_allow_html=True)

# --- Navbar Ngang ---
nav_col = st.columns(4)
with nav_col[0]:
    if st.button("🔍 Trạm Nhận Diện", use_container_width=True): st.switch_page("ap.py")
with nav_col[1]:
    if st.button("📚 Cẩm Nang Xanh", use_container_width=True): st.switch_page("pages/cam_nang.py")
with nav_col[2]:
    if st.button("🎮 Đố Vui Sống Xanh", use_container_width=True): st.switch_page("pages/do_vui.py")
with nav_col[3]: 
    st.button("📍 Bản Đồ Giải Cứu", use_container_width=True, type="primary")

# --- Tiêu đề & Browser Chrome Mockup ---
st.title("📍 Điểm Thu Gom Rác Đặc Thù")

st.markdown("""
<div class="browser-chrome">
    <div class="tabbar">
        <div class="tab-pill">📍 ban-do-giai-cuu.untitled</div>
        <div class="dots">🤍 ✕</div>
    </div>
    <div class="addressbar">
        <span>←&nbsp;→&nbsp;⟳&nbsp;⌂</span>
        <div class="url-pill">https://trolyxanh.local/ban-do-giai-cuu-ha-noi</div>
        <span>☆</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.write("Đừng vứt pin hay thiết bị điện tử ra thùng rác chung! Hãy mang đến các trạm thu gom an toàn tại khu vực Hà Nội dưới đây:")
st.markdown("---")

# --- Nội dung điểm thu gom gốc ---
st.markdown("### 🔋 Điểm thu hồi Pin cũ & Rác Điện Tử Mini")
st.info("""
* **UBND Phường Quán Thánh:** Số 12-14 Phan Đình Phùng, Ba Đình, Hà Nội.
* **Nhà Văn Hóa Phường Nghĩa Tân:** Đối diện trường THCS Nghĩa Tân, Cầu Giấy, Hà Nội.
* **UBND Phường Tràng Tiền:** Số 2 Cổ Tân, Hoàn Kiếm, Hà Nội.
* **Các điểm thu đổi của Hà Nội Xanh:** Thu gom định kỳ theo các chiến dịch làm sạch môi trường.
""")

st.markdown("### 💻 Điểm thu hồi Thiết Bị Điện Tử Lớn (Việt Nam Tái Chế)")
st.success("""
* **Chi cục Bảo vệ Môi trường Hà Nội:** Số 17 Trung Yên 3, Trung Hòa, Cầu Giấy, Hà Nội.
* Các trung tâm bảo hành lớn hoặc chương trình 'Đổi cũ lấy mới' tại các hệ thống siêu thị điện máy lớn trên địa bàn thành phố.
""")


# ── PHẦN FORM GÓP Ý & LƯU CSV ───────────────────────────────────────────────
st.markdown('<br>', unsafe_allow_html=True)
csv_file = "contributions.csv" # Tên file lưu trữ dữ liệu

with st.expander("✨ Bạn biết điểm thu gom nào khác? Bật mí cho chúng mình nhé!"):
    with st.form("suggest_location", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Tên địa điểm / Tên chiến dịch:")
        with col2:
            waste_type = st.selectbox("Nhận thu gom loại rác gì?", ["Pin cũ", "Rác điện tử", "Quần áo cũ", "Vỏ hộp sữa", "Khác"])
        
        addr = st.text_area("Địa chỉ chi tiết hoặc link fanpage:")
        
        submit = st.form_submit_button("Gửi đóng góp 💌", type="primary")
        
        # Xử lý khi nhấn nút gửi
        if submit:
            if name and addr:
                # Tạo một DataFrame chứa dữ liệu mới
                new_data = pd.DataFrame({
                    "Thời gian": [datetime.now().strftime("%d/%m/%Y %H:%M")],
                    "Tên địa điểm": [name],
                    "Loại rác": [waste_type],
                    "Địa chỉ": [addr]
                })
                
                # Lưu vào file CSV (Nếu có file rồi thì viết tiếp, chưa có thì tạo mới)
                if os.path.exists(csv_file):
                    new_data.to_csv(csv_file, mode='a', header=False, index=False, encoding='utf-8-sig')
                else:
                    new_data.to_csv(csv_file, mode='w', header=True, index=False, encoding='utf-8-sig')
                    
                st.success("🎉 Cảm ơn bạn! Thông tin đã được lưu lại để cộng đồng cùng xem.")
            else:
                st.warning("⚠️ Nhập thiếu thông tin rồi! Cậu điền tên và địa chỉ giúp mình nhé.")


# ── PHẦN HIỂN THỊ DỮ LIỆU ĐÓNG GÓP TỪ CSV ───────────────────────────────────
with st.expander("👀 Xem các địa điểm cộng đồng đã đóng góp"):
    if os.path.exists(csv_file):
        # Đọc dữ liệu từ file csv và hiển thị ra bảng
        df = pd.read_csv(csv_file)
        # Sử dụng st.dataframe để hiển thị bảng gọn gàng, tự động dàn trang
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        st.info("🌱 Hiện tại chưa có địa điểm nào được đóng góp. Bạn hãy là người đầu tiên nhé!")

# --- Footer chung ---
st.markdown('<div class="custom-footer">🍊by dnh_mng.1753<br><span style="font-size: 0.8em; opacity: 0.8;">Dự án bảo vệ môi trường</span></div>', unsafe_allow_html=True)