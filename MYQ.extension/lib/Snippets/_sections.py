# -*- coding: utf-8 -*-
import pprint
from operator import itemgetter
from Autodesk.Revit.DB import *
from pprint import PrettyPrinter

uidoc    = __revit__.ActiveUIDocument
doc      = __revit__.ActiveUIDocument.Document
active_view = uidoc.ActiveView
app      = __revit__.Application
rvt_year = int(app.VersionNumber)


class SectionGenerator:

    def __init__(self, doc, origin, vector, width=1, height=1, offset=1, depth=1, depth_offset=1):
        """General class to create Sections and place them on sheets"""
        # type: XYZ, XYZ, float, float, float, float, float
        self.doc = doc
        self.origin = origin
        self.vector = vector
        self.width = width
        self.height = height
        self.offset = offset
        self.depth = depth
        self.depth_offset = depth_offset

        scale = None
        view_template = None
        title_block_type = None
        section_type = None

    def create_transform(self, mode='elevation'):
        trans = Transform.Identity
        trans.Origin = self.origin
        vector = self.vector.Normilize()

        if mode.lower() == 'elevation':
            trans.BasisX = vector
            trans.BasisY = XYZ.BasisZ
            trans.BasisZ = vector.CrossProduct(XYZ.BasisZ)

        return trans

    def create_section_box(self, mode='elevation'):
        section_box = BoundingBoxXYZ()
        trans = self.create_transform(mode=mode)

        """
        TODO
        """

        section_box.Transform = trans
        return section_box
