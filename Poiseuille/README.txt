# Instructions to run and analyse the Poiseuille system

Step 1: Run the LAMMPS script using the command "mpirun -np 2 lammps-daily < poiseuille.lmp".
Step 2: Run the VMD script using the command "vmd -dispdev text -e create_psf.tcl".
Step 3: Run the Python script using the command "python plot.py".
