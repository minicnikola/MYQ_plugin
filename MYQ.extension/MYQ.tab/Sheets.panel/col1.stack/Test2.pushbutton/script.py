import pprint
from operator import itemgetter
import random

import pyrevit.forms
from Autodesk.Revit.DB import *
from pprint import PrettyPrinter

__title__ = "Place views on sheets"
__author__ = "Me"
__doc__ = "--------"

from Snippets._select import get_viewports, get_a2_block
from Snippets.size import get_view_size, get_scaled_size, get_viewport_dimensions
from constants import Sizes


uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document
ui_view = doc.ActiveView

viewport_label_family = None

# parameter_name = 'Family and Type'
parameter_name = 'Type'


# def determine_paper_size(view_):


def get_room_type(number):
    all_rooms = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rooms).ToElements()
    for room in all_rooms:
        if room.Number == number:
            return room.GetParameters("Comments")[0].AsValueString()


def get_room(number):
    all_rooms = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rooms).ToElements()
    for room in all_rooms:
        if room.Number == number:
            return room


def multiple_sheets(view_):
    return False


def create_sheet(name, number, title_block=None):
    print "name : {s}, number : {n}".format(s=name, n=number)
    if title_block is None:
        title_block = get_a2_block()
    sheet_ = ViewSheet.Create(doc, title_block.Id)

    try:
        sheet_.SheetNumber = "ID - 3" + str(number)
    except Exception as e:
        print e
        sheet_.SheetNumber = "ID - 3" + str(number) + str(random.choice(range(1, 30)))

    sheet_.GetParameters("Sheet Name")[0].Set(name)
    sheet_.GetParameters("Sheet Group")[0].Set("Interior")
    # WARNING this should be uncommented
    # sheet_.GetParameters("Sheet Sort")[0].Set('3' + str(number)[0] + "00")
    sheet_.GetParameters("Sheet series")[0].Set("ID3000 - ELEVATIONS")
    return sheet_


def get_title_block():
    pass


def get_viewport_label():
    # collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Viewports)

    all_viewport_lines = FilteredElementCollector(doc).OfClass(Viewport).ToElements()
    for m in all_viewport_lines:
        par_name = m.GetParameters("Type")[0].AsValueString()
        if par_name == 'ALEA_Title w Line':
            return m

    # List to store unique viewport label types
    viewport_label_types = []

    # Iterate through each viewport label and get its type
    # TODO: Try to find a way to change viewport label line type
    # for viewport_label in collector:
    #     kk = viewport_label.Parameters
    #     ttt = "ALEA_Title w Line"
    #     viewport_name_par = next((p for p in kk if p.Definition.Name == ttt), None)
    #     viewport_name = viewport_name_par.AsValueString()
    #     print viewport_name
    #     return viewport_label


def find_plan_views():
    views = FilteredElementCollector(doc).OfClass(View).ToElements()
    plan_views = list()

    for view in views:
        parameters = view.Parameters
        parameter = next((p for p in parameters if p.Definition.Name == parameter_name), None)
        type_name = parameter.AsValueString()

        if type_name == "Interior - Working":
            plan_views.append(view)

    return plan_views


def find_elevation_views():
    views = FilteredElementCollector(doc).OfClass(View).ToElements()
    el_views = list()

    for el_view in views:
        parameters = el_view.Parameters
        parameter = next((p for p in parameters if p.Definition.Name == parameter_name), None)
        type_name = parameter.AsValueString()

        if type_name == "Interior Elevation":
            el_views.append(el_view)
            view_name = el_view.Name

            # view name
            room_number = view_name.split(' - ')[0]
            room_name = view_name.split(' - ')[1]
            width, height = get_view_size(el_view)

    return el_views


def sort_views():
    plan_views = find_plan_views()
    elevation_views = find_elevation_views()
    views = dict()
    for plan_view in plan_views:
        room_views = dict()
        view_name = plan_view.Name
        room_number = view_name.split(' - ')[0]
        room_views['plan'] = plan_view

        for elev_view in elevation_views:
            el_view_name = elev_view.Name
            room_number_elevation_view = el_view_name.split(' - ')[0]
            detail_letter_elevation_view = el_view_name.split(' - ')[-1]
            if room_number_elevation_view == room_number:
                room_views[detail_letter_elevation_view] = elev_view

        views[room_number] = room_views
    return views


