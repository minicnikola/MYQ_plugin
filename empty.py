

# filtered_sheets = list()
#
#     for sheet in all_sheets:
#         if str(sheet.SheetNumber).startswith("ID - 1"):
#             filtered_sheets.append(sheet)
#
#     viewports = (FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_ViewportLabel)
#                  .WhereElementIsElementType().ToElements())
#
#     for m in filtered_sheets:
#         k = m.GetAllViewports()
#         for i in k:
#             viewport = doc.GetElement(i)
#             viewport.GetParameters("Crop Region Visible")[0].Set(False)
#
#             viewport_types = viewport.GetValidTypes()
#             print (len(viewport_types))
#             for aa in viewport_types:
#                 element = doc.GetElement(aa)
#                 element_type = element.GetType()
#                 print (type(element_type))
#                 print (dir(element_type))
#                 # print (dir(element_type))
#                 # print (dir(element))
#                 # print (element.Name)
#                 break
#             break
#         break


# ['Activate', 'ArePhasesModifiable', 'AssemblyInstanceId', 'BoundingBox', 'CanBeCopied', 'CanBeDeleted',
# 'CanBeHidden', 'CanBeLocked', 'CanBeRenamed', 'CanDeleteSubelement', 'CanHaveStructuralSection',
# 'CanHaveTypeAssigned', 'Category', 'ChangeTypeId', 'CreatedPhaseId', 'DeleteEntity', 'DeleteSubelement',
# 'DeleteSubelements', 'DemolishedPhaseId', 'DesignOption', 'Dispose', 'Document', 'Duplicate', 'Equals',
# 'EvaluateAllParameterValues', 'EvaluateParameterValues', 'Family', 'FamilyName', 'Geometry', 'GetChangeTypeAny',
# 'GetChangeTypeElementAddition', 'GetChangeTypeElementDeletion', 'GetChangeTypeGeometry', 'GetChangeTypeParameter',
# 'GetDependentElements', 'GetEntity', 'GetEntitySchemaGuids', 'GetExternalFileReference',
# 'GetExternalResourceReference', 'GetExternalResourceReferenceExpanded', 'GetExternalResourceReferences',
# 'GetExternalResourceReferencesExpanded', 'GetFamilyPointLocations', 'GetGeneratingElementIds',
# 'GetGeometryObjectFromReference', 'GetHashCode', 'GetMaterialArea', 'GetMaterialIds', 'GetMaterialVolume',
# 'GetMonitoredLinkElementIds', 'GetMonitoredLocalElementIds', 'GetOrderedParameters', 'GetParameter',
# 'GetParameterFormatOptions', 'GetParameters', 'GetPhaseStatus', 'GetPreviewImage', 'GetSimilarTypes',
# 'GetStructuralSection', 'GetSubelements', 'GetThermalProperties', 'GetType', 'GetTypeId', 'GetValidTypes',
# 'GroupId', 'HasPhases', 'HasThermalProperties', 'Id', 'IsActive', 'IsCreatedPhaseOrderValid',
# 'IsDemolishedPhaseOrderValid', 'IsExternalFileReference', 'IsHidden', 'IsModifiable', 'IsMonitoringLinkElement',
# 'IsMonitoringLocalElement', 'IsPhaseCreatedValid', 'IsPhaseDemolishedValid', 'IsSimilarType', 'IsTransient',
# 'IsValidDefaultFamilyType', 'IsValidObject', 'IsValidType', 'LevelId', 'Location', 'LookupParameter',
# 'MemberwiseClone', 'Name', 'OwnerViewId', 'Parameter', 'Parameters', 'ParametersMap', 'Pinned', 'ReferenceEquals',
# 'RefersToExternalResourceReference', 'RefersToExternalResourceReferences', 'ReleaseUnmanagedResources',
# 'SetEntity', 'SetStructuralSection', 'SetThermalProperties', 'StructuralMaterialType', 'ToString', 'UniqueId',
# 'VersionGuid', 'ViewSpecific', 'WorksetId', '__class__', '__delattr__', '__doc__', '__enter__', '__exit__',
# '__format__', '__getattribute__', '__hash__', '__init__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
# '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'getBoundingBox', 'setElementType']


