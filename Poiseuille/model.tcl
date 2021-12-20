package require psfgen
package require topotools
package require pbctools

topo readlammpsdata poiseuille.lmpsys
set sel [atomselect top all]
$sel writepsf poiseuille.psf

mol delete all
exit

