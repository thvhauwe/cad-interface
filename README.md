# cad-interface

**Cad-interface** allows to import, access, compare and manipulate CAD files saved in the neutral `STEP` format, using FreeCAD.

Corresponding Author: Thijs.vanhauwermeiren@UGent.be  
Supervisor: Guillaume.crevecoeur@UGent.be   
Organization website: http://www.ugent.be/m-f/en   

This script is supplementary material to support a submitted publication (Fast performance assessment of mechatronic designs integrating CAD and dynamical models with application on servo actuated designs) for IEEE CASE 2020.

### 1. ABSTRACT
----
This scripts allows comparison between different designs of a mechanical assembly or part using the STEP file.
All the parts are available as FreeCad `features`, which have properties `Mass`, `Volume`, `Label`, etc. Calculation of inertia is possible with the method `getMomentOfInertia (pos, rot)` with `pos` the (x,y,z) position and `rot` the rotation axis (as a vector). To compare the inertia of different parts, it is advised to model them such that the rotation center is fixed in the origin of the part, as such `pos = (0, 0, 0)`.

### 2. SOFTWARE DEPENDENCIES
----

1. FreeCAD `ver >=0.18` Available from http://www.freecadweb.org
1. PyCharm IDE (CE) Available from https://www.jetbrains.com/pycharm/

Tested on recent Windows 10.

### 3. INSTALLATION
---------------------------

Clone the repository:
`git clone https://github.com/thvhauwe/cad-interface`

### 4. GETTING STARTED
------------------

Objects can be created by importing `PartChecker.py`. The STEP files used in the publication are available in `./parts`.  
Example usage is in file `PartChecker_main.py`. The documententation is provided inline with the code.

