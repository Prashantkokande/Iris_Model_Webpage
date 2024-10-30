FROM python
COPY . /app
WORKDIR /app
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python app.py runserver 0.0.0.0:8000
