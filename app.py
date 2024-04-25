import streamlit as st
import pytube
from pytube import YouTube

st.set_page_config(page_title="Super Downloader", page_icon=":sparkles:", layout="wide")
st.title("Công cụ tải video trực tuyến")

st.header("Youtube Downloader")
link = st.text_input(placeholder="E.g: https://www.youtube.com/watch?v=Example", type="default", label="Nhập đường dẫn")
output_message = st.empty()

def download():
    if(link == ""):
        output_message.error("Đường dẫn đang bị trống, hãy nhập gì đó...")
        return

    try:
        YouTube(link).streams.first().download()
        output_message.success("Tải xuống thành công")
    except pytube.exceptions.RegexMatchError:
        output_message.error("URL không hợp lệ. Vui lòng kiểm tra và thử lại.")
    except pytube.exceptions.VideoUnavailable:
        output_message.error("Video không khả dụng. Có thể bị xoá hoặc cấm tải xuống.")
    except Exception as e:
        output_message.error(f"Có lỗi xảy ra: {e}")


if st.button("Tải xuống", type="primary"):
    download()
