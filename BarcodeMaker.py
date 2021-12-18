from barcode import EAN13
number = "133815381610"
my_code = EAN13(number)
my_code.save("barcode")
