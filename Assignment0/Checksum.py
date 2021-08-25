import zlib

with open("test.jpg", "rb") as f:
    bytes = f.read()
checksum = zlib.crc32(bytes)

