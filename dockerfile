FROM python:3.7
#COPY [src] [target] 
COPY  ./code target
WORKDIR /target
RUN pip freeze > requirements.txt 
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
CMD ["python", "start.py"]