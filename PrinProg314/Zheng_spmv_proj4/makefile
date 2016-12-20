#For this file, I owe my soul to:
#https://devblogs.nvidia.com/parallelforall/separate-compilation-linking-cuda-device-code

CC = /usr/local/cuda-7.5/bin/nvcc
objects = mmio.o

all: $(objects)
	$(CC) -arch=sm_20 $(objects) -o spmv

%.o: %.c
	$(CC) -x cu -arch=sm_20 -I. -dc $< -o $@

clean:
	rm -f *.o spmv
