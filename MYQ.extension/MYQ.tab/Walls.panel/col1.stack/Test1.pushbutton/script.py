from Autodesk.Revit.DB import *
from pprint import PrettyPrinter
from pyrevit import forms
import pyrevit

__title__ = "Change allow join"
__author__ = "Me"
__doc__ = "--------"

from Snippets._selection import pick_wall

pp = PrettyPrinter(indent=2)

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document


def main():
    # f = pyrevit.forms.alert(title="Warning", msg='Do you want to proceed')
    # if not f:
    #     return

    t = Transaction(doc, "Test")
    t.Start()
    try:

        # >>>>>>>>>> SELECT MAIN WALL
        try:
            print '--1-1-'
            selected_walls = pick_wall(uidoc)
            for wall in selected_walls:
                print wall
                # wall_curve = wall.Location.Curve
                # print wall_curve
            t.Commit()
        except Exception as e:
            forms.alert("Script is canceled.", exitscript=True, title="Script Canceled.")
            t.Commit()
        t.Commit()
    except Exception as e:
        print (e)
        t.Commit()

    t.Commit()


if __name__ == "__main__":
    main()