# ['AsType', 'Assembly', 'AssemblyQualifiedName', 'Attributes', 'BaseType', 'Clone', 'ContainsGenericParameters',
# 'CustomAttributes', 'DeclaredConstructors', 'DeclaredEvents', 'DeclaredFields', 'DeclaredMembers',
# 'DeclaredMethods', 'DeclaredNestedTypes', 'DeclaredProperties', 'DeclaringMethod', 'DeclaringType',
# 'DefaultBinder', 'Delimiter', 'EmptyTypes', 'Equals', 'FilterAttribute', 'FilterName', 'FilterNameIgnoreCase',
# 'FindInterfaces', 'FindMembers', 'FullName', 'GUID', 'GenericParameterAttributes', 'GenericParameterPosition',
# 'GenericTypeArguments', 'GenericTypeParameters', 'GetArrayRank', 'GetAttributeFlagsImpl', 'GetConstructor',
# 'GetConstructorImpl', 'GetConstructors', 'GetCustomAttributes', 'GetCustomAttributesData', 'GetDeclaredEvent',
# 'GetDeclaredField', 'GetDeclaredMethod', 'GetDeclaredMethods', 'GetDeclaredNestedType', 'GetDeclaredProperty',
# 'GetDefaultMembers', 'GetElementType', 'GetEnumName', 'GetEnumNames', 'GetEnumUnderlyingType', 'GetEnumValues',
# 'GetEvent', 'GetEvents', 'GetField', 'GetFields', 'GetGenericArguments', 'GetGenericParameterConstraints',
# 'GetGenericTypeDefinition', 'GetHashCode', 'GetIDsOfNames', 'GetInterface', 'GetInterfaceMap', 'GetInterfaces',
# 'GetMember', 'GetMembers', 'GetMethod', 'GetMethodImpl', 'GetMethods', 'GetNestedType', 'GetNestedTypes',
# 'GetObjectData', 'GetProperties', 'GetProperty', 'GetPropertyImpl', 'GetType', 'GetTypeArray', 'GetTypeCode',
# 'GetTypeCodeImpl', 'GetTypeFromCLSID', 'GetTypeFromHandle', 'GetTypeFromProgID', 'GetTypeHandle', 'GetTypeInfo',
# 'GetTypeInfoCount', 'HasElementType', 'HasElementTypeImpl', 'ImplementedInterfaces', 'Invoke', 'InvokeMember',
# 'IsAbstract', 'IsAnsiClass', 'IsArray', 'IsArrayImpl', 'IsAssignableFrom', 'IsAutoClass', 'IsAutoLayout',
# 'IsByRef', 'IsByRefImpl', 'IsCOMObject', 'IsCOMObjectImpl', 'IsClass', 'IsConstructedGenericType', 'IsContextful',
# 'IsContextfulImpl', 'IsDefined', 'IsEnum', 'IsEnumDefined', 'IsEquivalentTo', 'IsExplicitLayout',
# 'IsGenericParameter', 'IsGenericType', 'IsGenericTypeDefinition', 'IsImport', 'IsInstanceOfType', 'IsInterface',
# 'IsLayoutSequential', 'IsMarshalByRef', 'IsMarshalByRefImpl', 'IsNested', 'IsNestedAssembly',
# 'IsNestedFamANDAssem', 'IsNestedFamORAssem', 'IsNestedFamily', 'IsNestedPrivate', 'IsNestedPublic', 'IsNotPublic',
# 'IsPointer', 'IsPointerImpl', 'IsPrimitive', 'IsPrimitiveImpl', 'IsPublic', 'IsSealed', 'IsSecurityCritical',
# 'IsSecuritySafeCritical', 'IsSecurityTransparent', 'IsSerializable', 'IsSpecialName', 'IsSubclassOf',
# 'IsUnicodeClass', 'IsValueType', 'IsValueTypeImpl', 'IsVisible', 'MakeArrayType', 'MakeByRefType',
# 'MakeGenericType', 'MakePointerType', 'MemberType', 'MemberwiseClone', 'MetadataToken', 'Missing', 'Module',
# 'Name', 'Namespace', 'ReferenceEquals', 'ReflectedType', 'ReflectionOnlyGetType', 'StructLayoutAttribute',
# 'ToString', 'TypeHandle', 'TypeInitializer', 'UnderlyingSystemType', '__class__', '__delattr__', '__doc__',
# '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__ne__', '__new__', '__reduce__',
# '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']









