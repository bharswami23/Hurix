FROM python:3.12-slim

RUN pip install numpy scipy openpyxl mpmath

WORKDIR /workspace

COPY data /workspace/data

RUN mkdir -p /logs/agent /logs/verifier