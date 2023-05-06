# 
FROM python:3.11

# 
WORKDIR /nebulaspock

# 
COPY ./requirements.txt .

# 
RUN pip install -r requirements.txt

# 
COPY ./main.py .

# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]