# ---------------------------------------------------------------------------------------------------------
# # all_views = FilteredElementCollector(doc).OfClass(View).WhereElementIsNotElementType().ToElements()
# # all_sheets = FilteredElementCollector(doc).OfClass(ViewSheet).WhereElementIsNotElementType().ToElements()
#
# rooms = (FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rooms)
#              .WhereElementIsNotElementType().ToElements())
#     all_views = FilteredElementCollector(doc).OfClass(View).WhereElementIsNotElementType().ToElements()
#     title_blocks = (FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_TitleBlocks)
#                   .WhereElementIsElementType().ToElements())
#
#     view_templates_list = FilteredElementCollector(doc).OfClass(View).ToElements()
#
#     list_of_view_template_ids = list()
#     for k in view_templates_list:
#         if k.ViewTemplateId != -1:
#             if k.ViewTemplateId in list_of_view_template_ids:
#                 pass
#             else:
#                 list_of_view_template_ids.append(k.ViewTemplateId)
#
#     viewTemplates = [v for v in view_templates_list if v.IsTemplate]
#
#     # print (len(list_of_view_template_ids))
#     title_block = None
#
#     for q in title_blocks:
#         if q.FamilyName == "ALEA+ - A2 NEW":
#             title_block = q
#
#     filtered_views = list()
#     for view in all_views:
#         if view.Name.startswith("EL-"):
#             filtered_views.append(view)
#
#     for room in rooms:
#         area = UnitUtils.ConvertFromInternalUnits(room.Area, UnitTypeId.SquareMeters)
#
#         if title_block is not None:
#             sheet = ViewSheet.Create(doc, title_block.Id)
#             sheet.SheetNumber = "ID - 3" + str(room.Number)
#             sheet.GetParameters("Sheet Group")[0].Set("Interior")
#             sheet.GetParameters("Sheet Sort")[0].Set('3' + str(room.Number)[0] + "00")
#             sheet.GetParameters("Sheet series")[0].Set("ID3000 - ELEVATIONS")
#
#             for view in filtered_views:
#                 can_be_added = Viewport.CanAddViewToSheet(doc, sheet.Id, view.Id)
#
#                 view_crop_box = view.CropBox
#                 min_x_o = view_crop_box.Min.X
#                 min_y_o = view_crop_box.Min.Y
#                 max_x_o = view_crop_box.Max.X
#                 max_y_o = view_crop_box.Max.Y
#
#                 unit = UnitTypeId.Centimeters
#                 min_x = UnitUtils.ConvertFromInternalUnits(min_x_o, unit)
#                 min_y = UnitUtils.ConvertFromInternalUnits(min_y_o, unit)
#                 max_x = UnitUtils.ConvertFromInternalUnits(max_x_o, unit)
#                 max_y = UnitUtils.ConvertFromInternalUnits(max_y_o, unit)
#
#                 # view size in cm
#                 viewport_width = max_x - min_x
#                 viewport_height = max_y - min_y
#
#                 # viewport_width = max_x_o - min_x_o
#                 # viewport_height = max_y_o - min_y_o
#
#                 # print (viewport_width, viewport_height)
#                 area = viewport_width * viewport_height
#                 print ("View name : {}".format(view.Name))
#                 print ("Area : {}".format(area))
#                 print ("viewport_width : {}".format(viewport_width))
#                 print ("viewport_height : {}".format(viewport_height))
#                 area_converted = UnitUtils.ConvertFromInternalUnits(area, UnitTypeId.SquareMeters)
#                 # print (area_converted)
#
#                 if can_be_added:
#                     point = XYZ(1, 1, 0)
#                     # viewport = Viewport.Create(doc, sheet.Id, view.Id, point)
#
#                     unit_x = UnitUtils.ConvertToInternalUnits(10, UnitTypeId.Centimeters)
#                     # viewport.SetBoxCenter(XYZ(unit_x, unit_x, unit_x))
#                     # bounding_box = viewport.get_BoundingBox(sheet)
#
#                 else:
#                     print ("Error occurred while placing view on sheet number {}.".format(sheet.SheetNumber))
#
# ---------------------------------------------------------------------------------------------------------



