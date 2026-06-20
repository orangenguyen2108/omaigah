import streamlit as st
import os

st.set_page_config(page_title="Cẩm Nang Xanh", page_icon="📚", layout="wide")

def load_local_css():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    css_path = os.path.join(root_dir, "style.css")
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
load_local_css()

# ── CSS bổ sung riêng cho trang này ──────────────────────────────────────────
st.markdown("""
<style>
.cam-nang-card {
    background: #ffffff;
    border: 2.5px solid #e8a0aa;
    border-radius: 14px;
    padding: 18px 16px;
    box-shadow: 4px 4px 0 #f9c8d0;
    height: 100%;
    margin-bottom: 4px;
}
.cam-nang-card .badge {
    display: inline-block;
    font-size: 11px;
    font-weight: 800;
    padding: 3px 10px;
    border-radius: 999px;
    border: 1.5px solid #e8a0aa;
    margin-bottom: 8px;
    font-family: 'Nunito', sans-serif;
}
.cam-nang-card .card-title {
    font-family: 'Quicksand', sans-serif;
    font-size: 17px;
    font-weight: 800;
    margin-bottom: 8px;
    color: #7a2a3a;
}
.cam-nang-card .card-body {
    font-size: 13px;
    line-height: 1.7;
    color: #8b3a4a;
    margin-bottom: 10px;
}
.cam-nang-card .card-tip {
    font-size: 12px;
    font-weight: 600;
    line-height: 1.65;
    padding: 8px 12px;
    border-radius: 10px;
    border: 1.5px dashed #e8a0aa;
    color: #8b3a4a;
}

/* màu nền từng loại card */
.card-organic { background: #FFF3E0 !important; border-color: #f5c070 !important; }
.card-organic .badge { background: #FFD59A; color: #c05010; }
.card-organic .card-tip { background: #FFE0B2; border-color: #f5c070; }

.card-recycle { background: #E8F5E9 !important; border-color: #7ec87e !important; }
.card-recycle .badge { background: #A5D6A7; color: #2e7d32; }
.card-recycle .card-tip { background: #C8E6C9; border-color: #7ec87e; }

.card-other { background: #FFFDE7 !important; border-color: #f0c840 !important; }
.card-other .badge { background: #FFE082; color: #7a6000; }
.card-other .card-tip { background: #FFF9C4; border-color: #f0c840; }

.card-hazard { background: #FCE4EC !important; border-color: #f06090 !important; }
.card-hazard .badge { background: #EF9A9A; color: #7f0000; }
.card-hazard .card-tip { background: #FFCDD2; border-color: #f06090; }

.card-elec { background: #E8EAF6 !important; border-color: #7986cb !important; }
.card-elec .badge { background: #9FA8DA; color: #1a237e; }
.card-elec .card-tip { background: #C5CAE9; border-color: #7986cb; }

/* step cards */
.step-card {
    background: #ffffff;
    border: 2.5px solid #e8a0aa;
    border-radius: 14px;
    padding: 16px 12px;
    text-align: center;
    box-shadow: 3px 3px 0 #f9c8d0;
}
.step-num {
    width: 30px; height: 30px;
    background: #f5b8c4;
    border: 2px solid #e8a0aa;
    border-radius: 50%;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-family: 'Nunito', sans-serif;
    font-size: 13px;
    font-weight: 900;
    color: #7a2a3a;
    margin-bottom: 8px;
}
.step-icon { font-size: 26px; margin-bottom: 6px; }
.step-text {
    font-size: 12px;
    font-weight: 700;
    color: #8b3a4a;
    line-height: 1.5;
}

/* section label */
.section-label {
    font-family: 'Nunito', sans-serif;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #c97080;
    margin: 20px 0 12px 0;
}

.info-banner {
    background: #fde8ec;
    border: 2px solid #e8a0aa;
    border-radius: 14px;
    padding: 14px 18px;
    font-size: 13px;
    line-height: 1.7;
    color: #8b3a4a;
    box-shadow: 3px 3px 0 #f9c8d0;
    margin-bottom: 8px;
}

.custom-footer {
    text-align: center;
    padding: 20px;
    color: #c97080;
    font-size: 13px;
    margin-top: 30px;
    border-top: 2px dashed #e8a0aa;
}
</style>
""", unsafe_allow_html=True)

