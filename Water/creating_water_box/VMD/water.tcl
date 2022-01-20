package require solvate
package require topotools

set molname "water"

solvate -minmax {{-10.0 -10.0 -10.0} {10.0 10.0 10.0}} -o ${molname}

mol load psf ${molname}.psf pdb ${molname}.pdb

set hyd [atomselect top "type HT"]
$hyd set type 1HT
$hyd set charge 0.4238
set oxy [atomselect top "type OT"]
$oxy set type 2OT
$oxy set charge -0.8476

topo writelammpsdata water.lmpsys

topo readlammpsdata water.lmpsys
set sel [atomselect top water]
set mm [measure minmax $sel]
puts $mm
set xlo [format %.4f [expr [lindex $mm 0 0]-5.0] ]
set xhi [format %.4f [expr [lindex $mm 1 0]+5.0] ]
set ylo [format %.4f [expr [lindex $mm 0 1]-5.0] ]
set yhi [format %.4f [expr [lindex $mm 1 1]+5.0] ]
set zlo [format %.4f [expr [lindex $mm 0 2]-5.0] ]
set zhi [format %.4f [expr [lindex $mm 1 2]+5.0] ]

exec sed -i "12s/.*/  $xlo $xhi  xlo xhi/" water.lmpsys
exec sed -i "13s/.*/  $ylo $yhi  ylo yhi/" water.lmpsys
exec sed -i "14s/.*/  $zlo $zhi  zlo zhi/" water.lmpsys

exec rm -f water.log

mol delete all
exit