# ['AddFilter', 'AllowsAnalysisDisplay', 'AnalysisDisplayStyleId', 'ApplyViewTemplateParameters',
# 'AreAnalyticalModelCategoriesHidden', 'AreAnnotationCategoriesHidden', 'AreCoordinationModelHandlesHidden',
# 'AreGraphicsOverridesAllowed', 'AreImportCategoriesHidden', 'AreModelCategoriesHidden', 'ArePhasesModifiable',
# 'ArePointCloudsHidden', 'AssemblyInstanceId', 'AssociatedAssemblyInstanceId', 'BoundingBox',
# 'CanApplyColorFillScheme', 'CanBeHidden', 'CanBeLocked', 'CanBePrinted', 'CanCategoryBeHidden',
# 'CanCategoryBeHiddenTemporary', 'CanDeleteSubelement', 'CanEnableTemporaryViewPropertiesMode',
# 'CanHaveTypeAssigned', 'CanModifyDetailLevel', 'CanModifyDisplayStyle', 'CanModifyViewDiscipline',
# 'CanUseDepthCueing', 'CanUseTemporaryVisibilityModes', 'CanViewBeDuplicated', 'Category', 'ChangeTypeId',
# 'ConvertTemporaryHideIsolateToPermanent', 'ConvertToIndependent', 'CreateCallout', 'CreateDetail',
# 'CreateReferenceCallout', 'CreateReferenceSection', 'CreateSection', 'CreateViewTemplate', 'CreatedPhaseId',
# 'CropBox', 'CropBoxActive', 'CropBoxVisible', 'DeleteEntity', 'DeleteSubelement', 'DeleteSubelements',
# 'DemolishedPhaseId', 'DesignOption', 'DetailLevel', 'DisableTemporaryViewMode', 'Discipline', 'DisplayStyle',
# 'Dispose', 'Document', 'Duplicate', 'EnableRevealHiddenMode', 'EnableTemporaryViewPropertiesMode', 'Equals',
# 'EvaluateAllParameterValues', 'EvaluateParameterValues', 'GenLevel', 'Geometry', 'GetBackground',
# 'GetCalloutParentId', 'GetCategoryHidden', 'GetCategoryOverrides', 'GetChangeTypeAny',
# 'GetChangeTypeElementAddition', 'GetChangeTypeElementDeletion', 'GetChangeTypeGeometry', 'GetChangeTypeParameter',
# 'GetColorFillSchemeId', 'GetCropRegionShapeManager', 'GetCropRegionShapeManagerForReferenceCallout',
# 'GetDependentElements', 'GetDependentViewIds', 'GetDepthCueing', 'GetDirectContext3DHandleOverrides',
# 'GetElementOverrides', 'GetEntity', 'GetEntitySchemaGuids', 'GetExternalFileReference',
# 'GetExternalResourceReference', 'GetExternalResourceReferenceExpanded', 'GetExternalResourceReferences',
# 'GetExternalResourceReferencesExpanded', 'GetFilterOverrides', 'GetFilterVisibility', 'GetFilters',
# 'GetGeneratingElementIds', 'GetGeometryObjectFromReference', 'GetHashCode', 'GetIsFilterEnabled',
# 'GetLinkOverrides', 'GetMaterialArea', 'GetMaterialIds', 'GetMaterialVolume', 'GetModelToProjectionTransforms',
# 'GetMonitoredLinkElementIds', 'GetMonitoredLocalElementIds', 'GetNonControlledTemplateParameterIds',
# 'GetOrderedFilters', 'GetOrderedParameters', 'GetParameter', 'GetParameterFormatOptions', 'GetParameters',
# 'GetPhaseStatus', 'GetPlacementOnSheetStatus', 'GetPointCloudOverrides', 'GetPrimaryViewId',
# 'GetReferenceCallouts', 'GetReferenceElevations', 'GetReferenceSections', 'GetSketchyLines', 'GetSubelements',
# 'GetTemplateParameterIds', 'GetTemporaryViewPropertiesId', 'GetTemporaryViewPropertiesName', 'GetType',
# 'GetTypeId', 'GetValidTypes', 'GetViewDisplayModel', 'GetWorksetVisibility', 'GetWorksharingDisplayMode',
# 'GroupId', 'HasDetailLevel', 'HasDisplayStyle', 'HasPhases', 'HasViewDiscipline', 'HasViewTransforms',
# 'HideActiveWorkPlane', 'HideCategoriesTemporary', 'HideCategoryTemporary', 'HideElementTemporary', 'HideElements',
# 'HideElementsTemporary', 'Id', 'IsAssemblyView', 'IsCallout', 'IsCategoryOverridable', 'IsCreatedPhaseOrderValid',
# 'IsDemolishedPhaseOrderValid', 'IsElementVisibleInTemporaryViewMode', 'IsExternalFileReference', 'IsFilterApplied',
# 'IsHidden', 'IsInTemporaryViewMode', 'IsModifiable', 'IsMonitoringLinkElement', 'IsMonitoringLocalElement',
# 'IsParentViewValidForCallout', 'IsPhaseCreatedValid', 'IsPhaseDemolishedValid', 'IsSplitSection', 'IsTemplate',
# 'IsTemporaryHideIsolateActive', 'IsTemporaryViewPropertiesModeEnabled', 'IsTransient', 'IsValidObject',
# 'IsValidType', 'IsValidViewScale', 'IsValidViewTemplate', 'IsViewFamilyTypeValidForCallout',
# 'IsViewValidForTemplateCreation', 'IsWorksetVisible', 'IsolateCategoriesTemporary', 'IsolateCategoryTemporary',
# 'IsolateElementTemporary', 'IsolateElementsTemporary', 'LevelId', 'Location', 'LookupParameter', 'MemberwiseClone',
# 'Name', 'Origin', 'Outline', 'OwnerViewId', 'Parameter', 'Parameters', 'ParametersMap', 'PartsVisibility',
# 'Pinned', 'Print', 'ReferenceEquals', 'RefersToExternalResourceReference', 'RefersToExternalResourceReferences',
# 'ReleaseUnmanagedResources', 'RemoveCalloutParent', 'RemoveFilter', 'RemoveLinkOverrides', 'RestoreCalloutParent',
# 'RevealConstraintsMode', 'RightDirection', 'Scale', 'SetBackground', 'SetCategoryHidden', 'SetCategoryOverrides',
# 'SetColorFillSchemeId', 'SetDepthCueing', 'SetElementOverrides', 'SetEntity', 'SetFilterOverrides',
# 'SetFilterVisibility', 'SetIsFilterEnabled', 'SetLinkOverrides', 'SetNonControlledTemplateParameterIds',
# 'SetSketchyLines', 'SetViewDisplayModel', 'SetWorksetVisibility', 'SetWorksharingDisplayMode', 'ShadowIntensity',
# 'ShowActiveWorkPlane', 'SketchPlane', 'SunAndShadowSettings', 'SunlightIntensity', 'SupportedColorFillCategoryIds',
# 'SupportsRevealConstraints', 'SupportsWorksharingDisplayMode', 'TemporaryViewModes', 'Title', 'ToString',
# 'UnhideElements', 'UniqueId', 'UpDirection', 'VersionGuid', 'ViewDirection', 'ViewSpecific', 'ViewTemplateId',
# 'ViewType', 'WorksetId', '__class__', '__delattr__', '__doc__', '__enter__', '__exit__', '__format__',
# '__getattribute__', '__hash__', '__init__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
# '__sizeof__', '__str__', '__subclasshook__', 'getBoundingBox', 'setElementType']


