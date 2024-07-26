# -*- coding: utf-8 -*-
import pprint
from operator import itemgetter
from Autodesk.Revit.DB import *
from pprint import PrettyPrinter

from constants import Sizes

uidoc = __revit__.ActiveUIDocument
doc   = __revit__.ActiveUIDocument.Document


def get_viewport_dimensions(viewport):
    viewport_outline = viewport.GetBoxOutline()

    viewport_min = viewport_outline.MinimumPoint
    viewport_max = viewport_outline.MaximumPoint
    result_vector = viewport_max - viewport_min
    width = result_vector.X * Sizes.feet_to_cm.value
    height = result_vector.Y * Sizes.feet_to_cm.value
    return width, height


def get_scaled_size(view, scale):
    w, h = get_view_size(view)
    scaled_w = w / scale
    scaled_h = h / scale
    return scaled_w, scaled_h


def get_view_size(view_):
    bbox = view_.get_BoundingBox(None)
    min_ = bbox.Min
    max_ = bbox.Max

    min_x = min_.X
    max_x = max_.X
    min_y = min_.Y
    max_y = max_.Y

    view_width = max_x - min_x
    view_height = max_y - min_y

    view_width_cm_scale = view_width * Sizes.feet_to_cm.value
    view_height_cm_scale = view_height * Sizes.feet_to_cm.value

    return view_width_cm_scale, view_height_cm_scale
