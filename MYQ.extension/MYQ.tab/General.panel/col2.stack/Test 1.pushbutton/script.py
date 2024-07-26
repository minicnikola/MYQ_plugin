from Autodesk.Revit.DB import *
from pprint import PrettyPrinter

__title__ = "Workset creation"
__author__ = "Me"
__doc__ = "Button"

pp = PrettyPrinter(indent=2)

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

t = Transaction(doc, "Test")
t.Start()

names = ['WINDOWS', 'DOORS', 'WALLS', 'ST_SLAB', 'ST_COLUMNS', "ST_BEAMS", 'FLOOR_FINISH', 'WALL FINISH',
         'SANITARY', 'CEILING']
interior_list = ['FURNITURE', 'SANITARY', 'CASEWORK', 'LIGHTNING',
                 'CEILING', 'POWER', 'RAILING', 'DOORS_AND_PARTITIONS']
CAD_worksets = ['DWG']
levels = ['BF', 'GF', 'FF', 'RF']


try:

    for n in CAD_worksets:
        for level in levels:
            name = "A" + '-' + level + "_" + n
            print name
            ws = Workset.Create(doc, name)
        #     break
        # break
except Exception as e:
    print (e)

t.Commit()