# ---------------------------------------------------------------------------------------------------------


print ('---------------- Script --------------')
    # try:
    #     transaction = Transaction(doc, "Test")
    #     transaction.Start()
    #
    #     view_type_list = ['FLOOR FINISHES', 'FURNITURE PLAN', 'GENERAL LAYOUT',
    #                       'LIGHT LOOPING PLAN', 'POWER PLAN', 'SANITARY PLAN',
    #                       'WALL FINISHES']
    #
    #     all_views = FilteredElementCollector(doc).OfClass(View).WhereElementIsNotElementType().ToElements()
    #     all_sheets = FilteredElementCollector(doc).OfClass(ViewSheet).WhereElementIsNotElementType().ToElements()
    #     all_levels = FilteredElementCollector(doc).OfClass(Level).WhereElementIsNotElementType().ToElements()
    #     view_types_collection = FilteredElementCollector(doc).OfClass(ViewPlan).ToElements()
    #     # kk = FilteredElementCollector(doc).OfClass(ViewFamily).ToElements()
    #     mmm = FilteredElementCollector(doc).OfClass(ViewFamilyType).WhereElementIsElementType().ToElements()
    #
    #     rooms = (FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rooms)
    #              .WhereElementIsNotElementType().ToElements())
    #     title_blocks = (FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_TitleBlocks)
    #                     .WhereElementIsElementType().ToElements())
    #
    #     crop_box = doc.GetElement(ElementId(1188210))
    #     view_templates_list = FilteredElementCollector(doc).OfClass(View).ToElements()
    #
    #     filtered_levels = list()
    #     view_templates = list()
    #     views = list()
    #
    #     for t in view_types_collection:
    #         # print (t.Name)
    #         if t.ViewType == ViewType.FloorPlan:
    #             if t.IsTemplate:
    #                 view_templates.append(t)
    #             else:
    #                 views.append(t)
    #
    #     furniture_plan_template = None
    #     floor_plan_template = None
    #     general_plan_template = None
    #     looping_plan_template = None
    #     power_plan_template = None
    #     sanitary_plan_template = None
    #     wall_plan_template = None
    #
    #     for k in view_templates:
    #         if k.Name == "A+_ID_FURNITURE PLAN_1-50":
    #             furniture_plan_template = k
    #         elif k.Name == "A+_ID_GENERAL LAYOUT_1-50":
    #             general_plan_template = k
    #             looping_plan_template = k
    #         elif k.Name == "A+_ID_FLOOR FINISHES_1-50":
    #             floor_plan_template = k
    #         elif k.Name == "A+_ID_POWER PLAN_1-50":
    #             power_plan_template = k
    #         elif k.Name == "A+_ID_SANITARY PLAN_1-50":
    #             sanitary_plan_template = k
    #         elif k.Name == "A+_ID_WALL FINISHES_1-50":
    #             wall_plan_template = k
    #
    #     # transaction.Commit()
    #     # return
    #
    #     for level in all_levels:
    #         if level.Name.find("F.F.L") != -1 and level.Name.find("TOR") == -1:
    #             filtered_levels.append(level)
    #
    #     sorted_list = sorted(filtered_levels, key=lambda x: x.Elevation)
    #     view_type_id = None
    #
    #     for k in mmm:
    #         if k.FamilyName == "Floor Plan":
    #             par_name = k.GetParameters("Type Name")[0].AsString()
    #             if par_name == 'Architecture':
    #                 view_type_id = k.Id
    #
    #     # for level in filtered_levels:
    #     #     for view_t in view_type_list:
    #     #         pass
    #     #         view = ViewPlan.Create(doc, view_type_id, level.Id)
    #     #         view_name = level.Name.split(" ")[0] + " - " + view_t + ' - Test'
    #     #         view.Name = view_name
    #     #         view.ViewTemplateId = 1
    #
    #     # -------------------------------------------------------------------------------------------
    #     legend_view = None
    #     for ll_m in all_views:
    #         if ll_m.Name == 'WALL LEGEND':
    #             legend_view = ll_m
    #
    #
    #     # list_of_view_template_ids = list()
    #     # for k in view_templates_list:
    #     #     if k.ViewTemplateId != -1:
    #     #         if k.ViewTemplateId in list_of_view_template_ids:
    #     #             pass
    #     #         else:
    #     #             list_of_view_template_ids.append(k.ViewTemplateId)
    #     #
    #     # viewTemplates = [v for v in view_templates_list if v.IsTemplate]
    #     #
    #     tem_to_delete = list()
    #
    #     # for tmp in viewTemplates:
    #     #     if not tmp.Name.startswith("A+"):
    #     #         tem_to_delete.append(tmp)
    #     #
    #     # for tmp_id in tem_to_delete:
    #     #     print (tmp_id.Name)
    #     #     # doc.Delete(tmp_id.Id)
    #
    #     # print (len(list_of_view_template_ids))
    #     title_block = None
    #
    #     for q in title_blocks:
    #         if q.FamilyName == "ALEA+ - A0 NEW":
    #             title_block = q
    #
    #     print (title_block)
    #     filtered_views = list()
    #     # for view in all_views:
    #     #     if view.Name.startswith("EL-"):
    #     #         filtered_views.append(view)
    #     scope_box_filter = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_VolumeOfInterest).ToElements()
    #     # scope_boxes = [elem for elem in scope_box_filter if elem.get_Parameter(BuiltInParameter.VIEWER_SCOPE_BOX_NAME)]
    #     scope_box_main = None
    #
    #     for scope_box in scope_box_filter:
    #         print(scope_box.Name)
    #         if scope_box.Name == "MAIN BOX":
    #             scope_box_main = scope_box
    #
    #     # transaction.Commit()
    #     # return
    #
    #     for level_id, level in enumerate(sorted_list):
    #         print ("level id : {}".format(level_id))
    #         index = 0
    #         for view_id in view_type_list:
    #             index = index + 1
    #             # print ("index id : {}".format(index))
    #             view = ViewPlan.Create(doc, view_type_id, level.Id)
    #             view_name = (level.Name.split(" ")[0] + " - " + "1"
    #                          + str(level_id) + "0" + str(index) + " - " + view_id)
    #             # print (view_name)
    #             view.Name = view_name
    #             view.CropBoxActive = True
    #             view.CropBoxVisible = False
    #             view.CropBox = scope_box_main.get_BoundingBox(None)
    #
    #             if view_id.find("FURNITURE") != -1:
    #                 view.ViewTemplateId = furniture_plan_template.Id
    #             elif view_id.find("GENERAL") != -1:
    #                 view.ViewTemplateId = general_plan_template.Id
    #             elif view_id.find("FLOOR") != -1:
    #                 view.ViewTemplateId = floor_plan_template.Id
    #             elif view_id.find("LIGHT") != -1:
    #                 view.ViewTemplateId = looping_plan_template.Id
    #             elif view_id.find("POWER") != -1:
    #                 view.ViewTemplateId = power_plan_template.Id
    #             elif view_id.find("SANITARY") != -1:
    #                 view.ViewTemplateId = sanitary_plan_template.Id
    #             elif view_id.find("WALL") != -1:
    #                 view.ViewTemplateId = wall_plan_template.Id
    #
    #             print (view.Name)
    #             # view.ViewTemplateId = 1
    #
    #             if title_block is not None:
    #                 sheet = ViewSheet.Create(doc, title_block.Id)
    #                 sheet.SheetNumber = "ID - 1" + str(level_id) + "0" + str(index)
    #                 sheet.GetParameters("Sheet Name")[0].Set(level.Name.split(" ")[0] + " - " + view_id)
    #                 sheet.GetParameters("Sheet Group")[0].Set("Interior")
    #                 sheet.GetParameters("Sheet Sort")[0].Set('1' + str(level_id) + "00")
    #                 sheet.GetParameters("Sheet series")[0].Set("ID1000 - PLANS")
    #
    #                 if view.Name.find("GENERAL") != -1:
    #                     legend_viewport = Viewport.Create(doc, sheet.Id, legend_view.Id, XYZ(1.3, 1.55, 0))
    #
    #                 # for view in filtered_views:
    #                 #     can_be_added = Viewport.CanAddViewToSheet(doc, sheet.Id, view.Id)
    #
    #                 can_be_added = Viewport.CanAddViewToSheet(doc, sheet.Id, view.Id)
    #                 view_crop_box = view.CropBox
    #                 min_x_o = view_crop_box.Min.X
    #                 min_y_o = view_crop_box.Min.Y
    #                 max_x_o = view_crop_box.Max.X
    #                 max_y_o = view_crop_box.Max.Y
    #
    #                 unit = UnitTypeId.Centimeters
    #                 min_x = UnitUtils.ConvertFromInternalUnits(min_x_o, unit)
    #                 min_y = UnitUtils.ConvertFromInternalUnits(min_y_o, unit)
    #                 max_x = UnitUtils.ConvertFromInternalUnits(max_x_o, unit)
    #                 max_y = UnitUtils.ConvertFromInternalUnits(max_y_o, unit)
    #
    #                 # view size in cm
    #                 viewport_width = max_x - min_x
    #                 viewport_height = max_y - min_y
    #
    #                 # viewport_width = max_x_o - min_x_o
    #                 # viewport_height = max_y_o - min_y_o
    #
    #                 # print (viewport_width, viewport_height)
    #                 area = viewport_width * viewport_height
    #                 # print ("View name : {}".format(view.Name))
    #                 # print ("Area : {}".format(area))
    #                 # print ("viewport_width : {}".format(viewport_width))
    #                 # print ("viewport_height : {}".format(viewport_height))
    #                 area_converted = UnitUtils.ConvertFromInternalUnits(area, UnitTypeId.SquareMeters)
    #                 # print (area_converted)
    #
    #                 if can_be_added:
    #                     point = XYZ(0, 0, 0)
    #                     viewport = Viewport.Create(doc, sheet.Id, view.Id, point)
    #
    #                     # unit_x = UnitUtils.ConvertToInternalUnits(0, UnitTypeId.Centimeters)
    #                     # unit_y = UnitUtils.ConvertToInternalUnits(31, UnitTypeId.Centimeters)
    #                     viewport.SetBoxCenter(XYZ(-1.21, .6, 0))
    #                     # bounding_box = viewport.get_BoundingBox(sheet)
    #
    #                 else:
    #                     print ("Error occurred while placing view on sheet number {}.".format(sheet.SheetNumber))
    #         # break

# ---------------------------------------------------------------------------------------------------------