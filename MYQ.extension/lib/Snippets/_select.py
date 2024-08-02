# -*- coding: utf-8 -*-
import pprint
from operator import itemgetter
from Autodesk.Revit.DB import *
from pprint import PrettyPrinter

uidoc = __revit__.ActiveUIDocument
doc   = __revit__.ActiveUIDocument.Document


def get_schedule_by_name(name):
    collector = FilteredElementCollector(doc).OfClass(ViewSchedule).ToElements()
    for item in collector:
        if item.Name == name:
            return item


def get_viewports(sheet):
    collector = FilteredElementCollector(doc, sheet.Id)
    collector.OfClass(Viewport)
    all_viewports = collector.ToElements()
    return all_viewports


def get_sheets_by_room(room_number):
    sheets = FilteredElementCollector(doc).OfClass(ViewSheet).ToElements()
    result = list()
    for sheet in sheets:
        sheet_number = sheet.GetParameters("Sheet Number")[0].AsString().split(' - ')
        if len(sheet_number) < 2:
            continue
        m = sheet_number[-1].split('-')[0]

        if m[1:] == room_number and sheet_number[0] == 'ID' and m[0] == '3':
            result.append(sheet)
    return result


def get_viewport_parameter_value(viewport, parameter_name):
    parameters = viewport.Parameters
    parameter = next((p for p in parameters if p.Definition.Name == parameter_name), None)
    type_name = parameter.AsValueString()
    return type_name


def get_view_parameter_value(view, parameter_name):
    parameters = view.Parameters
    parameter = next((p for p in parameters if p.Definition.Name == parameter_name), None)
    type_name = parameter.AsValueString()
    return type_name


def get_element_parameter_value(element, parameter_name):
    parameters = element.Parameters
    parameter = next((p for p in parameters if p.Definition.Name == parameter_name), None)

    if parameter is not None:
        type_name = parameter.AsValueString()
        return type_name
    return None


def get_a1_block():
    title_blocks = (FilteredElementCollector(doc).OfCategory(
        BuiltInCategory.OST_TitleBlocks).WhereElementIsElementType().ToElements())
    a1_title_block = None
    for q in title_blocks:
        if q.FamilyName == "ALEA+ - A1 NEW":
            a1_title_block = q
            return a1_title_block
    return a1_title_block


def get_3000_plan_views():
    all_views = FilteredElementCollector(doc).OfClass(ViewPlan).ToElements()
    results = list()

    for view in all_views:
        if get_view_parameter_value(view, 'Type') == 'Interior - Working':
            results.append(view)

    return results


def get_floor_plan_views(view_type):
    all_views = FilteredElementCollector(doc).OfClass(ViewPlan).ToElements()
    results = list()

    for view in all_views:
        if get_view_parameter_value(view, 'Type') == view_type:
            results.append(view)

    return results


def get_all_walls_in_view(view):
    all_walls = FilteredElementCollector(doc, view.Id).OfCategory(BuiltInCategory.OST_Walls).ToElements()
    return all_walls


def get_walls_by_type(wall_type, view_id):
    if type(wall_type) != str:
        raise Exception("Provide string as wall type")
    results = list()
    all_walls = FilteredElementCollector(doc, view_id).OfCategory(BuiltInCategory.OST_Walls).ToElements()

    for wall in all_walls:
        wall_type_name = get_element_parameter_value(wall, "Type")
        if wall_type_name == wall_type:
            results.append(wall)

    return results


def get_text_note_by_type(tag_family_req, tag_type_req):
    tags = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_TextNotes).ToElements()
    for tag in tags:
        tag_family = get_element_parameter_value(tag, "Family")
        tag_type = get_element_parameter_value(tag, "Type")
        if tag_type == tag_type_req and tag_family == tag_family_req:
            return tag
        else:
            continue


def get_furniture_tag_by_type(tag_family_req, tag_type_req):
    tags = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_FurnitureTags).WhereElementIsElementType().ToElements()
    for tag in tags:
        tag_family = get_element_parameter_value(tag, "Family Name")
        tag_type = get_element_parameter_value(tag, "Type Name")
        if tag_type == tag_type_req and tag_family == tag_family_req:
            return tag
        else:
            continue


def get_wall_tag_by_type(tag_family_req, tag_type_req):
    tags = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_WallTags).WhereElementIsElementType().ToElements()
    for tag in tags:
        tag_family = get_element_parameter_value(tag, "Family Name")
        tag_type = get_element_parameter_value(tag, "Type Name")
        if tag_type == tag_type_req and tag_family == tag_family_req:
            return tag
        else:
            continue


def get_a2_block():
    #
    title_blocks = (FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_TitleBlocks).WhereElementIsElementType().ToElements())
    # title_block_ = None
    #
    # bbox = view_.get_BoundingBox(None)
    # min_ = bbox.Min
    # max_ = bbox.Max
    #
    # min_x = min_.X
    # max_x = max_.X
    # min_y = min_.Y
    # max_y = max_.Y
    #
    # view_width = max_x - min_x
    # view_height = max_y - min_y
    #
    # a1_title_block = None
    a2_title_block = None

    for q in title_blocks:
        if q.FamilyName == "ALEA+ - A2 NEW":
            a2_title_block = q
            title_block_index = 1

    # for qq in title_blocks:
    #     if qq.FamilyName == "ALEA+ - A1 NEW":
    #         a1_title_block = qq
    #         title_block_index = 0
    #
    # if view_height * Sizes.cm_to_feet.value * 1.15 > Sizes.a2_paper_height.value:
    #     return a1_title_block
    # else:
    return a2_title_block


def get_sheets_by_series(series):
    all_sheets = FilteredElementCollector(doc).OfClass(ViewSheet).ToElements()
    results = list()

    for sheet in all_sheets:
        sheet_series_param = sheet.GetParameters("Sheet series")

        if len(sheet_series_param) == 0:
            continue

        sheet_series = sheet_series_param[0].AsString()

        if sheet_series == series:
            results.append(sheet)

    return results


def get_image_by_name(name):
    results = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_RasterImages).ToElements()
    for img in results:
        print img
        if name == img.GetParameters("Type Name")[0].AsString():
            return img
    return None


def get_all_images():
    results = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_RasterImages).ToElements()
    return results


def get_image_count(name):
    results = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_RasterImages).ToElements()
    count = 0
    for img in results:
        if name == img.GetParameters("Type Name")[0].AsString():
            count += 1

    return count


def get_generic_annotation(name):
    results = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_GenericAnnotation).ToElements()

    for i in results:
        if name == i.GetParameters("Type Name")[0].AsString():
            return i
    return None


def get_view_name_from_viewport(viewport, par_name):
    v_name = get_viewport_parameter_value(viewport, par_name)
    return v_name


def get_families_by_category(category):
    results = FilteredElementCollector(doc).OfCategory(category).ToElements()
    return results


def get_family_by_category_and_type_name(category, type_name):
    pass
