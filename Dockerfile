ARG path=test2

FROM python:3.8-slim-buster


RUN mkdir /test2
WORKDIR /test2


RUN apt-get update; apt-get install -y curl sudo gnupg2 libodbc1 g++

RUN sudo su
RUN apt-get update && \
    apt-get install -y apt-transport-https && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install msodbcsql17 unixodbc-dev mssql-tools -y
RUN exit


RUN apt-get install -y --no-install-recommends \
    unixodbc-dev \
    unixodbc \
    libpq-dev 

ADD requirements.txt /test2/
RUN pip3 install -r requirements.txt
ADD . /test2/



ENTRYPOINT [ "python" ]
CMD ["app.py"]