def set_plan_label(viewport):
    current_pos_min = viewport.GetBoxOutline().MinimumPoint
    current_pos_max = viewport.GetBoxOutline().MaximumPoint
    k = (current_pos_max-current_pos_min).X * Sizes.feet_to_cm.value - 1.6
    viewport.LabelLineLength = k * Sizes.cm_to_feet.value
    viewport.LabelOffset = XYZ(1.5 * Sizes.cm_to_feet.value, -2 * Sizes.cm_to_feet.value, 0)

    label_id = get_viewport_label()
    if label_id is not None:
        viewport.ChangeTypeId(label_id.GetTypeId())


def set_label_offset(viewport):
    viewport.ChangeTypeId(get_viewport_label().GetTypeId())
    # print '------------'
    # label_outline = viewport.GetLabelOutline()
    # print "Label minimum point : {s}".format(s=label_outline.MinimumPoint)
    # print "Label maximum point : {s}".format(s=label_outline.MaximumPoint)
    current_pos_min = viewport.GetBoxOutline().MinimumPoint
    current_pos_max = viewport.GetBoxOutline().MaximumPoint
    # print "Viewport size min : {mp}, max {ms}".format(mp=current_pos_min, ms=current_pos_max)
    # print "Viewport label line length : {s}".format(s=viewport.LabelLineLength)
    #
    # print "Viewport width : {m}".format(m=current_pos_max-current_pos_min)
    k = (current_pos_max-current_pos_min).X * Sizes.feet_to_cm.value - 2.5 - 4.5 - 1.6
    viewport.LabelLineLength = k * Sizes.cm_to_feet.value
    # if sheet is not None:
    #     print viewport.get_BoundingBox(sheet).Min
    # pos_x = current_pos_min.X
    # pos_y = current_pos_min.Y
    # print pos_x
    # print pos_y
    # plan_viewport.LabelOffset = XYZ((pos_x + 1.5) * Sizes.cm_to_feet.value, (pos_y - 2) * Sizes.cm_to_feet.value, 0)
    viewport.LabelOffset = XYZ(3.9 * Sizes.cm_to_feet.value, -2 * Sizes.cm_to_feet.value, 0)


def place_plan_view(view, sheet):
    plan_viewport = Viewport.Create(doc, sheet.Id, view.Id, XYZ(0, 0, 0))
    box_outline = plan_viewport.GetBoxOutline()
    min_point = box_outline.MinimumPoint
    max_point = box_outline.MaximumPoint
    width = max_point.X - min_point.X
    height = max_point.Y - min_point.Y
    x = width / 2 + 0.075
    title_block = get_a2_block()

    if "A1" in title_block.FamilyName:
        paper_height = Sizes.a1_paper_height.value * Sizes.cm_to_feet.value
        view_offset = height / 2 * 1.15
        y = paper_height - view_offset
    else:
        y = (Sizes.a2_paper_height.value * Sizes.cm_to_feet.value) - (height / 2 * 1.15)

    new_center = XYZ(x, y, 0)
    plan_viewport.SetBoxCenter(new_center)
    set_plan_label(plan_viewport)


# def get_sheets_by_room(room_number):
#     sheets = FilteredElementCollector(doc).OfClass(ViewSheet).ToElements()
#     result = list()
#     for sheet in sheets:
#         sheet_number = sheet.GetParameters("Sheet Number")[0].AsString().split(' - ')
#         if len(sheet_number) < 2:
#             continue
#         m = sheet_number[-1].split('-')[0]
#
#         if m[1:] == room_number and sheet_number[0] == 'ID' and m[0] == '3':
#             result.append(sheet)
#     return result


def create_plan_sheet(plan_view, name):
    pass


def create_elevation_sheet(el_view, name):
    pass

