#What?

These aren't quite testcases. Here is just some help for the assignment (mostly just using the tools properly).

The [howtorunCUDA.md](howtorunCUDA.md) details where the binaries and libraries are. Most of this is handled by the provided makefile, though the library locations would be useful. Also, **Google is your friend**.

The makefile is indispensible if you want multiple files. It handles the fact that there are two assembly languages all the code must compile to: PTX (for the GPU) and x86\_64 (ye olde familliar from comp arch). Then, the two have to link... Luckily, the make file knows how to tell nvcc (the CUDA compiler) to do all that. All you have to do is make sure the object files (compiled libraries) you want are in the variable `objects` ([see here](makefile#5) for details).

Also, mmio.h and mmio.c are included from the previous assignment. They've been mildly edited to do all the file IO directly (essentially copy-pasting from the given code in project 3). Also, there is a MatrixInfo struct by yours truly that you may find useful.
