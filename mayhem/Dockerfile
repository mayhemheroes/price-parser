FROM fuzzers/atheris:2.0.7-python3.9
COPY . /price-parser

WORKDIR /price-parser
RUN pip install .
RUN chmod +x /price-parser/mayhem/extract-prices.py