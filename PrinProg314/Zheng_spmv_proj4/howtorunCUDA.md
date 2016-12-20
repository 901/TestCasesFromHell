/usr/local/cuda-7.5/bin is useful...
nvcc, cuda-gdb, nvlink, and nvprof are at this path.
In fact:
`export PATH=$PATH:/usr/local/cuda-7.5/bin`
Or, in your home directory,
`echo "export PATH=\$PATH:/usr/local/cuda7.5/bin" >> .bashrc`
and then `bash -i` every time you login through ssh (or PuTTY).
`null.cs.rutgers.edu` is the shortest name with CUDA enabled (so far).

`/usr/local/cuda-7.5/include` has the CUDA includes. `driver_types.h` has the definition of `cudaError\_t`. `cudaGetErrorString(cudaError_t myError)` is also useful to this end.

cuda-gdb doesn't want to work since the GPU cannot be arbitrarily stalled (it also has screens to render, the poor busy thing).

To get started, [this tutorial is handy](https://www.olcf.ornl.gov/tutorials/cuda-vector-addition/).