# ── Navbar ───────────────────────────────────────────────────────────────────
nav_col = st.columns(4)
with nav_col[0]:
    if st.button("🔍 Trạm Nhận Diện", use_container_width=True): st.switch_page("ap.py")
with nav_col[1]:
    st.button("📚 Cẩm Nang Xanh", use_container_width=True, type="primary")
with nav_col[2]:
    if st.button("🎮 Đố Vui Sống Xanh", use_container_width=True): st.switch_page("pages/do_vui.py")
with nav_col[3]:
    if st.button("📍 Bản Đồ Giải Cứu", use_container_width=True): st.switch_page("pages/ban_do.py")

# ── Tiêu đề ──────────────────────────────────────────────────────────────────
st.title("📚 Cẩm Nang Phân Loại Rác")
st.markdown('<div class="browser-chrome"><div class="tabbar"><div class="tab-pill">📚 cam-nang-xanh.untitled</div><div class="dots">🤍 ✕</div></div><div class="addressbar"><span>←&nbsp;→&nbsp;⟳&nbsp;⌂</span><div class="url-pill">https:trolyxanh.local/cam-nang-phan-loai-rac</div><span>☆</span></div><div class="preview">🌱&nbsp;&nbsp;♻️&nbsp;&nbsp;🍃&nbsp;&nbsp;✨</div></div>', unsafe_allow_html=True)
st.write("Cùng tìm hiểu cách phân loại các nhóm rác trong gia đình để bảo vệ môi trường nhé!")

