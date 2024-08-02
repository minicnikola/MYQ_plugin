import os

from Autodesk.Revit.DB import *
from pprint import PrettyPrinter

__title__ = "Place joinery images"
__author__ = "Me"
__doc__ = "Button"

from Snippets._select import get_floor_plan_views, get_sheets_by_series, get_all_images, get_image_by_name, \
    get_image_count

pp = PrettyPrinter(indent=2)

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document
ac_view = doc.ActiveView


def load_image(image_path):
    img_opt = ImageTypeOptions(image_path, False, ImageTypeSource.Import)
    img = ImageType.Create(doc, img_opt)
    return img


def place_image_on_sheet(doc, sheet_id, image_id, location):
    print sheet_id
    print image_id
    img_instance = ImageInstance.Create(doc, sheet_id, image_id.Id, ImagePlacementOptions(location, BoxPlacement.Center))
    return img_instance


def main():
    t = Transaction(doc, "Test")
    t.Start()

    try:
        series = "ID4000 - JOINERY"
        sheets = get_sheets_by_series(series)
        # all_images = get_all_images()
        return
        folder_path = "Z:/2023_PROJEKTI/5079_La Mer-A05_Revit model/LA MER A05 - ID DD DATE BASE/IMAGES FOR 3000/FINAL/"

        for i, sheet in enumerate(sheets):
            sheet_number_param = sheet.GetParameters("Sheet Number")

            if len(sheet_number_param) == 0:
                continue

            sheet_number = sheet_number_param[0].AsString()
            room_number_extracted = sheet_number.split('-')[-1].split('.')[0].replace('4', '')
            print room_number_extracted

            for img_file in os.listdir(folder_path):
                room_number_from_image = img_file.split(' - ')[0]
                img_path = os.path.join(folder_path, img_file)
                # img_count = get_image_count('103 - 1.jpg')
                # print img_count
                # break
                # print '-' * 20
                # print room_number_extracted
                # print room_number_from_image
                # print '-' * 20

                if room_number_from_image != room_number_extracted:
                    continue

                if get_image_by_name(img_file) is not None:
                    img_instance = get_image_by_name(img_file)
                else:
                    img_instance = load_image(img_path)

                location = XYZ(0, 0, 0)  # Coordinates where you want to place the image
                viewport = place_image_on_sheet(doc, sheet, img_instance, location)

                if viewport:
                    print("Image placed on sheet successfully. Viewport ID: {viewport}"
                          .format(viewport=sheet.GetParameters("Sheet Name")[0].AsString()))
                else:
                    print("Failed to place the image on the sheet.")

                break

            if i == 20:
                break
    except Exception as e:
        print (e)

    t.Commit()


if __name__ == "__main__":
    main()
