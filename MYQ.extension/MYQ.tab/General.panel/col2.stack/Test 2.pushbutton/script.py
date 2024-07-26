from Autodesk.Revit.DB import *
from pprint import PrettyPrinter

__title__ = "Col 2 - BTN 2"
__author__ = "Me"
__doc__ = "Button"

pp = PrettyPrinter(indent=2)

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document


t = Transaction(doc, "Test")
t.Start()

try:
    print ("-" * 20)
    view_templates_list = FilteredElementCollector(doc).OfClass(View).ToElements()
    list_of_view_template_ids = list()

    for k in view_templates_list:
        if k.IsTemplate:
            # print k.Name
            if not k.Name.startswith("ALEA_") and not k.Name.startswith("A+"):
                print k.Name
                # new_name = "A+_AD_" + k.Name[8:]
                # print new_name
                # k.Name = new_name
                # doc.Delete(k.Id)
        # if k.ViewTemplateId != -1:
        #     if k.ViewTemplateId in list_of_view_template_ids:
        #         pass
        #     else:
        #         list_of_view_template_ids.append(k.ViewTemplateId)
        #     viewTemplates = [v for v in view_templates_list if v.IsTemplate]
        #     tem_to_delete = list()

    # for pp in tem_to_delete:
    #     print pp.Name
    # for tmp in viewTemplates:
    #     if not tmp.Name.startswith("A+"):
    #         tem_to_delete.append(tmp)
    #         for tmp_id in tem_to_delete:
    #     print (tmp_id.Name)
    #     doc.Delete(tmp_id.Id)

    # print (len(list_of_view_template_ids))
    title_block = None

    # for q in title_blocks:
    #     if q.FamilyName == "ALEA+ - A0 NEW":
    #         title_block = q

    # for v in view_templates_list:
    #     print v.Name
    #     # print v.ViewTemplateId
    #     # print dir(v)
    #     # break
    #     # print (v.ViewTemplateId)
    #     if v.ViewTemplateId != -1:
    #         if v.ViewTemplateId in list_of_view_template_ids:
    #             pass
    #         else:
    #             list_of_view_template_ids.append(v.ViewTemplateId)

    for p in list_of_view_template_ids:
        print p
except Exception as e:
    print (e)

t.Commit()
