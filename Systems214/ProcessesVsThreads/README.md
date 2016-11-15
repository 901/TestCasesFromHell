So, there are a few things here...

dummy1.txt is the testcase. The output for `./compressT_LOLS dummy1.txt 5` is also provided.

test\_enc.py is expected to work with any version of python. It accepts the uncompressed file and a list of compressed files (in order).

`python test_enc.py dummy1.txt dummy_*`
and
`python3 test_enc.py dummy1.txt dummy_*`
both work. They print out the result of the decompression, the alphabetic contents of the original and then a boolean indicating the success
of the test.
