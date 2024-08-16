# -*- coding: utf-8 -*-
import pprint
from operator import itemgetter
from Autodesk.Revit.DB import *
from pprint import PrettyPrinter
from Autodesk.Revit.UI.Selection import ISelectionFilter, ObjectType, Selection

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document


class CustomISelectionFilter(ISelectionFilter):
    """Filter user selection to certain element."""

    def __init__(self, cats):
        self.cats = cats

    def AllowElement(self, e):
        if str(e.Category.Id) == str(self.cats):
            #if e.Category.Name == "Walls"
            return True
        return False


def pick_wall(given_uidoc=uidoc):
    """Function to promt user to select a wall element in Revit UI."""
    wall_ref = given_uidoc.Selection.PickObject(ObjectType.Element, CustomISelectionFilter("-2000011"),
                                                "Select a Wall")  # -2000011 <- Id of OST_Walls
    wall = given_uidoc.Document.GetElement(wall_ref)
    return wall
