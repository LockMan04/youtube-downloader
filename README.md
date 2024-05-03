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
    FROM python:3.12-alpine
    WORKDIR /app
    EXPOSE 8501
    COPY requirements.txt .
    RUN pip install -r requirements.txt
    COPY app.py . 
    CMD ["streamlit", "run", "app.py"]
```

Trong đó
> - `FROM python:3.12-alpine`: Sử dụng python:3.12-alpine làm base image
> - `WORKDIR /app`: Thiết lập thư mục làm trong container
> - `EXPOSE 8501`: Cấu hình cổng cho image là 8501
> - `COPY requirements.txt .`: Copy file requirements.txt trong container
> - `RUN pip install -r requirements.txt`: Cài đặt các thư viện cần thiết
> - `COPY app.py .`: Copy mã mã nguồn vào trong container
> - `CMD ["streamlit", "run", "app.py"]`: Dùng để chạy ứng dụng web khi container được khởi động

## Build một image

Để build một image, ta dùng lệnh: 

```base
    docker build -t youtube-downloader .
```

> ⚠️: đừng quên dấu chấm ở cuối


Lệnh `docker build` sẽ sử dụng Dockerfile để build một image mới

Cờ `-t`: `tag`. Có thể hiểu đây là tên của image và có thể tham chiếu đến nó khi chạy một container

Dấu `.` sẽ cho docker biết Dockerfile hiện tại đang ở đâu. Trong ví dụ này nó ở trong thư mục gốc

## Khởi chạy container

Để chạy một container ta sẽ sử dụng lệnh `docker run`

```base
    docker run -dp 127.0.0.1:8501:8501 youtube-downloader
```

> - Cờ `d` hay `--detach`: cho phép container của bạn chạy ở chế độ nền. Bạn có thể kiểm tra container của bạn bằng lệnh `docker ps`
> - Cờ `p` hay `--publish`: tạo ánh xạ giữa localhost và container. Nếu không có sự ánh xạ này bạn không thể nào truy cập được ứng dụng từ máy của bạn

Đi đến trình duyệt và xem thành quả [localhost:8501](http://localhost:8501/)

## Hướng dẫn nhanh

Dockerfile này đã được upload lên [hub.docker.com](https://hub.docker.com/). Bạn có thể pull về bằng: 

```bash
    docker pull lockman04/youtube-downloader:latest
```

## Tùy chọn lệch `docker run`
Đây là một số tùy chọn và tham số phổ biến:
1. Tùy chọn `-d`: Cho phép container chạy ở chế độ nền (daemon):
```bash 
docker run -d youtube-downloader
```
2. Tùy chọn `--name`: Đặt tên cho container:
```bash
docker run --name my-container youtube-downloader
```
3. Tùy chọn `-p`: ánh xạ cổng từ host vào container:
```bash 
docker run -p 8080:80 nginx 
```
4. Tùy chọn `e`: Đặt biến môi trường trong container: 
```bash 
docker run -e ENV_VAR=value youtube-downloader
```
5. Tùy chọn `-it`: Mở terminal sau khi container được khởi chạy:
```bash
docker run -it help
```
6. Tùy chọn `--rm`: Tự động xóa container khi kết thúc:
```bash
docker run --rm youtube-downloader
```
7. ...


## Bind Mount
![](https://docs.docker.com/storage/images/types-of-mounts-bind.webp?w=450&h=300)

Để bắt đầu hãy chạy lệnh dưới đây:
```bash 
docker run -it --mount type=bind,src="$(pwd)",target=/src ubuntu bash
```

Tùy chọn `--mount type=bind` sẽ yêu cầu Docker tạo một bind mount. `src` là thư mục làm hiện tại trên host là ở đâu và `target` là nơi thư mục đó xuất hiện bên trong container

Sau khi chạy, Docker sẽ bắt đầu một phiên `bash` tương tác trong thư mục gốc của container

![](https://raw.githubusercontent.com/LockMan04/Stored/main/youtube-downloader/Screenshot4.png)

Di chuyển vào thư mục `src`. Có thể thấy rằng nội dung của thư mục này sẽ giống như thư mục `youtube-downloader` trên host

![](https://raw.githubusercontent.com/LockMan04/Stored/main/youtube-downloader/Screenshot5.png)

Bây giờ hãy thử tạo một file mới có tên là `myfile.txt`
```bash
    touch myfile.txt
```

![](https://raw.githubusercontent.com/LockMan04/Stored/main/youtube-downloader/Screenshot6.png)

Mở mã nguồn của bạn quan sát và thấy rằng file `myfile.txt` cũng nằm ở trong thư mực

![](https://raw.githubusercontent.com/LockMan04/Stored/main/youtube-downloader/Screenshot7.png)

Từ máy của bạn, hãy xóa file `myfile.txt`

Khi `ls` một lần nữa trong container, sẽ thấy `myfile.txt` sẽ biến mất

![](https://raw.githubusercontent.com/LockMan04/Stored/main/youtube-downloader/Screenshot8.png)

> Dùng `Crl` + `D` để dừng phiên container

## Thanks