def sort_elevation_by_width(room_views):
    elevation_views = list()
    for room_view in room_views:
        if room_view[0] != 'plan':
            elevation_views.append(room_view)

    # ordered_views = list()
    # arr = np.array(room_views)
    # sorted_arr = room_views.sort(key=)
    elevation_views_list_objects = list()
    for i in elevation_views:
        single_elevation_view = dict()
        w, h = get_scaled_size(i[1], 25)
        single_elevation_view['view'] = i[1]
        single_elevation_view['width'] = w
        elevation_views_list_objects.append(single_elevation_view)

    ordered_views = sorted(elevation_views_list_objects, key=itemgetter('width'))
    return ordered_views


def place_two_by_two_elevations(sheet, plan_view, sorted_elevations):
    vw, vh = get_scaled_size(plan_view, 25)

    one_v = sorted_elevations[0]['view']
    two_v = sorted_elevations[1]['view']
    three_v = sorted_elevations[2]['view']
    four_v = sorted_elevations[3]['view']

    vw_one, vh_one = get_scaled_size(one_v, 25)
    vw_two, vh_two = get_scaled_size(two_v, 25)
    vw_three, vh_three = get_scaled_size(three_v, 25)
    vw_four, vh_four = get_scaled_size(four_v, 25)

    if vw_two + vw_two + vw + 18 < Sizes.a2_paper_width.value:
        print 'kkkkkk'
        center_one = XYZ((vw_one/2 + vw + 9) * Sizes.cm_to_feet.value, (Sizes.a2_paper_height.value - 1.5 - vh_one/2) * Sizes.cm_to_feet.value, 0)
        center_two = XYZ((vw_one/2 + vw + 9) * Sizes.cm_to_feet.value, (Sizes.a2_paper_height.value - 5.5 - vh_two/2 - vh_one) * Sizes.cm_to_feet.value, 0)
        center_three = XYZ((vw_three/2 + vw_one + vw + 16) * Sizes.cm_to_feet.value, (Sizes.a2_paper_height.value - 1.5 - vh_three/2) * Sizes.cm_to_feet.value, 0)
        center_four = XYZ((vw_three/2 + vw_one + vw + 16) * Sizes.cm_to_feet.value, (Sizes.a2_paper_height.value - 5.5 - vh_four/2 - vh_three) * Sizes.cm_to_feet.value, 0)
    else:
        print 'ffffff'
        center_one = XYZ((vw_one / 2 + vw + 7) * Sizes.cm_to_feet.value, (Sizes.a2_paper_height.value - 1.5 - vh_one / 2) * Sizes.cm_to_feet.value, 0)
        center_two = XYZ((vw_one / 2 + vw + 7) * Sizes.cm_to_feet.value, (Sizes.a2_paper_height.value - 5.5 - vh_two/2 - vh_one) * Sizes.cm_to_feet.value, 0)
        center_three = XYZ((vw_three / 2 + vw_one + vw + 10) * Sizes.cm_to_feet.value,
                           (Sizes.a2_paper_height.value - 1.5 - vh_three / 2) * Sizes.cm_to_feet.value, 0)
        center_four = XYZ((vw_three / 2 + vw_one + vw + 10) * Sizes.cm_to_feet.value, (Sizes.a2_paper_height.value - 5.5 - vh_four/2 - vh_three) * Sizes.cm_to_feet.value, 0)

    elevation_one_viewport = Viewport.Create(doc, sheet.Id, one_v.Id, center_one)
    elevation_two_viewport = Viewport.Create(doc, sheet.Id, two_v.Id, center_two)
    elevation_three_viewport = Viewport.Create(doc, sheet.Id, three_v.Id, center_three)
    elevation_four_viewport = Viewport.Create(doc, sheet.Id, four_v.Id, center_four)

    set_label_offset(elevation_one_viewport)
    set_label_offset(elevation_two_viewport)
    set_label_offset(elevation_three_viewport)
    set_label_offset(elevation_four_viewport)

    label_id = get_viewport_label()
    if label_id is not None:
        elevation_one_viewport.ChangeTypeId(label_id.GetTypeId())
        elevation_two_viewport.ChangeTypeId(label_id.GetTypeId())
        elevation_three_viewport.ChangeTypeId(label_id.GetTypeId())
        elevation_four_viewport.ChangeTypeId(label_id.GetTypeId())

    set_detail_letter(elevation_one_viewport)
    set_detail_letter(elevation_two_viewport)
    set_detail_letter(elevation_three_viewport)
    set_detail_letter(elevation_four_viewport)


