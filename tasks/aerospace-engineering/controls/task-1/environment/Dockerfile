FROM python:3.12-slim

RUN pip install openpyxl==3.1.5 mpmath==1.3.0

WORKDIR /workspace

COPY data /workspace/data

RUN mkdir -p /logs/agent /logs/verifier