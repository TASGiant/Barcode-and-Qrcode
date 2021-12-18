from barcode import EAN13
from barcode.writer import ImageWriter

number = "133815381610"

my_code = EAN13(number, writer=ImageWriter())

my_code.save("BarCode")
