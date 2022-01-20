package require topotools
package require psfgen

mol load pdb water0.pdb

topo guessbonds 
topo guessangles 
topo guessdihedrals 
topo guessimpropers

set sel [atomselect top "type OH"]
$sel set name O
$sel set type OT
$sel set segname U
$sel set resname SPE
$sel set mass 15.9994
$sel set charge -0.8476 

set sel [atomselect top "type 1HH"]
$sel set name 1H
$sel set type HT
$sel set segname U
$sel set resname SPE
$sel set mass 1.0080
$sel set charge 0.4238

set sel [atomselect top "type 2HH"]
$sel set name 2H
$sel set type HT
$sel set segname U
$sel set resname SPE
$sel set mass 1.0080
$sel set charge 0.4238

set sel [atomselect top all]
set num [$sel num]
for {set i 0} {$i < $num} {incr i} {
set atm [atomselect top "index $i"]
$atm set resid $i }

set sel [atomselect top all]
$sel writepsf water.psf
topo writelammpsdata water.lmpsys

topo readlammpsdata water.lmpsys
set sel [atomselect top all]
set mm [measure minmax $sel]
set xlo [format %.4f [expr [lindex $mm 0 0]-0.5] ]
set xhi [format %.4f [expr [lindex $mm 1 0]+0.5] ]
set ylo [format %.4f [expr [lindex $mm 0 1]-0.5] ]
set yhi [format %.4f [expr [lindex $mm 1 1]+0.5] ]
set zlo [format %.4f [expr [lindex $mm 0 2]-0.5] ]
set zhi [format %.4f [expr [lindex $mm 1 2]+0.5] ]

exec sed -i "12s/.*/  $xlo $xhi  xlo xhi/" water.lmpsys
exec sed -i "13s/.*/  $ylo $yhi  ylo yhi/" water.lmpsys
exec sed -i "14s/.*/  $zlo $zhi  zlo zhi/" water.lmpsys

mol delete all
exit
