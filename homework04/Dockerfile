FROM centos:7.9.2009

RUN yum update -y && \
    yum install -y python3 

RUN pip3 install pytest==7.0.0
RUN yum install -y emacs 

COPY ml_data_analysis.py /code/ml_data_analysis.py
COPY test_ml_data.py /code
COPY Meteorite_Landings.json /code

RUN chmod +rx /code/ml_data_analysis.py 

ENV PATH "/code:$PATH"