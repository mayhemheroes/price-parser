#!/usr/bin/python3
import atheris
import sys

with atheris.instrument_imports():
    from price_parser import Price

@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    in_str = fdp.ConsumeString(128)
    price = Price.fromstring(in_str)

    if price.amount == None:
        return

    if price.currency == None:
        return

    assert(type(price.currency) == str, 'currency should be a string')
    assert(type(price.amount) == float, 'currency should be a float')

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()