def set_detail_letter(viewport):
    view_id = viewport.ViewId
    view = doc.GetElement(view_id)
    view_name = view.GetParameters("View Name")[0].AsString()
    view_letter = view_name.split(" - ")[-1]
    param_a = viewport.LookupParameter("Detail Number")
    param_a.Set(view_letter)


def place_rest_on_second_sheet(room_name, room_number, sorted_el):
    elevation_three = sorted_el[2]
    elevation_four = sorted_el[3]

    three_view = elevation_three['view']
    four_view = elevation_four['view']
    vt_w, vt_h = get_scaled_size(three_view, 25)
    vf_w, vf_h = get_scaled_size(four_view, 25)

    sheet = create_sheet(room_name, room_number+'-1')
    el_three_width, el_three_height = get_scaled_size(elevation_three['view'], 25)
    el_four_width, el_four_height = get_scaled_size(elevation_four['view'], 25)
    if el_three_width + el_four_width + 14 > Sizes.a2_paper_width.value:
        # TODO place one below another
        center_one = XYZ(Sizes.a2_paper_width.value/2 * Sizes.cm_to_feet.value, (Sizes.a2_paper_height.value-vt_h/2-3) * Sizes.cm_to_feet.value, 0)
        center_two = XYZ(Sizes.a2_paper_width.value/2 * Sizes.cm_to_feet.value, (vf_h/2+5)*Sizes.cm_to_feet.value, 0)
        v_one = Viewport.Create(doc, sheet.Id, elevation_three['view'].Id, center_one)
        v_two = Viewport.Create(doc, sheet.Id, elevation_four['view'].Id, center_two)

        set_detail_letter(v_one)
        set_detail_letter(v_two)
        set_label_offset(v_one)
        set_label_offset(v_two)
    else:
        # TODO place side by side
        tt = (Sizes.a2_paper_height.value - 3 - vt_h/2) * Sizes.cm_to_feet.value
        center_one = XYZ(((vt_w / 2)+5) * Sizes.cm_to_feet.value, tt, 0)
        center_two = XYZ((vt_w + vf_w/2 + 10) * Sizes.cm_to_feet.value,  tt, 0)
        v_one = Viewport.Create(doc, sheet.Id, elevation_three['view'].Id, center_one)
        v_two = Viewport.Create(doc, sheet.Id, elevation_four['view'].Id, center_two)
        set_detail_letter(v_one)
        set_detail_letter(v_two)
        set_label_offset(v_one)
        set_label_offset(v_two)


def place_one_by_one_elevation(sheet, room_name, room_number, plan_view, sorted_elevations):
    elevation_one = sorted_elevations[0]
    elevation_two = sorted_elevations[1]

    all_viewports = get_viewports(sheet)
    if len(all_viewports) != 1:
        return None

    plan_viewport = all_viewports[0]
    plan_viewport_center = plan_viewport.GetBoxCenter()
    v_w, v_h = get_viewport_dimensions(plan_viewport)
    ww_one, wh_one = get_scaled_size(elevation_one['view'], 25)
    ww_two, wh_two = get_scaled_size(elevation_two['view'], 25)
    horizontal_offset = (Sizes.a2_paper_width.value - ((Sizes.a2_paper_width.value - v_w - 4)/2)) * Sizes.cm_to_feet.value

    ver_one = (Sizes.a2_paper_height.value - wh_one / 2 - 3) * Sizes.cm_to_feet.value
    vet_two = (wh_two / 2 + 5) * Sizes.cm_to_feet.value

    v_one = Viewport.Create(doc, sheet.Id, elevation_one['view'].Id, XYZ(horizontal_offset, ver_one, 0))
    v_two = Viewport.Create(doc, sheet.Id, elevation_two['view'].Id, XYZ(horizontal_offset, vet_two, 0))

    set_detail_letter(v_one)
    set_detail_letter(v_two)
    set_label_offset(v_one)
    set_label_offset(v_two)

    place_rest_on_second_sheet(room_name, room_number, sorted_elevations)


