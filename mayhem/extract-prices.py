#!/usr/bin/python3
import atheris
import sys

with atheris.instrument_imports():
    from price_parser import Price

@atheris.instrument_func
def ValidateResult(price):
    if price.amount == None:
        return

    if price.currency == None:
        return

    assert(type(price.currency) == str, 'currency should be a string')
    assert(type(price.amount) == float, 'currency should be a float')

@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    num = fdp.ConsumeIntInRange(0, 2)
    in_str_1 = fdp.ConsumeUnicodeNoSurrogates(64)
    in_str_2 = fdp.ConsumeUnicodeNoSurrogates(64)
    in_str_3 = fdp.ConsumeUnicodeNoSurrogates(64)

    if num == 0:
        ValidateResult(Price.fromstring(in_str_1))

    if num == 1:
        ValidateResult(Price.fromstring(in_str_1, in_str_2))

    if num == 2:
        ValidateResult(Price.fromstring(in_str_3, in_str_2, in_str_3))

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()