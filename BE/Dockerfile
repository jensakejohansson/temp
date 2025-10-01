FROM python:3.12-slim
COPY requirements.txt calculator.py calculator_helper.py calculator_rest_service.py models.py /
# COPY .. (meaning copy all in the dir)
RUN pip install -r requirements.txt 
#JSON syntax so it  knows to execute as an executable
ENTRYPOINT ["python" , "calculator.py"] 