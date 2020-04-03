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
import pandas as pd

if __name__ == '__main__':

    # Load the conrod parts:
    D0 = PartChecker("./parts/conrod/Stang_met_gat150.STEP")
    D1 = PartChecker("./parts/conrod/Stang_met_gat200.STEP")
    D2 = PartChecker("./parts/conrod/Stang_met_gat250.STEP")
    D3 = PartChecker("./parts/conrod/Stang_met_gat300.STEP")
    D4 = PartChecker("./parts/conrod/Stang_met_gat350.STEP")

    # Load the crank parts:
    D_0 = PartChecker("./parts/crank/BASE050.STEP")
    Da = PartChecker("./parts/crank/BASE060.STEP")
    Db = PartChecker("./parts/crank/BASE070.STEP")
    Dc = PartChecker("./parts/crank/BASE080.STEP")
    Dd = PartChecker("./parts/crank/BASE090.STEP")

    # Obtain the masses of conrods:

    mass_conrod = [D0.parts[0].Shape.Mass / D0.parts[0].Shape.Mass,
                D1.parts[0].Shape.Mass / D0.parts[0].Shape.Mass,
                D2.parts[0].Shape.Mass / D0.parts[0].Shape.Mass,
                D3.parts[0].Shape.Mass / D0.parts[0].Shape.Mass,
                D4.parts[0].Shape.Mass / D0.parts[0].Shape.Mass]

    # Obtain the inertia about the x-axis of conrods:

    inertia_conrod = [D0.parts[0].Shape.getMomentOfInertia(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(1, 0, 0)) / D0.parts[
        0].Shape.getMomentOfInertia(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(1, 0, 0)),
                      D1.parts[0].Shape.getMomentOfInertia(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(1, 0, 0)) / D0.parts[
                          0].Shape.getMomentOfInertia(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(1, 0, 0)),
                      D2.parts[0].Shape.getMomentOfInertia(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(1, 0, 0)) / D0.parts[
                          0].Shape.getMomentOfInertia(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(1, 0, 0)),
                      D3.parts[0].Shape.getMomentOfInertia(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(1, 0, 0)) / D0.parts[
                          0].Shape.getMomentOfInertia(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(1, 0, 0)),
                      D4.parts[0].Shape.getMomentOfInertia(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(1, 0, 0)) / D0.parts[
                          0].Shape.getMomentOfInertia(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(1, 0, 0))]

    # Obtain the masses of crank:

    mass_crank = [D_0.parts[0].Shape.Mass / D_0.parts[0].Shape.Mass,
                  Da.parts[0].Shape.Mass / D_0.parts[0].Shape.Mass,
                  Db.parts[0].Shape.Mass / D_0.parts[0].Shape.Mass,
                  Dc.parts[0].Shape.Mass / D_0.parts[0].Shape.Mass,
                  Dd.parts[0].Shape.Mass / D_0.parts[0].Shape.Mass]

    # Obtain the inertia about the z-axis of the crank:

    inertia_crank = [D_0.parts[0].Shape.getMomentOfInertia(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(0, 0, 1)) / D_0.parts[
        0].Shape.getMomentOfInertia(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(0, 0, 1)),
                      Da.parts[0].Shape.getMomentOfInertia(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(0, 0, 1)) / D_0.parts[
                          0].Shape.getMomentOfInertia(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(0, 0, 1)),
                      Db.parts[0].Shape.getMomentOfInertia(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(0, 0, 1)) / D_0.parts[
                          0].Shape.getMomentOfInertia(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(0, 0, 1)),
                      Dc.parts[0].Shape.getMomentOfInertia(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(0, 0, 1)) / D_0.parts[
                          0].Shape.getMomentOfInertia(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(0, 0, 1)),
                      Dd.parts[0].Shape.getMomentOfInertia(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(0, 0, 1)) / D_0.parts[
                          0].Shape.getMomentOfInertia(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(0, 0, 1))]

    # Place the results in a table:
    d1 = {'$L_2$': [150, 200, 250, 300, 350], '$M_2$': mass_conrod, '$J_2$':inertia_conrod}
    df = pd.DataFrame(data=d1)
    df.to_csv('conrods.csv')
    df.to_latex("conrods.tex",float_format="%.2f")

    d2 = {'$L_1$': [50, 60, 70, 80, 90], '$M_1$': mass_crank, '$J_1$':inertia_crank}
    df2 = pd.DataFrame(data=d2)
    df2.to_csv('cranks.csv')
    df2.to_latex("cranks.tex",float_format="%.2f")