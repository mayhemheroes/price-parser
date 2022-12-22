#!/usr/bin/python3
import atheris
import sys

with atheris.instrument_imports():
    from price_parser import Price

@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    num = fdp.ConsumeIntInRange(0, 2)     

    if num == 0:
        in_str_1 = fdp.ConsumeUnicodeNoSurrogates(64)
        in_str_2 = fdp.ConsumeUnicodeNoSurrogates(64)
        price = Price.fromstring(in_str_1, currency_hint=in_str_2)

    if num == 1:
        in_str_1 = fdp.ConsumeUnicodeNoSurrogates(64)
        in_str_2 = fdp.ConsumeUnicodeNoSurrogates(64)
        price = Price.fromstring(in_str_1, decimal_separator=in_str_2)

    if num == 2:
        in_str_1 = fdp.ConsumeUnicodeNoSurrogates(64)
        in_str_2 = fdp.ConsumeUnicodeNoSurrogates(64)
        in_str_3 = fdp.ConsumeUnicodeNoSurrogates(64)
        price = Price.fromstring(in_str_1, currency_hint=in_str_2,  decimal_separator=in_str_3)

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()