def place_rest_on_third_sheet(sheet, three_v, four_v):
    vw_three, vh_three = get_scaled_size(three_v, 25)
    vw_four, vh_four = get_scaled_size(four_v, 25)
    center_three = XYZ(Sizes.a2_paper_width.value/2 * Sizes.cm_to_feet.value, (Sizes.a2_paper_height.value-vh_four/2-3) * Sizes.cm_to_feet.value, 0)
    center_four = XYZ(Sizes.a2_paper_width.value/2 * Sizes.cm_to_feet.value, (vh_three / 2 + 6) * Sizes.cm_to_feet.value, 0)
    viewport_three = Viewport.Create(doc, sheet.Id, three_v.Id, center_three)
    viewport_four = Viewport.Create(doc, sheet.Id, four_v.Id, center_four)
    set_label_offset(viewport_three)
    set_label_offset(viewport_four)


def find_sheet_by_number(number):
    all_sheets = FilteredElementCollector(doc).OfClass(ViewSheet).ToElements()
    for sheet in all_sheets:
        print number
        print sheet.GetParameters("Sheet Number")[0].ToString()
        if sheet.GetParameters("Sheet Number")[0].AsValueString() == number:
            return sheet
        return None


def get_viewports_on_sheet(sheet):
    # Get the sheet view Id
    sheet_view_id = sheet.Id

    # Filter for viewports placed on the sheet
    collector = FilteredElementCollector(doc, sheet_view_id).OfCategory(BuiltInCategory.OST_Viewports)
    viewports = list(collector)

    return viewports


def place_fourth_on_first_sheet(name, room_number, vw_four, plan_sheet):
    # TODO get sheet for provided room number

    if plan_sheet is not None:
        all_viewports = get_viewports_on_sheet(plan_sheet)
        if len(all_viewports) == 1:
            plan_viewport = all_viewports[0]
            pv_w, pv_h = get_viewport_dimensions(plan_viewport)
            print vw_four
            el_four_w, el_four_h = get_scaled_size(vw_four, 25)

            if pv_h + el_four_h + 5 < Sizes.a2_paper_height.value:
                center = XYZ((pv_w/2 + 2.9)*Sizes.cm_to_feet.value, (Sizes.a2_paper_height.value-pv_h-el_four_h/2-6)*Sizes.cm_to_feet.value, 0)
                viewport_four = Viewport.Create(doc, plan_sheet.Id, vw_four.Id, center)
                set_detail_letter(viewport_four)
            else:
                new_sheet = create_sheet(name, room_number)
                center = XYZ((Sizes.a2_paper_width.value/2)*Sizes.cm_to_feet.value, (Sizes.a2_paper_height.value - el_four_w/2 - 4)*Sizes.cm_to_feet.value, 0)
                viewport_four = Viewport.Create(doc, new_sheet.Id, vw_four.Id, center)
                set_detail_letter(viewport_four)
                set_label_offset(viewport_four)

    # TODO check if height of plan viewport is higher than paper
    # TODO if it is higher place it on fourth sheet
    # TODO otherwise, place it on current sheet


