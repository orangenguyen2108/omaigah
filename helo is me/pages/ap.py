import streamlit as st
import tensorflow as tf
import numpy as np
import pandas as pd
import os
from PIL import Image
from datetime import datetime

st.set_page_config(page_title="Trợ Lý Số Xanh", page_icon="🌸", layout="wide")

def load_local_css():
    with open("style.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
load_local_css()

# Thanh điều hướng nằm ngang trên đỉnh đầu bằng nút bấm
nav_col = st.columns(4)
with nav_col[0]: st.button("🔍 Trạm Nhận Diện", use_container_width=True, type="primary")
with nav_col[1]:
    if st.button("📚 Cẩm Nang Xanh", use_container_width=True): st.switch_page("pages/cam_nang.py")
with nav_col[2]:
    if st.button("🎮 Đố Vui Sống Xanh", use_container_width=True): st.switch_page("pages/do_vui.py")
with nav_col[3]:
    if st.button("📍 Bản Đồ Giải Cứu", use_container_width=True): st.switch_page("pages/ban_do.py")

LABELS = ['Battery', 'Keyboard', 'Microwave', 'Mobile', 'Mouse', 'PCB', 'Player', 'Printer', 'Television', 'Washing Machine', 'cardboard', 'glass', 'metal', 'organic', 'paper', 'plastic', 'trash']

TRASH_DETAILS = {
    'Battery': {'vi': 'Pin / Ắc quy', 'type': 'Rác nguy hại 🚨', 'tip': 'TUYỆT ĐỐI KHÔNG vứt vào thùng rác chung hoặc đốt. Pin chứa kim loại nặng gây ô nhiễm nguồn nước. Hãy gom lại vào hộp khô và mang đến các điểm thu hồi pin cũ gần nhất.'},
    'Keyboard': {'vi': 'Bàn phím máy tính', 'type': 'Rác điện tử 🔌', 'tip': 'Đừng vứt ra bãi rác sinh hoạt. Nhựa và bảng mạch bên trong có thể tái chế. Hãy liên hệ các đơn vị thu mua đồ điện tử cũ.'},
    'Microwave': {'vi': 'Lò vi sóng', 'type': 'Rác điện tử cỡ vừa 🔌', 'tip': 'Thiết bị điện tử chứa linh kiện có thể tái sử dụng. Nên đem đến các cửa hàng sửa chữa điện tử cũ hoặc trung tâm tái chế.'},
    'Mobile': {'vi': 'Điện thoại di động', 'type': 'Rác điện tử 🔌', 'tip': 'Chứa nhiều kim loại quý và pin Lithium nguy hiểm. Hãy chuyển giao cho các trung tâm bảo hành hoặc điểm thu gom rác công nghệ.'},
    'Mouse': {'vi': 'Chuột máy tính', 'type': 'Rác điện tử 🔌', 'tip': 'Thuộc nhóm rác thải công nghệ mini. Gom cụm lại cùng với dây cáp, bàn phím cũ để xử lý đúng quy trình.'},
    'PCB': {'vi': 'Bảng mạch điện tử', 'type': 'Rác điện tử nguy hại 🔬', 'tip': 'Bao gồm các linh kiện bán dẫn, mối hàn chì. Cần được xử lý bởi các công ty môi trường chuyên nghiệp để bóc tách kim loại độc hại.'},
    'Player': {'vi': 'Máy nghe nhạc / Đầu đĩa', 'type': 'Rác điện tử 🔌', 'tip': 'Tháo phần pin ra xử lý riêng. Phần vỏ nhựa và linh kiện cơ học có thể đem đến nơi thu gom đồ điện tử.'},
    'Printer': {'vi': 'Máy in', 'type': 'Rác điện tử 🔌', 'tip': 'Chú ý hộp mực bên trong máy in cũ thường chứa bột mực độc hại. Cần tháo hộp mực ra riêng trước khi đem máy đi thanh lý.'},
    'Television': {'vi': 'Tivi / Màn hình', 'type': 'Rác điện tử cỡ lớn 📺', 'tip': 'Màn hình thủy tinh cũ chứa lưu huỳnh và thủy ngân. Tuyệt đối không đập vỡ, hãy gọi thợ thu mua đồ cũ hoặc đơn vị tái chế.'},
    'Washing Machine': {'vi': 'Máy giặt', 'type': 'Rác điện tử khổng lồ 🧺', 'tip': 'Kim loại từ vỏ máy giặt có giá trị tái chế rất cao. Hãy liên hệ các bên thu mua phế liệu lớn.'},
    'cardboard': {'vi': 'Bìa các-tông', 'type': 'Rác tái chế được 📦', 'tip': '💡 **Ý tưởng DIY:** Bạn có thể cắt ra làm hộp đựng bút, khay tài liệu, hoặc làm nhà đồ chơi bằng giấy cho thú cưng. Ép phẳng và giữ khô ráo để bán phế liệu.'},
    'glass': {'vi': 'Thủy tinh / Chai lọ', 'type': 'Rác tái chế được 🍾', 'tip': '💡 **Ý tưởng DIY:** Rửa sạch để làm lọ cắm hoa, hũ muối dưa, hoặc luồn đèn LED vào làm đèn ngủ cực chill. Tránh để vỡ gây nguy hiểm.'},
    'metal': {'vi': 'Kim loại / Lon nước', 'type': 'Rác tái chế được 🥫', 'tip': 'Rửa sạch bên trong lon nước ngọt, giẫm bẹp để tiết kiệm diện tích. Đây là nguồn nguyên liệu tái chế 100% giúp tiết kiệm năng lượng.'},
    'organic': {'vi': 'Rác hữu cơ / Đồ ăn thừa', 'type': 'Rác phân hủy sinh học 🍎', 'tip': '💡 **Ý tưởng sống xanh:** Bạn có thể ủ đống rác này với một chút đất để làm phân bón hữu cơ siêu dinh dưỡng cho cây cảnh tại nhà.'},
    'paper': {'vi': 'Giấy vụn / Sách vở', 'type': 'Rác tái chế được 📄', 'tip': '💡 **Ý tưởng DIY:** Gom lại đóng thành sổ tay nháp, hoặc dùng làm giấy lót khi vẽ, làm đồ thủ công. Luôn giữ giấy khô ráo.'},
    'plastic': {'vi': 'Nhựa / Chai nhựa', 'type': 'Rác tái chế được 🥤', 'tip': '💡 **Ý tưởng DIY:** Cắt đôi chai nước để làm chậu trồng cây mầm. Nếu vứt đi, hãy bóc nhãn mác giấy ra trước để tăng tỷ lệ tái chế thành công.'},
    'trash': {'vi': 'Rác sinh hoạt khác', 'type': 'Rác không thể tái chế 🗑️', 'tip': 'Đây là những loại rác khó tái chế (như màng bọc thực phẩm bẩn, băng gạc...). Hãy bọc kín và vứt vào thùng rác tổng để xe chở đi chôn lấp.'}
}

HISTORY_FILE = "waste_history.csv"

def save_to_history(label_en):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_data = pd.DataFrame([[now, label_en]], columns=["Thời gian", "Loại rác"])
    if not os.path.exists(HISTORY_FILE):
        new_data.to_csv(HISTORY_FILE, index=False)
    else:
        new_data.to_csv(HISTORY_FILE, mode='a', header=False, index=False)

def get_history_data():
    if os.path.exists(HISTORY_FILE): return pd.read_csv(HISTORY_FILE)
    return pd.DataFrame(columns=["Thời gian", "Loại rác"])

@st.cache_resource
def load_model():
    try: return tf.keras.models.load_model('./waste_mobile_model.keras')
    except Exception as e:
        st.error(f"Lỗi tải model: Không tìm thấy file 'waste_mobile_model.keras' trong cùng thư mục! Lỗi: {e}")
        return None

model = load_model()

st.title("♻️ Nhận diện & phân loại rác tự động")
st.markdown('<div class="browser-chrome"><div class="tabbar"><div class="tab-pill">♻️ rac-app.untitled</div><div class="dots">🤍 ✕</div></div><div class="addressbar"><span>←&nbsp;→&nbsp;⟳&nbsp;⌂</span><div class="url-pill">https://trolyxanh.local/phan-loai-rac</div><span>☆</span></div><div class="preview">☁️&nbsp;&nbsp;🌤️&nbsp;&nbsp;☁️&nbsp;&nbsp;✨</div></div>', unsafe_allow_html=True)
st.markdown("---")

tab1, tab2 = st.tabs(["🔍 nhận diện & tư vấn", "📊 nhật ký sống xanh"])

with tab1:
    st.write("Tải ảnh lên để AI phân tích và đưa ra giải pháp xử lý môi trường phù hợp.")
    uploaded_file = st.file_uploader("Chọn một bức ảnh rác thải...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        col1, col2 = st.columns([1, 1.2])
        with col1:
            st.image(image, caption='Ảnh đã tải lên', use_container_width=True)
        with col2:
            st.subheader("🤖 Kết quả phân tích từ AI:")
            if st.button("Bắt đầu nhận diện", type="primary"):
                with st.spinner('AI đang quét các đặc trưng hình khối...'):
                    img = image.resize((224, 224))
                    img_array = np.array(img)
                    if img_array.shape[-1] == 4: img_array = img_array[..., :3]
                    img_array = img_array / 255.0
                    img_array = np.expand_dims(img_array, axis=0)
                    
                    if model is not None:
                        predictions = model.predict(img_array)
                        result_idx = np.argmax(predictions)
                        confidence = np.max(predictions)
                        pred_en = LABELS[result_idx]
                        info = TRASH_DETAILS.get(pred_en, {'vi': pred_en, 'type': 'Không xác định', 'tip': 'Không có dữ liệu.'})
                        
                        save_to_history(pred_en)
                        st.metric(label="Vật liệu phát hiện", value=f"{pred_en} ({info['vi']})")
                        st.info(f"**Phân loại:** {info['type']}")
                        st.write(f"**Độ chính xác dự đoán:** {confidence * 100:.2f}%")
                        st.progress(float(confidence))
                        st.markdown("### 💡 Hướng dẫn xử lý & Tái chế xanh:")
                        st.warning(info['tip'])

with tab2:
    st.subheader("📊 Thống kê lượng rác bạn đã phân loại")
    df_history = get_history_data()
    if df_history.empty:
        st.info("Nhật ký trống. Hãy tích cực phân loại rác ở Tab bên cạnh để xây dựng biểu đồ sống xanh nhé!")
    else:
        trash_counts = df_history["Loại rác"].value_counts().reset_index()
        trash_counts.columns = ["Loại rác", "Số lượng (Lần)"]
        trash_counts["Tên tiếng Việt"] = trash_counts["Loại rác"].apply(lambda x: TRASH_DETAILS.get(x, {'vi': x})['vi'])
        st.markdown(f"🎉 Tuyệt vời! Bạn đã thực hiện tổng cộng **{len(df_history)}** lần phân loại rác bảo vệ môi trường.")
        st.bar_chart(data=trash_counts, x="Tên tiếng Việt", y="Số lượng (Lần)", color="#F3B768")
        with st.expander("Xem chi tiết nhật ký mốc thời gian"):
            st.dataframe(df_history.sort_values(by="Thời gian", ascending=False), use_container_width=True)
            if st.button("Xóa toàn bộ lịch sử"):
                if os.path.exists(HISTORY_FILE):
                    os.remove(HISTORY_FILE)
                    st.rerun()

st.markdown('<div class="custom-footer">🍊by dnh_mng.1753<br><span style="font-size: 0.8em; opacity: 0.8;">Dự án bảo vệ môi trường</span></div>', unsafe_allow_html=True)