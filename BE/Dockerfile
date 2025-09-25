#Docker formatting starts with FROM instruction
#Read requirements.txt to find which Python version for containers maybe?
#Create a new build stage from a base image (Docker syntax)

FROM python:3.12-slim

#venv does not affect this because we do not copy it
#Copy files and directory (Docker Syntax)
#FROM BEST PRACTICES DOCKER:
#If you have multiple Dockerfile steps that use different files from your 
#context, COPY them individually, rather than all at once. 
#This will ensure that each step’s build cache is only invalidated 
#(forcing the step to be re-run)if the specifically required files change.
#WORKDIR is good practice but not in the assignment here?
# / will put .txt into root of container 

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY calculator_helper.py /
COPY calculator_rest_service.py /
COPY models.py /

# entrypoint is what to run when container starts
# so copy modules before this (layer by layer)
COPY calculator.py /
ENTRYPOINT [ "python", "calculator.py" ]