def place_on_second_sheet(room_name, room_number, sorted_elevations, plan_sheet):
    one_v = sorted_elevations[0]['view']
    two_v = sorted_elevations[1]['view']
    three_v = sorted_elevations[2]['view']
    four_v = sorted_elevations[3]['view']

    vw_one, vh_one = get_scaled_size(one_v, 25)
    vw_two, vh_two = get_scaled_size(two_v, 25)
    vw_three, vh_three = get_scaled_size(three_v, 25)
    vw_four, vh_four = get_scaled_size(four_v, 25)

    if vw_one + vw_two + 10 > Sizes.a2_paper_width.value:
        print '-1-----'
        sheet_one = create_sheet(room_name, room_number + '-1')
        sheet_two = create_sheet(room_name, room_number + '-2')
        center_one = XYZ((Sizes.a2_paper_width.value/2)*Sizes.cm_to_feet.value, (Sizes.a2_paper_height.value-vh_one/2-3)*Sizes.cm_to_feet.value, 0)
        center_two = XYZ((Sizes.a2_paper_width.value/2)*Sizes.cm_to_feet.value, (vh_two/2+6)*Sizes.cm_to_feet.value, 0)
        viewport_one = Viewport.Create(doc, sheet_one.Id, one_v.Id, center_one)
        viewport_two = Viewport.Create(doc, sheet_one.Id, two_v.Id, center_two)
        set_detail_letter(viewport_one)
        set_detail_letter(viewport_two)
        set_label_offset(viewport_one)
        set_label_offset(viewport_two)

        place_rest_on_third_sheet(sheet_two, three_v, four_v)
    else:
        print '-2-----'
        mm = Sizes.a2_paper_width.value - (Sizes.a2_paper_width.value - vw_one - 4)/2
        center_one = XYZ((vw_one/2+6)*Sizes.cm_to_feet.value, (Sizes.a2_paper_height.value-vh_one/2-3)*Sizes.cm_to_feet.value, 0)
        center_two = XYZ(mm*Sizes.cm_to_feet.value, (Sizes.a2_paper_height.value-vh_two/2-3)*Sizes.cm_to_feet.value, 0)
        center_three = XYZ((vw_three/2 + 6)*Sizes.cm_to_feet.value, (vh_four/2+5)*Sizes.cm_to_feet.value, 0)
        center_four = XYZ((vw_three + vw_four/2 + 7)*Sizes.cm_to_feet.value, (vh_three/2+4)*Sizes.cm_to_feet.value, 0)

        sheet = create_sheet(room_name, room_number + '-1')
        viewport_one = Viewport.Create(doc, sheet.Id, one_v.Id, center_one)
        viewport_two = Viewport.Create(doc, sheet.Id, two_v.Id, center_two)
        viewport_three = Viewport.Create(doc, sheet.Id, three_v.Id, center_three)

        set_detail_letter(viewport_one)
        set_detail_letter(viewport_two)
        set_detail_letter(viewport_three)

        set_label_offset(viewport_one)
        set_label_offset(viewport_two)
        set_label_offset(viewport_three)

        if vw_three + vw_four + 5 > Sizes.a2_paper_width.value:
            print '-4'
            place_fourth_on_first_sheet(room_name, room_number+'-2', four_v, plan_sheet)
        else:
            print '-5'
            viewport_four = Viewport.Create(doc, sheet.Id, four_v.Id, center_four)
            set_detail_letter(viewport_four)
            set_label_offset(viewport_four)


def place_views(room_views, room_number):
    room = get_room(room_number)
    room_name = room.GetParameters("Name")[0].AsString()
    pl_w, pl_h = None, None
    sheet = None
    plan_view = None
    for room_view in room_views:
        if room_view[0] == 'plan':
            plan_view = room_view[1]
            pl_w, pl_h = get_scaled_size(plan_view, 25)
            # WARNING : sheet create
            sheet = create_sheet(room_name, room_number)
            place_plan_view(plan_view, sheet)

    sorted_elevations = sort_elevation_by_width(room_views)

    if plan_view is None:
        print "There is no plan view"
        return room_name

    if len(sorted_elevations) != 4:
        print "There are less than four"
        return room_name

    if sheet is None:
        print 'Sheet is none'
        return room_name

    elevation_one = sorted_elevations[0]
    elevation_two = sorted_elevations[1]
    elevation_three = sorted_elevations[2]
    elevation_four = sorted_elevations[3]

    if pl_w is not None:
        view_one_item = elevation_one.items()
        view_one = view_one_item[0][1]
        view_w_one = view_one_item[1][1]

        view_two_item = elevation_two.items()
        view_two = view_two_item[0][1]
        view_w_two = view_two_item[1][1]

        view_three_item = elevation_three.items()
        view_three = view_three_item[0][1]
        view_w_three = view_three_item[1][1]

        view_four_item = elevation_four.items()
        view_four = view_four_item[0][1]
        view_w_four = view_four_item[1][1]

        print pl_w + view_w_one + view_w_two

        if pl_w + view_w_one + view_w_two + 14 < Sizes.a2_paper_width.value:
            print '1----'
            place_two_by_two_elevations(sheet, plan_view, sorted_elevations)
        elif pl_w + view_w_one + 12 < Sizes.a2_paper_width.value:
            print '2----'
            place_one_by_one_elevation(sheet, room_name, room_number, plan_view, sorted_elevations)
        else:
            print '3----'
            place_on_second_sheet(room_name, room_number, sorted_elevations, sheet)
        # pl_w + elevation_one.items()

    return "OK"
    # if pl_h + 15 < Sizes.a2_paper_height.value:
    #     print room_name
    #     print "width: {s} / height: {p}".format(s=pl_w, p=pl_h)


