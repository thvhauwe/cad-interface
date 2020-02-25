# FreeCAD specific imports:

import FreeCAD
import FreeCAD as App
import Part
import numpy as np
import warnings as warn

# End of FreeCAD specific imports
# -----
def loadAssemblyFromFile(file):
    """loadAssemblyFromFile

    Open a 3D CAD assembly file, return the document object and [list of all the parts]
    """

    FreeCAD.open(file)
    doc = App.activeDocument()
    doc = FreeCAD.ActiveDocument
    objs = FreeCAD.ActiveDocument.Objects
    return doc, objs


def extractObjects(InputList: list, ID: str) -> list:
    """
    filterListByID

    Input == Assembly
    Output == List of selected objects

    Typical run with (list,'Part::Feature') to extract the features (of parts) of the assembly
    """

    filteredList = []
    for x in InputList:
        if (x.TypeId == ID):
            filteredList.append(x)
    print(f"Detected {len(filteredList)} different parts in assembly")
    return filteredList


def nestedCaller(obj:Part.Feature, key:str):
    """
    Auxiliary method for nestedTester

    :param obj: object to call
    :param key: field to call
    :return: object.field
    """
    return getattr(obj, key)


def nestedTester(obj_b:Part.Feature, property:str):
    """
    nestedTester is a function such that a property of 'A.B.C' is decomposed,
    such that the attribute C of object A.B is called correctly

    It is generic in the sense that property can consist out of 1, 2 or N pieces, seperated by '.'
    the corresponding (N-1) object is called with attribute N

    :param obj_b: the Part.Feature to be called
    :param property: the property string
    :return: The called attribute
    """

    property_list = property.split(".")  # This enables the 'nested' part
    final = None
    temp = obj_b
    for i in range(len(property_list)):
        final = nestedCaller(temp, property_list[i])
        temp = final  # Final can be the object to call, or the property

    return final  # Returns a property value


class PartChecker:
    def __init__(self, filestring):
        self.document, self._objects = loadAssemblyFromFile(filestring)
        self.parts = extractObjects(self._objects,'Part::Feature')  # In FreeCAD terminology, this is a Part

    def single_feature_check(self, pc_other, property):
        l1 = self.parts
        l2 = pc_other.parts
        statusmatrix = np.zeros([len(l1), len(l2)])
        exitcode = -1
        diffstring = ""

        diff_elements = []

        try:
            if (len(l1) == len(l2)):

                for i in range(len(l1)):
                    check = nestedTester(l1[i], property) == nestedTester(l2[i], property)
                    statusmatrix[i, i] = check
                    if not check:
                        diff_elements.append(i)

                        diffstring = diffstring + " -- " + f"Base: {self.document.Name}, "\
                                                           f"Other: {pc_other.document.Name}, "\
                                                           f"Property: {property}, " \
                                                           f"Part Name (Base): {l1[i].Label}, " \
                                                           f"Value_Base: {nestedTester(l1[i], property)}, " \
                                                           f"Value_Other: {nestedTester(l2[i], property)} \n"

                if np.array_equal(np.diag(statusmatrix), np.ones([len(l1)])):
                    exitcode = 1  # All parts has the same value for property
                else:
                    exitcode = 2

            else:
                exitcode = 3
        except Exception:

            warn.warn("--- An error occured in function call listCompare with inputs: ---")
            print(l1)
            print(l2)
            print(property)
            warn.warn("--- End of of except statement ---")

        finally:
            return exitcode, diffstring, diff_elements

    def compare(self, pc_other, list_of_features):
        keys = list_of_features
        values = [self.single_feature_check(pc_other,list_of_features[i])[0] for i in range(0,len(list_of_features))]
        return dict(zip(keys,values))

    def basic_info(self):
        print('TODO: implement')
