import streamlit as st
import os

st.set_page_config(page_title="Đố Vui Sống Xanh", page_icon="🎮", layout="wide")

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

# --- CSS Ép màu trực tiếp vào nút bấm của Streamlit ---
st.markdown("""
<style>
.quiz-container div[data-testid="stButton"] > button {
    border-radius: 14px !important;
    padding: 14px 16px !important;
    font-size: 14px !important;
    font-weight: 700 !important;
    text-align: center !important;
    display: block !important;
}

div[data-quiz-type="organic"] div[data-testid="stButton"] > button { background: #FFF3E0 !important; border-color: #f5c070 !important; box-shadow: 4px 4px 0 #FFF9C4 !important; }
div[data-quiz-type="recycle"] div[data-testid="stButton"] > button { background: #E8F5E9 !important; border-color: #7ec87e !important; box-shadow: 4px 4px 0 #C8E6C9 !important; }
div[data-quiz-type="other"] div[data-testid="stButton"] > button { background: #FFFDE7 !important; border-color: #f0c840 !important; box-shadow: 4px 4px 0 #FFF9C4 !important; }
div[data-quiz-type="hazard"] div[data-testid="stButton"] > button { background: #FCE4EC !important; border-color: #f06090 !important; box-shadow: 4px 4px 0 #FFCDD2 !important; }
div[data-quiz-type="elec"] div[data-testid="stButton"] > button { background: #E8EAF6 !important; border-color: #7986cb !important; box-shadow: 4px 4px 0 #C5CAE9 !important; }

div[data-quiz-type] div[data-testid="stButton"] > button p {
    color: var(--pink-900) !important;
}

.quiz-question {
    font-size: 16px;
    font-weight: 700;
    color: var(--pink-900);
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# --- Navbar ---
nav_col = st.columns(4)
with nav_col[0]: 
    if st.button("🔍 Trạm Nhận Diện", use_container_width=True): st.switch_page("ap.py")
with nav_col[1]: 
    if st.button("📚 Cẩm Nang Xanh", use_container_width=True): st.switch_page("pages/cam_nang.py")
with nav_col[2]: 
    st.button("🎮 Đố Vui Sống Xanh", use_container_width=True, type="primary")
with nav_col[3]: 
    if st.button("📍 Bản Đồ Giải Cứu", use_container_width=True): st.switch_page("pages/ban_do.py")

# --- Tiêu đề & Browser Chrome Mockup ---
st.title("🎮 Thử Thách Đố Vui")

st.markdown("""
<div class="browser-chrome">
    <div class="tabbar">
        <div class="tab-pill">🎮 do-vui-song-xanh.untitled</div>
        <div class="dots">🤍 ✕</div>
    </div>
    <div class="addressbar">
        <span>←&nbsp;→&nbsp;⟳&nbsp;⌂</span>
        <div class="url-pill">https://trolyxanh.local/do-vui</div>
        <span>☆</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.info("""
✨ **Chào mừng bạn đến với thử thách Phân Loại Rác!** Hãy vận dụng những kiến thức bổ ích từ Cẩm Nang Xanh để giải quyết các tình huống thực tế dưới đây. Mỗi lựa chọn đúng của bạn đều góp phần làm cho Trái Đất của chúng ta sạch đẹp hơn từng ngày! 🌱
""")

st.markdown("---")

# --- DANH SÁCH 7 CÂU HỎI ---
questions = [
    {
        "id": "q1",
        "label": "🗂️ Tình huống 1: Phân loại rác bánh mì",
        "q": "Vụn bánh mì cháy và cặn bột ca cao thuộc nhóm nào?",
        "options": [
            ("A. Rác Tái Chế", "recycle"),
            ("B. Rác Hữu Cơ", "organic"),
            ("C. Rác Còn Lại", "other"),
            ("D. Rác Nguy Hại", "hazard")
        ],
        "correct": 1
    },
    {
        "id": "q2",
        "label": "⚡ Tình huống 2: Linh kiện điện tử",
        "q": "Dây cáp và bảng mạch cũ nên bỏ vào đâu?",
        "options": [
            ("A. Rác Còn Lại", "other"),
            ("B. Rác Hữu Cơ", "organic"),
            ("C. Rác Tái Chế", "recycle"),
            ("D. Rác Điện Tử", "elec")
        ],
        "correct": 3
    },
    {
        "id": "q3",
        "label": "🥤 Tình huống 3: Ly trà sữa và vỏ hộp nhựa",
        "q": "Một chiếc ly nhựa đựng trà sữa sau khi uống xong cần xử lý và phân loại như thế nào?",
        "options": [
            ("A. Vứt ngay vào thùng Rác Còn Lại", "other"),
            ("B. Rửa sạch, phơi khô rồi bỏ vào Rác Tái Chế", "recycle"),
            ("C. Gom chung với thức ăn thừa ở Rác Hữu Cơ", "organic"),
            ("D. Đốt bỏ tại nhà cho sạch", "hazard")
        ],
        "correct": 1
    },
    {
        "id": "q4",
        "label": "🚨 Tình huống 4: Dọn dẹp tủ thuốc gia đình",
        "q": "Thuốc tây đã hết hạn sử dụng và vỏ vỉ thuốc làm bằng nhôm/nhựa nên phân loại vào nhóm nào?",
        "options": [
            ("A. Rác Tái Chế vì có nhôm", "recycle"),
            ("B. Rác Còn Lại cho xe gom đi chôn lấp", "other"),
            ("C. Rác Nguy Hại (cần gom riêng xử lý đặc biệt)", "hazard"),
            ("D. Rác Hữu Cơ để phân hủy tự nhiên", "organic")
        ],
        "correct": 2
    },
    {
        "id": "q5",
        "label": "📦 Tình huống 5: Hộp xốp đựng cơm văn phòng",
        "q": "Hộp xốp đựng thức ăn bám nhiều dầu mỡ (không thể rửa sạch hoàn toàn) thuộc loại rác nào?",
        "options": [
            ("A. Rác Còn Lại", "other"),
            ("B. Rác Tái Chế", "recycle"),
            ("C. Rác Hữu Cơ", "organic"),
            ("D. Rác Điện Tử", "elec")
        ],
        "correct": 0
    },
    {
        "id": "q6",
        "label": "🌿 Tình huống 6: Chăm sóc cây cảnh tại nhà",
        "q": "Lá cây rụng, cành cây nhỏ tỉa từ ban công và vỏ trứng gà đập ra nên xử lý ra sao?",
        "options": [
            ("A. Gom vào thùng Rác Tái Chế", "recycle"),
            ("B. Cho vào Rác Hữu Cơ (hoặc ủ làm phân bón)", "organic"),
            ("C. Bỏ vào thùng Rác Còn Lại", "other"),
            ("D. Gom cùng đồ điện tử hỏng", "elec")
        ],
        "correct": 1
    },
    {
        "id": "q7",
        "label": "🔋 Tình huống 7: Thay pin điều khiển Tivi",
        "q": "Những viên pin tiểu (pin AA/AAA) đã qua sử dụng tuyệt đối không được làm gì?",
        "options": [
            ("A. Tuyệt đối không vứt chung rác sinh hoạt hoặc đốt", "hazard"),
            ("B. Không mang đi bán phế liệu", "recycle"),
            ("C. Không rửa bằng nước sạch", "other"),
            ("D. Không cất trong tủ kính", "elec")
        ],
        "correct": 0
    }
]

# --- RENDER CÂU HỎI ---
st.markdown('<div class="quiz-container">', unsafe_allow_html=True)

for item in questions:
    st.markdown(f'<div class="section-label">{item["label"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="quiz-question">{item["q"]}</div>', unsafe_allow_html=True)
    
    if item["id"] not in st.session_state: 
        st.session_state[item["id"]] = None
    
    cols = st.columns(2)
    for i, (text, quiz_type) in enumerate(item["options"]):
        with cols[i % 2]:
            st.markdown(f'<div class="quiz-item" data-quiz-type="{quiz_type}">', unsafe_allow_html=True)
            if st.button(text, key=f"{item['id']}_{i}", use_container_width=True):
                st.session_state[item["id"]] = i
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Hiển thị Feedback nhanh cho từng câu
    if st.session_state[item["id"]] is not None:
        if st.session_state[item["id"]] == item["correct"]:
            st.success("🎉 **Chính xác!**")
        else:
            st.error("❌ **Chưa đúng rồi!**")
    
    st.markdown("---")

st.markdown('</div>', unsafe_allow_html=True)


# ── PHẦN NÚT BẤM XEM KẾT QUẢ TỔNG KẾT ──────────────────────────────────────────
st.markdown('<div class="section-label" style="text-align: center;">🏁 Hoàn thành bài trắc nghiệm</div>', unsafe_allow_html=True)

# Tạo một cột căn giữa cho nút Xem Kết Quả
_, center_col, _ = st.columns([1, 2, 1])

with center_col:
    if st.button("📊 Xem Kết Quả Tổng Kết", use_container_width=True, type="primary"):
        total_correct = 0
        unanswered = 0
        
        # Vòng lặp tính toán điểm từ session state
        for item in questions:
            user_choice = st.session_state.get(item["id"])
            if user_choice is None:
                unanswered += 1
            elif user_choice == item["correct"]:
                total_correct += 1
                
        # --- BẮT ĐẦU PHÂN LOẠI ĐÁNH GIÁ ---
        st.markdown("<br>", unsafe_allow_html=True)
        
        if unanswered > 0:
            st.warning(f"⚠️ Bạn chưa hoàn thành hết tất cả các câu hỏi! (Còn {unanswered}/{len(questions)} câu chưa trả lời). Hãy chọn đáp án cho tất cả các câu trước nhé!")
        else:
            # Tỷ lệ số câu đúng (Ví dụ: Bạn có 7 câu, nếu đúng >= 5 câu (~70% trở lên) thì tính là Xuất Sắc)
            # Ở đây mình tính theo mốc tỉ lệ: Từ 5/7 câu trở lên là Xuất Sắc, dưới 5 câu là Cần Cố Gắng.
            if total_correct >= 5:
                st.balloons() # Thả bóng bay chúc mừng
                st.success(f"""
                🏆 **XUẤT SẮC!! Bạn đích thực là một chiến binh bảo vệ môi trường!** 🎯 **Kết quả:** Bạn trả lời đúng **{total_correct}/{len(questions)}** câu.  
                🌱 Bạn đã nắm vững kiến thức và có thể tự tin phân loại rác một cách chính xác tại ngôi nhà của mình! Hãy tiếp tục lan tỏa tinh thần sống xanh này nhé!
                """)
            else:
                st.info(f"""
                💪 **CẦN CỐ GẮNG THÊM MỘT CHÚT NỮA THÔI!** 🎯 **Kết quả:** Bạn trả lời đúng **{total_correct}/{len(questions)}** câu.  
                📚 Đừng buồn nhé, phân loại rác cần một chút thời gian để ghi nhớ mà. Bạn có thể mở lại tab **Cẩm Nang Xanh** để "ôn tập" lại các mẹo vặt và thử sức lại bất cứ lúc nào nha! Bạn làm được mà!
                """)

# --- Footer chung ---
st.markdown('<div class="custom-footer">🍊by dnh_mng.1753<br><span style="font-size: 0.85em; opacity: 0.8;">Dự án bảo vệ môi trường</span></div>', unsafe_allow_html=True)