#/bin/bash


# Using LLNL job handler (srun)
LD_PRELOAD=../../../install/lib/libstracker.so mpiexec -n 16 ./test
