package require psfgen
package require topotools
package require pbctools

topo readlammpsdata atomic.lmpsys
set sel [atomselect top all]
$sel writepsf atomic.psf

mol delete all
exit

