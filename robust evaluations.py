from connect import *

case = get_current("Case")
patient_model = case.PatientModel
examination = get_current("Examination")
patient = get_current("Patient")

# Rigid registrations

case.CreateNamedIdentityFrameOfReferenceRegistration(FromExaminationName="AIP_uke1", ToExaminationName="AIP_plan", RegistrationName="Frame-of-reference registration AIP uke 1", Description="Bone")

case.ComputeGrayLevelBasedRigidRegistration(FloatingExaminationName="AIP_uke1", ReferenceExaminationName="AIP_plan", RegistrationName=None, UseOnlyTranslations=True, HighWeightOnBones=True, InitializeImages=True, FocusRoisNames=[])

case.CreateNamedIdentityFrameOfReferenceRegistration(FromExaminationName="AIP_uke3", ToExaminationName="AIP_plan", RegistrationName="Frame-of-reference registration AIP uke 3", Description="Bone")

case.ComputeGrayLevelBasedRigidRegistration(FloatingExaminationName="AIP_uke3", ReferenceExaminationName="AIP_plan", RegistrationName=None, UseOnlyTranslations=True, HighWeightOnBones=True, InitializeImages=True, FocusRoisNames=[])

case.CreateNamedIdentityFrameOfReferenceRegistration(FromExaminationName="DIBH_uke1", ToExaminationName="DIBH1_plan", RegistrationName="Frame-of-reference registration DIBH uke1", Description="Bone")

case.ComputeGrayLevelBasedRigidRegistration(FloatingExaminationName="DIBH_uke1", ReferenceExaminationName="DIBH1_plan", RegistrationName=None, UseOnlyTranslations=True, HighWeightOnBones=True, InitializeImages=True, FocusRoisNames=[])

case.CreateNamedIdentityFrameOfReferenceRegistration(FromExaminationName="DIBH_uke3", ToExaminationName="DIBH1_plan", RegistrationName="Frame-of-reference registration DIBH uke3", Description="Bone")

case.ComputeGrayLevelBasedRigidRegistration(FloatingExaminationName="DIBH_uke3", ReferenceExaminationName="DIBH1_plan", RegistrationName=None, UseOnlyTranslations=True, HighWeightOnBones=True, InitializeImages=True, FocusRoisNames=[])

# Deformable registrations

case.PatientModel.CreateHybridDeformableRegistrationGroup(RegistrationGroupName="HybridDefRegDIBH", ReferenceExaminationName="DIBH1_plan", TargetExaminationNames=["DIBH2_plan", "DIBH3_plan"], ControllingRoiNames=[], ControllingPoiNames=[], FocusRoiNames=[], AlgorithmSettings={ 'NumberOfResolutionLevels': 3, 'InitialResolution': { 'x': 0.5, 'y': 0.5, 'z': 0.5 }, 'FinalResolution': { 'x': 0.25, 'y': 0.25, 'z': 0.3 }, 'InitialGaussianSmoothingSigma': 2, 'FinalGaussianSmoothingSigma': 0.333333333333333, 'InitialGridRegularizationWeight': 400, 'FinalGridRegularizationWeight': 400, 'ControllingRoiWeight': 0.5, 'ControllingPoiWeight': 0.1, 'MaxNumberOfIterationsPerResolutionLevel': 1000, 'ImageSimilarityMeasure': "CorrelationCoefficient", 'DeformationStrategy': "Default", 'ConvergenceTolerance': 1E-05 })

case.MapRoiGeometriesDeformably(RoiGeometryNames=["SpinalCanal", "Lungs", "Heart", "Esophagus", "CTV_DIBH"], CreateNewRois=False, StructureRegistrationGroupNames=["HybridDefRegDIBH"], ReferenceExaminationNames=["DIBH1_plan"], TargetExaminationNames=["DIBH3_plan"], ReverseMapping=False, AbortWhenBadDisplacementField=False)

case.MapRoiGeometriesDeformably(RoiGeometryNames=["SpinalCanal", "Lungs", "Heart", "Esophagus", "CTV_DIBH"], CreateNewRois=False, StructureRegistrationGroupNames=["HybridDefRegDIBH"], ReferenceExaminationNames=["DIBH1_plan"], TargetExaminationNames=["DIBH2_plan"], ReverseMapping=False, AbortWhenBadDisplacementField=False)

