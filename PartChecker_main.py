# --------------------------------------------
#
# Author: Thijs Van Hauwermeiren
# EEDT-DC - Flanders Make @ Universiteit Gent
#
# Email: thijs.vanhauwermeiren@ugent.be
# Tel: 09 264 34 18
#
# --------------------------------------------
#
# License: MIT
#
# Part of https://github.com/thvhauwe/cad-interface
#
# Tested on recent Windows 10, using PyCharm IDE and FreeCAD 0.18

# --------------------------------------------
# How to run this code:
#
# Use the built-in FreeCAD Conda python executable (Default since version 0.18).
# This is most easily done using PyCharm.
#
# On my system, the FreeCAD-conda-python executeable is located in $USER-HOME\AppData\Local\FreeCAD 0.18\bin\python.exe
#
# Add this python interpreter to your PyCharm project to be able to run this file
# --------------------------------------------


# Script file for END USER:

from PartChecker import PartChecker
import FreeCAD
import numpy as np

if __name__ == '__main__':

    # Three assembly files are loaded in: Base, v1 (identical), v2 (slightly adapted)

    Base_Assembly = PartChecker("GearboxAssembly_v3.FCStd")
    Assembly_v1 = PartChecker("GearboxAssembly_v3_ID.FCStd")
    Assembly_v2 = PartChecker("GearboxAssembly_v3_NON_ID.FCStd")
    # difference compared to Base: All labels renamed,
    # Small gear displaced


    #  method `single_feature_check` checks two PartChecker objects for 1 property

    a, b, c = Base_Assembly.single_feature_check(Assembly_v1, 'Label')
    x, y, z = Base_Assembly.single_feature_check(Assembly_v2,'Label')

    # Returns an exitcode (1 == identical for property, 2 == difference detected, other == error), a diff string, diff indices
    # print(y) to see where Base and v2 differ and what the values are
    print(y)

    # More realistic use-case: provide a list of properties/features to check if they match: ListOfFeatures (LOF)

    LOF=['Label','Shape.Mass','Shape.Volume','Shape.Placement.Base','Shape.Placement.Rotation']
    p = Base_Assembly.compare(Assembly_v1, LOF)
    q = Base_Assembly.compare(Assembly_v2, LOF)

    # p,q == a dict
    # One can act upon detected differences using `for k,v in p.items():`

    for k, v in q.items():
        if v == 2:
            # Difference detected between Base and Assembly_v2 for this problem, fetching the diff string:
            print(f'Got an exitcode 2 for property {k}, fetching diff-string:')
            a, b, c = Base_Assembly.single_feature_check(Assembly_v2, k)
            print(b)

