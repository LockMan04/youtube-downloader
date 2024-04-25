#  Cách tạo docker file

> ⚠️ Chú ý: Hãy chắc chắc rằng máy tính của bạn đã cài và đang chạy Docker.
> Nếu chưa hãy tải xuống [tại trang chủ của Docker](https://www.docker.com/)


**Giới hiệu sơ lượt về `youtube-downloader`**

- Là một ứng dụng web python đơn giản và cơ bản sử dụng thư viện [Pytube](https://pytube.io/en/latest/index.html) để tải video từ _**Youtube**_
- Ảnh chụp màn hình: 

![](https://raw.githubusercontent.com/LockMan04/Stored/main/youtube-downloader/Screenshot1.png)

![](https://raw.githubusercontent.com/LockMan04/Stored/main/youtube-downloader/Screenshot2.png)

![](https://raw.githubusercontent.com/LockMan04/Stored/main/youtube-downloader/Screenshot3.png)

## Tải xuống mã nguồn

Trước tiên để có thể chạy được chương trình hãy clone [kho lưu trữ này](https://github.com/LockMan04/youtube-downloader) về máy của bạn

```bash
    git clone https://github.com/LockMan04/youtube-downloader.git
```

```bash
    cd youtube-downloader
```

## Tạo Dockerfile

Dockerfile chỉ đơn giản là một tệp dựa trên văn bản không có phần mở rộng (Extention) chứa những tập lệnh hướng dẫn. Docker sẽ sử dụng tệp này sẽ build một container image

Tạo một file có tên là `Dockerfile` và chắc chắc rằng nó không có phần mở rộng. Mở nó lên và thêm đoạn code này vào

```dockerfile
    FROM python:3.12
    WORKDIR /app
    COPY . .
    RUN pip install -r requirements.txt
    EXPOSE 8501
    CMD ["streamlit", "run", "app.py"]
```

Trong đó
> - `FROM python:3.12`: Sử dụng python:3.12 làm base image
> - `WORKDIR /app`: Thiết lập thư mục làm trong container
> - `COPY . .`: Copy tất cả file từ thư mục hiện tại vào trong container
> - `RUN pip install -r requirements.txt`: Cài đặt các thư viện cần thiết
> - `EXPOSE 8501`: Mở localhost với cổng là 8501
> - `CMD ["streamlit", "run", "app.py"]`: Dùng để chạy ứng dụng web khi container được khởi động

Để build một image, ta dùng lệnh: 

```base
    docker build -t youtube-downloader .
```

> ⚠️: đừng quên dấu chấm ở cuối

## Build một image

Lệnh `docker build` sẽ sử dụng Dockerfile để build một image mới

Cờ `-t`: tag. Có thể hiểu đây là tên của image và có thể tham chiếu đến nó khi chạy một container

Dấu `.` sẽ cho docker biết Dockerfile hiện tại đang ở đâu. Trong ví dụ này nó ở trong thư mục hiện tại

## Khởi chạy container

Để chạy một container ta sẽ sử dụng lệnh `docker build`

```base
    docker run -dp 127.0.0.1:8501:8501 youtube-downloader
```

Đi đến trình duyệt và xem thành quả [localhost:8501](http://localhost:8501/)

> - Cờ `d` hay `--detach`: cho phép container của bạn chạy ở chế độ nền. Bạn có thể kiểm tra container của bạn bằng lệnh `docker ps`
> - Cờ `p` hay `--publish`: tạo ánh xạ giữa localhost và container. Nếu không có sự ánh xạ này bạn không thể nào truy cập được ứng dụng từ máy của bạn

## Hướng dẫn nhanh

Dockerfile này đã được upload lên [hub.docker.com](https://hub.docker.com/). Bạn có thể pull về bằng: 

```bash
    docker pull lockman04/youtube-downloader
```

## Thanks