st.markdown("""
<div class="info-banner">
    💡 <b>Tại sao cần phân loại rác?</b><br>
    Phân loại rác tại nguồn giúp tăng tỷ lệ tái chế lên đến <b>80%</b>, giảm lượng rác chôn lấp,
    tiết kiệm tài nguyên thiên nhiên và giảm phát thải khí nhà kính.
    Mỗi hành động nhỏ của bạn tạo ra sự khác biệt lớn! 🌱
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ── PHẦN 1: 3 nhóm rác cơ bản ───────────────────────────────────────────────
st.markdown('<div class="section-label">🗂️ 3 nhóm rác cơ bản tại nhà</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="cam-nang-card card-organic">
        <div class="step-icon">🍎</div>
        <span class="badge">Phân hủy sinh học</span>
        <div class="card-title">Rác Hữu Cơ</div>
        <div class="card-body">
            <b>Bao gồm:</b> Thức ăn thừa, rau củ quả thối, bã trà, bã cà phê, vỏ trứng, lá cây...
        </div>
        <div class="card-tip">
            💡 Ủ thành phân bón hữu cơ siêu dinh dưỡng cho cây cảnh tại nhà, hoặc gom riêng cho xe thu gom chuyên dụng.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="cam-nang-card card-recycle">
        <div class="step-icon">📦</div>
        <span class="badge">Tái chế được</span>
        <div class="card-title">Rác Tái Chế</div>
        <div class="card-body">
            <b>Bao gồm:</b> Giấy báo, bìa các-tông, vỏ chai nhựa, lon nước ngọt, chai lọ thủy tinh, sắt vụn...
        </div>
        <div class="card-tip">
            💡 Rửa sạch, phơi khô, bóp bẹp để tiết kiệm diện tích và đem bán phế liệu hoặc điểm thu gom.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="cam-nang-card card-other">
        <div class="step-icon">🗑️</div>
        <span class="badge">Không tái chế</span>
        <div class="card-title">Rác Còn Lại</div>
        <div class="card-body">
            <b>Bao gồm:</b> Túi nilon bẩn, hộp xốp, tã bỉm, giấy ăn đã qua sử dụng, vỏ gói bim bim...
        </div>
        <div class="card-tip">
            💡 Bọc kín lại và vứt vào thùng rác sinh hoạt chung để xe rác đưa đi chôn lấp/đốt đúng quy trình.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ── PHẦN 2: Rác nguy hại & điện tử ──────────────────────────────────────────
st.markdown('<div class="section-label">⚠️ Nhóm rác đặc biệt — Xử lý riêng</div>', unsafe_allow_html=True)

col4, col5 = st.columns(2)

with col4:
    st.markdown("""
    <div class="cam-nang-card card-hazard">
        <div class="step-icon">🚨</div>
        <span class="badge">Nguy hại — Không vứt chung!</span>
        <div class="card-title">Rác Nguy Hại</div>
        <div class="card-body">
            <b>Bao gồm:</b> Pin, ắc quy, bóng đèn huỳnh quang, hóa chất tẩy rửa, thuốc tây hết hạn, nhiệt kế thủy ngân...
        </div>
        <div class="card-tip">
            🚫 TUYỆT ĐỐI không vứt vào thùng rác chung hoặc đốt. Gom lại trong hộp khô và mang đến các điểm thu hồi pin/hóa chất chuyên dụng gần nhất.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class="cam-nang-card card-elec">
        <div class="step-icon">🔌</div>
        <span class="badge">Rác điện tử — E-waste</span>
        <div class="card-title">Rác Điện Tử</div>
        <div class="card-body">
            <b>Bao gồm:</b> Điện thoại cũ, máy tính, bảng mạch PCB, dây cáp, tivi, máy giặt, tủ lạnh...
        </div>
        <div class="card-tip">
            ♻️ Liên hệ các trung tâm bảo hành, cửa hàng thu mua đồ điện tử cũ, hoặc đơn vị tái chế chuyên nghiệp để bóc tách kim loại quý.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ── PHẦN 3: 4 bước phân loại ─────────────────────────────────────────────────
st.markdown('<div class="section-label">✅ 4 bước phân loại rác đúng chuẩn</div>', unsafe_allow_html=True)

s1, s2, s3, s4 = st.columns(4)

steps = [
    ("1", "🧹", "Làm sạch sơ bộ trước khi phân loại"),
    ("2", "🗂️", "Phân loại vào đúng 3 thùng riêng biệt"),
    ("3", "📦", "Bọc kín, ép bẹp để tiết kiệm diện tích"),
    ("4", "🚛", "Đặt đúng lịch và điểm thu gom quy định"),
]

for col, (num, icon, text) in zip([s1, s2, s3, s4], steps):
    with col:
        st.markdown(f"""
        <div class="step-card">
            <div class="step-num">{num}</div><br>
            <div class="step-icon">{icon}</div>
            <div class="step-text">{text}</div>
        </div>
        """, unsafe_allow_html=True)

  
# --- Hàm bọc Card (nếu bạn chưa có ở trên) ---
def card_box(content_func, css_class="cam-nang-card"):
    st.markdown(f'<div class="{css_class}" style="padding: 10px;">', unsafe_allow_html=True)
    content_func()
    st.markdown('</div>', unsafe_allow_html=True)

# --- Phần hiển thị 4 video ---
st.markdown('<div class="section-label">🎬 Thư viện Video Shorts</div>', unsafe_allow_html=True)

# Tạo 4 cột
cols = st.columns(4)

# Danh sách link video gốc của bạn
video_links = [
    "https://www.youtube.com/shorts/xxtmx3p8NzM",
    "https://www.youtube.com/shorts/GESaQrj_tsc",
    "https://www.youtube.com/shorts/hEKEWZ7bIyI",
    "https://www.youtube.com/shorts/74MQZm2m6ck"
]

# Đẩy video vào từng cột
for i, col in enumerate(cols):
    with col:
        # Chuyển đổi link từ /shorts/ sang /watch?v= để Streamlit nhận diện đầy đủ thumbnail
        clean_url = video_links[i].replace("youtube.com/shorts/", "youtube.com/watch?v=")
        
        # Hàm nội dung cho từng video
        def vid_content(url=clean_url):
            st.video(url)
            st.markdown(f"<p style='font-size:12px; margin-top:5px; text-align:center;'>Video {i+1}</p>", unsafe_allow_html=True)
        
        # Gọi hàm card_box để bọc video
        card_box(vid_content, css_class="cam-nang-card")

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown('<div class="custom-footer">🍊by dnh_mng.1753<br><span style="font-size: 0.8em; opacity: 0.8;">Dự án bảo vệ môi trường</span></div>', unsafe_allow_html=True)