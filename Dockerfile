FROM python:3.7.0 As builder
COPY requirements.txt .
RUN  pip install --upgrade pip && pip install -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt
FROM python:3.7.0-alpine3.7
COPY --from=builder /usr/local/lib/python3.7/site-packages /usr/local/lib/python3.7/site-packages
COPY --from=builder /usr/local/bin/uvicorn /usr/local/bin/
#Set System TimeZone
# Set 阿里云软件更新源
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories

RUN apk add --no-cache tzdata bash
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN mkdir -p /xwkj/app && mkdir -p /xwkj/data/log/op-cicd-api && chmod 775 -R /xwkj/

WORKDIR /xwkj/app/op-cicd-api
COPY . .
CMD  python boot.py