def get_viewport_title_lines(view_tuple):
    all_viewport_lines = FilteredElementCollector(doc).OfClass(Viewport).ToElements()
    for m in all_viewport_lines:
        par_name = m.GetParameters("Type")[0].AsValueString()
        if par_name == 'Title w Line':
            print m
            viewport_label_family = m
            break
            new_sheet = create_sheet('0120', 'sdkfln')
            vk = doc.GetElement(ElementId(2704874))
            # view_tuple[1].items()[0][1].Id
            ka = Viewport.Create(doc, new_sheet.Id, vk.Id, XYZ(0, 0, 0))
            for type_id in ka.GetValidTypes():
                el = doc.GetElement(type_id)
                parameters = el.Parameters
                # for pk in parameters:
                #     print pk.Definition.Name
                parameter = next((p for p in parameters if p.Definition.Name == 'Type Name'), None)
                if parameter.AsValueString() == 'Title w Line':
                    viewport_label_family = el
                    print viewport_label_family
                # print dir(el)
                # print el.ParametersMap.Item
                # print '------'
                # print el.GetParameters("Family")
                # print el.GetType()
                # print dir(el)
                # print el.GetParameters("Family and Type")[0]
            # ka.ChangeTypeId()
            break

        # if par_name is not None and len(par_name) == 1:
        #     print par_name[0].AsValueString()
        # parameters = m.Parameters
        # parameter = next((p for p in parameters if p.Definition.Name == 'Family and Type'), None)
        # # print parameter
        # if parameter is not None:
        #     type_name = parameter.AsValueString()
        #     # type_name = parameter.AsValueString()
        #     # print type_name


def main():
    f = pyrevit.forms.alert(title="Warning", msg='Do you want to proceed')
    if not f:
        return
    t = Transaction(doc, "Test")
    t.Start()
    i = 1
    try:
        views = sort_views()
        for view_tuple in views.items():
            # WARNING this should be deleted later
            # if i == 20:
            #     break
            room_number = view_tuple[0]
            # if room_number.strip() != '010':
            #     continue

            # # TODO : delete this line
            # if len(view_tuple[1].items()) < 3:
            #     continue

            st = SubTransaction(doc)
            st.Start()
            try:
                if room_number.isnumeric():
                    room_views_dict = view_tuple[1]
                    room_views = room_views_dict.items()
                    print '10101'
                    v_info = place_views(room_views, room_number)
                    print v_info
                    print '10101'

                    # print v_info
                st.Commit()
            except Exception as e:
                print e
                st.RollBack()

            i += 1

    except Exception as e:
        print (e)

    t.Commit()


if __name__ == "__main__":
    main()

# print room_view
# if room_view[0] == 'plan':
#     create_plan_sheet(room_view, room_number)
# else:
#     create_elevation_sheet(room_views, room_number)

# if multiple_sheets(view_tuple):
#     pass
# else:
#     pass
#     # TODO this can be an issue
