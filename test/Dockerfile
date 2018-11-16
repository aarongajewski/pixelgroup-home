FROM python:2.7.9

ADD . /opt

RUN pip install -r /opt/requirements.txt

WORKDIR /opt

CMD nosetests test.py --with-xunit --xunit-file="/nosetests.xml"
