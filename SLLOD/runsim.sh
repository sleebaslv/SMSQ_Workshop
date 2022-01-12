for srate in 0.01 0.02 0.05 0.08 0.1 0.2 0.5 0.8 1.0 1.2 1.5 1.8 2.0 2.2 2.5  
do

mpirun -np 8 lmp_mpi -in sllod.lmp -var strain_rate ${srate} 

done
