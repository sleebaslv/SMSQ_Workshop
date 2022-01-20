# Instructions to run and analyse the Water system

Step 1: Run the LAMMPS script using the command "mpirun -np 2 lammps-daily < water.lmp".
Step 2: Run the Python script using the command "python plot.py".
Step 3: To visualize the mean square displacement 'choose option 1' or 
	To visualize the radial distribution function 'choose option 2'.

# Intructions to create a water box
# Using Packmol
Step 1; Go to the packmol directory inside creating_water_box directory by typing "cd ./creating_water_box/Packmol".
Step 2: Run the Packmol script using the command "packmol < water.inp".
Step 3: Copy the generated LAMMPS system file to the folder containing the LAMMPS script by typing "cp water.lmpsys ../../".

# Using VMD
Step 1; Go to the VMD directory inside creating_water_box directory by typing "cd ./creating_water_box/VMD".
Step 2: Run the VMD script using the command "vmd -dispdev text -e water.tcl".
Step 3: Copy the generated LAMMPS system file to the folder containing the LAMMPS script by typing "cp water.lmpsys ../../".