case.PatientModel.CreateHybridDeformableRegistrationGroup(RegistrationGroupName="HybridDefRegFB", ReferenceExaminationName="AIP_plan", TargetExaminationNames=["CT0", "CT50"], ControllingRoiNames=[], ControllingPoiNames=[], FocusRoiNames=[], AlgorithmSettings={ 'NumberOfResolutionLevels': 3, 'InitialResolution': { 'x': 0.5, 'y': 0.5, 'z': 0.5 }, 'FinalResolution': { 'x': 0.25, 'y': 0.25, 'z': 0.3 }, 'InitialGaussianSmoothingSigma': 2, 'FinalGaussianSmoothingSigma': 0.333333333333333, 'InitialGridRegularizationWeight': 400, 'FinalGridRegularizationWeight': 400, 'ControllingRoiWeight': 0.5, 'ControllingPoiWeight': 0.1, 'MaxNumberOfIterationsPerResolutionLevel': 1000, 'ImageSimilarityMeasure': "CorrelationCoefficient", 'DeformationStrategy': "Default", 'ConvergenceTolerance': 1E-05 })

case.MapRoiGeometriesDeformably(RoiGeometryNames=["SpinalCanal", "Lungs", "Heart", "Esophagus", "CTV"], CreateNewRois=False, StructureRegistrationGroupNames=["HybridDefRegFB"], ReferenceExaminationNames=["AIP_plan"], TargetExaminationNames=["CT50"], ReverseMapping=False, AbortWhenBadDisplacementField=False)

case.MapRoiGeometriesDeformably(RoiGeometryNames=["SpinalCanal", "Lungs", "Heart", "Esophagus", "CTV"], CreateNewRois=False, StructureRegistrationGroupNames=["HybridDefRegFB"], ReferenceExaminationNames=["AIP_plan"], TargetExaminationNames=["CT0"], ReverseMapping=False, AbortWhenBadDisplacementField=False)

# Prepare CTs for dose calculation

examination = case.Examinations['CT0']

structure_set = patient_model.StructureSets[examination.Name]

if structure_set.RoiGeometries['BODY'].HasContours() == False:

  case.PatientModel.RegionsOfInterest['BODY'].CreateExternalGeometry(Examination=examination, ThresholdLevel=-250)

structure_set.SimplifyContours(RoiNames=['BODY'],RemoveHoles3D=True)

examination = case.Examinations['CT50']

structure_set = patient_model.StructureSets[examination.Name]

if structure_set.RoiGeometries['BODY'].HasContours() == False:

  case.PatientModel.RegionsOfInterest['BODY'].CreateExternalGeometry(Examination=examination, ThresholdLevel=-250)

structure_set.SimplifyContours(RoiNames=['BODY'],RemoveHoles3D=True)

structure_set = patient_model.StructureSets["DIBH2_plan"]

structure_set.SimplifyContours(RoiNames=['BODY'],RemoveHoles3D=True)

structure_set = patient_model.StructureSets["DIBH3_plan"]

structure_set.SimplifyContours(RoiNames=['BODY'],RemoveHoles3D=True)

structure_set = patient_model.StructureSets["DIBH_uke1"]

structure_set.SimplifyContours(RoiNames=['BODY'],RemoveHoles3D=True)

structure_set = patient_model.StructureSets["DIBH_uke3"]

structure_set.SimplifyContours(RoiNames=['BODY'],RemoveHoles3D=True)

structure_set = patient_model.StructureSets["AIP_uke1"]

structure_set.SimplifyContours(RoiNames=['BODY'],RemoveHoles3D=True)

structure_set = patient_model.StructureSets["AIP_uke3"]

structure_set.SimplifyContours(RoiNames=['BODY'],RemoveHoles3D=True)

# Calculate plans on additional CTs

plan = case.TreatmentPlans['auto FB']

beam_set = plan.BeamSets['auto FB']

beam_set.ComputeDoseOnAdditionalSets(OnlyOneDosePerImageSet=False, AllowGridExpansion=True, ExaminationNames=["CT0", "CT50", "AIP_uke1", "AIP_uke3"], FractionNumbers=[0, 0, 0, 0], ComputeBeamDoses=True)

plan = case.TreatmentPlans['auto DIBH']

beam_set = plan.BeamSets['auto DIBH']

beam_set.ComputeDoseOnAdditionalSets(OnlyOneDosePerImageSet=False, AllowGridExpansion=True, ExaminationNames=["DIBH2_plan", "DIBH3_plan", "DIBH_uke1", "DIBH_uke3"], FractionNumbers=[0, 0, 0, 0], ComputeBeamDoses=True)

patient.Save()
