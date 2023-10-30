# Set up and optimize IMPT plans for LA-NSCLC patients

from connect import *
import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')
from System.Windows import *
from System.Drawing import *
from System.Windows.Forms import *

db = get_current("PatientDB")
patient = get_current("Patient")
case = get_current("Case")
patient_model = case.PatientModel
examination = get_current("Examination")
structure_set = patient_model.StructureSets[examination.Name]


# Fix structures:

structure_set.SimplifyContours(RoiNames=['BODY'],RemoveHoles3D=True)
 

# Select target and apply HU correction on AIP:

roi_names = [r.Name for r in case.PatientModel.RegionsOfInterest]

if structure_set.RoiGeometries['CTV_DIBH'].PrimaryShape != None:
    target = 'CTV_DIBH'
else:
    target = 'CTV'
    igtv_corr = 'zIGTV HU corr'
    if igtv_corr not in roi_names:
        igtv_corr = case.PatientModel.CreateRoi(Name="zIGTV HU corr", Color="Gray", Type="Gtv", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
        igtv_corr.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["IGTVn"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': ["IGTVp"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ResultOperation="Union", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
        await_user_input('Set material in "zIGTV HU corr" to "Tissue Soft" and resume script execution')
    if structure_set.RoiGeometries['zIGTV HU corr'].PrimaryShape == None:
        igtv_corr = case.PatientModel.RegionsOfInterest['zIGTV HU corr']
        igtv_corr.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", ExpressionA={ 'Operation': "Union", 'SourceRoiNames': ["IGTVn"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': ["IGTVp"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ResultOperation="Union", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
        await_user_input('Set material in "zIGTV HU corr" to "Tissue Soft" and resume script execution')

# Open the Plan Design module

ui = get_current('ui')
menu_item = ui.TitleBar.Navigation.MenuItem
menu_item['Plan design'].Button_Plan_design.Click()

   
#Get plan name and prescription from user:

class Name(Form):
	def __init__(self):
		#textbox
		self.Text = "Select name for plan and beam set"
		name="Plan name"
		self.name = TextBox()
		self.name.Text=str(name)
		self.name.Location = Point(20,10)
		self.Controls.Add(self.name)
		#button
		self.but = Button()
		self.but.Text = "Save"
		self.but.Location = Point(20,50)      
		self.but.Click += self.but_click
		self.Controls.Add(self.but)
        #button function
	def but_click(self, sender, args):
		global plan_name
		plan_name = self.name.Text
		self.Close()
form = Name()
Application.Run(form)

class Dose(Form):
	def __init__(self):
		#textbox
		self.Text = "Enter the prescribed dose in Gy"
		name="Prescribed dose in Gy"
		self.name = TextBox()
		self.name.Text=str(name)
		self.name.Location = Point(20,10)
		self.Controls.Add(self.name)
		#button
		self.but = Button()
		self.but.Text = "Save"
		self.but.Location = Point(20,50)      
		self.but.Click += self.but_click
		self.Controls.Add(self.but)
        #button function
	def but_click(self, sender, args):
		global dose_gy
		dose_gy = int(self.name.Text)
		self.Close()
form = Dose()
Application.Run(form)

p_dose = dose_gy*100
n_frac = p_dose/200

# Add treatment plan:

new_plan = case.AddNewPlan(PlanName=plan_name, ExaminationName=examination.Name)

new_bs = new_plan.AddNewBeamSet(Name=plan_name, ExaminationName=examination.Name, MachineName="pulmDIBH", Modality="Protons", TreatmentTechnique="ProtonPencilBeamScanning", PatientPosition="HeadFirstSupine", NumberOfFractions=n_frac)

new_bs.SetDefaultDoseGrid(VoxelSize={ 'x': 0.3, 'y': 0.3, 'z': 0.3 })

new_bs.AddRoiPrescriptionDoseReference(RoiName=target, PrescriptionType="MedianDose", DoseValue=p_dose)


#Get beam angles from user:
number=3
class Beams(Form):
	def __init__(self):
		y=0
		#textbox
		self.name = [None] * number
		self.Text = "Add beam angles"
		for x in range(0,number):
			name="Beam Angle " + str(x+1)
			self.name[x] = TextBox()
			self.name[x].Text=str(name)
			self.name[x].Location = Point(20,y+10)
			self.Controls.Add(self.name[x])
			y=y+25
		#button
		self.but = Button()
		self.but.Text = "Save"
		self.but.Location = Point(20, y+10)      
		self.but.Click += self.but_click
		self.Controls.Add(self.but)
        #button function
	def but_click(self, sender, args):
		global ba1
		global ba2
		global ba3
		ba1 = int(self.name[0].Text)
		ba2 = int(self.name[1].Text)
		ba3 = int(self.name[2].Text)
		self.Close()
form = Beams()
Application.Run(form)

# Add beams:

center = structure_set.RoiGeometries[target].GetCenterOfRoi()

beam_1 = new_bs.CreatePBSIonBeam(SnoutId="snout40", SpotTuneId="3.0", RangeShifter="RS4cm", MinimumAirGap=5, MetersetRateSetting="", IsocenterData={ 'Position': { 'x': center.x, 'y': center.y, 'z': center.z }, 'NameOfIsocenterToRef': "", 'Name': plan_name + "1", 'Color': "98, 184, 234" }, Name="Beam 1", Description="", GantryAngle=ba1, CouchRotationAngle=0, CouchPitchAngle=0, CouchRollAngle=0, CollimatorAngle=0)

beam_2 = new_bs.CreatePBSIonBeam(SnoutId="snout40", SpotTuneId="3.0", RangeShifter="RS4cm", MinimumAirGap=5, MetersetRateSetting="", IsocenterData={ 'Position': { 'x': center.x, 'y': center.y, 'z': center.z }, 'NameOfIsocenterToRef': plan_name + "1", 'Name': plan_name + "1", 'Color': "98, 184, 234" }, Name="Beam 2", Description="", GantryAngle=ba2, CouchRotationAngle=0, CouchPitchAngle=0, CouchRollAngle=0, CollimatorAngle=0)

beam_3 = new_bs.CreatePBSIonBeam(SnoutId="snout40", SpotTuneId="3.0", RangeShifter="RS4cm", MinimumAirGap=5, MetersetRateSetting="", IsocenterData={ 'Position': { 'x': center.x, 'y': center.y, 'z': center.z }, 'NameOfIsocenterToRef': plan_name + "1", 'Name': plan_name + "1", 'Color': "98, 184, 234" }, Name="Beam 3", Description="", GantryAngle=ba3, CouchRotationAngle=0, CouchPitchAngle=0, CouchRollAngle=0, CollimatorAngle=0)

await_user_input('Ready to start optimization? Check beam angles, range shifter, air gap, field specific targets, optimization algorithm (Monte Carlo 10000 ions/spot), dose algorithm (Monte Carlo 0.5% uncert.). Check that right plan is open. Resume script execution.')

patient.Save()


#---------------- Optimize plan -------------------

plan = get_current("Plan")
beam_set = get_current("BeamSet")

# Open the Plan Optimization module

menu_item['Plan optimization'].Button_Plan_optimization.Click()


po = plan.PlanOptimizations[0]

p_dose = beam_set.Prescription.PrescriptionDoseReferences[0].DoseValue


# Add objectives for CTV and BODY
  
with CompositeAction('Add optimization function'):

  retval_0 = po.AddOptimizationFunction(FunctionType="UniformDose", RoiName=target, IsRobust=True)

  po.Objective.ConstituentFunctions[0].DoseFunctionParameters.DoseLevel = p_dose

  po.Objective.ConstituentFunctions[0].DoseFunctionParameters.Weight = 500


with CompositeAction('Add optimization function'):

  retval_1 = po.AddOptimizationFunction(FunctionType="MaxDose", RoiName="BODY")

  po.Objective.ConstituentFunctions[1].DoseFunctionParameters.DoseLevel = p_dose + 50

  po.Objective.ConstituentFunctions[1].DoseFunctionParameters.Weight = 1500


with CompositeAction('Add optimization function'):

  retval_2 = po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName="BODY")

  po.Objective.ConstituentFunctions[2].DoseFunctionParameters.HighDoseLevel = p_dose

  po.Objective.ConstituentFunctions[2].DoseFunctionParameters.LowDoseLevel = 1000

  po.Objective.ConstituentFunctions[2].DoseFunctionParameters.LowDoseDistance = 1.5

  po.Objective.ConstituentFunctions[2].DoseFunctionParameters.Weight = 5


#Set optimization and robustness parameters and start optimization

opt_param = po.OptimizationParameters

with CompositeAction('Set optimization parameters'):

    opt_param.Algorithm.MaxNumberOfIterations = 200

    opt_param.Algorithm.OptimalityTolerance = 1E-06

    opt_param.PencilBeamScanningProperties.NumberOfIterationsBeforeSpotWeightBounding = 40

    opt_param.SaveRobustnessParameters(PositionUncertaintyAnterior=0.5, PositionUncertaintyPosterior=0.5, PositionUncertaintySuperior=0.5, PositionUncertaintyInferior=0.5, PositionUncertaintyLeft=0.5, PositionUncertaintyRight=0.5, DensityUncertainty=0.035, PositionUncertaintySetting="Universal", IndependentLeftRight=True, IndependentAnteriorPosterior=True, IndependentSuperiorInferior=True, ComputeExactScenarioDoses=False, NamesOfNonPlanningExaminations=[], PatientGeometryUncertaintyType="PerTreatmentCourse", PositionUncertaintyType="PerTreatmentCourse", TreatmentCourseScenariosFactor=1000)

po.RunOptimization()


# Add objectives for OARs based on achieved dose distribution

total_dose = plan.TreatmentCourse.TotalDose

heart_dose_1 = total_dose.GetDoseStatistic(RoiName="Heart",DoseType="Average")

lungs_dose_1 = total_dose.GetDoseStatistic(RoiName="Lungs",DoseType="Average")

esophagus_dose_1 = total_dose.GetDoseStatistic(RoiName="Esophagus",DoseType="Average")

spinal_dose_1 = total_dose.GetDoseStatistic(RoiName="SpinalCanal",DoseType="Max")

if 'BrachialPlexus' in roi_names:
    
    brachial_dose_1 = total_dose.GetDoseStatistic(RoiName="BrachialPlexus",DoseType="Max")


with CompositeAction('Add optimization function'):

  retval_3 = po.AddOptimizationFunction(FunctionType="MaxEud", RoiName="Heart")

  po.Objective.ConstituentFunctions[3].DoseFunctionParameters.DoseLevel = heart_dose_1 * 0.9

  po.Objective.ConstituentFunctions[3].DoseFunctionParameters.Weight = 5


with CompositeAction('Add optimization function'):

  retval_4 = po.AddOptimizationFunction(FunctionType="MaxEud", RoiName="Lungs")

  po.Objective.ConstituentFunctions[4].DoseFunctionParameters.DoseLevel = lungs_dose_1 * 0.9

  po.Objective.ConstituentFunctions[4].DoseFunctionParameters.Weight = 5


with CompositeAction('Add optimization function'):

  retval_5 = po.AddOptimizationFunction(FunctionType="MaxEud", RoiName="Esophagus")

  po.Objective.ConstituentFunctions[5].DoseFunctionParameters.DoseLevel = esophagus_dose_1 * 0.9

  po.Objective.ConstituentFunctions[5].DoseFunctionParameters.Weight = 5


with CompositeAction('Add optimization function'):

  if spinal_dose_1 > 4800:

      retval_6 = po.AddOptimizationFunction(FunctionType="MaxDose", RoiName="SpinalCanal", IsConstraint=True, IsRobust=True)

      po.Constraints[0].DoseFunctionParameters.DoseLevel = 4800

  elif spinal_dose_1 > 4000:
      
      retval_6 = po.AddOptimizationFunction(FunctionType="MaxDose", RoiName="SpinalCanal",IsRobust=True)

      po.Objective.ConstituentFunctions[6].DoseFunctionParameters.DoseLevel = spinal_dose_1 - 200
  
      po.Objective.ConstituentFunctions[6].DoseFunctionParameters.Weight = 5
        
  elif spinal_dose_1 < 200:
      
      retval_6 = po.AddOptimizationFunction(FunctionType="MaxDose", RoiName="SpinalCanal",IsRobust=True)

      po.Objective.ConstituentFunctions[6].DoseFunctionParameters.DoseLevel = spinal_dose_1
  
      po.Objective.ConstituentFunctions[6].DoseFunctionParameters.Weight = 1
      
  else:

      retval_6 = po.AddOptimizationFunction(FunctionType="MaxDose", RoiName="SpinalCanal")

      po.Objective.ConstituentFunctions[6].DoseFunctionParameters.DoseLevel = spinal_dose_1 - 200
  
      po.Objective.ConstituentFunctions[6].DoseFunctionParameters.Weight = 5


if 'BrachialPlexus' in roi_names:

    if brachial_dose_1 > 6000:
    
        with CompositeAction('Add optimization function'):

          retval_7 = po.AddOptimizationFunction(FunctionType="MaxDose", RoiName="BrachialPlexus")

          if spinal_dose_1 > 4800:

              po.Objective.ConstituentFunctions[6].DoseFunctionParameters.DoseLevel = 6000

              po.Objective.ConstituentFunctions[6].DoseFunctionParameters.Weight = 5

          else:
              
              po.Objective.ConstituentFunctions[7].DoseFunctionParameters.DoseLevel = 6000

              po.Objective.ConstituentFunctions[7].DoseFunctionParameters.Weight = 5



# Restart optimization with new objectives

po.ResetOptimization()

po.RunOptimization(ScalingOfSoftMachineConstraints=None)



# Adjust OAR objectives if achieved dose is lower than initial objective

total_dose = plan.TreatmentCourse.TotalDose

heart_dose_2 = total_dose.GetDoseStatistic(RoiName="Heart",DoseType="Average")

lungs_dose_2 = total_dose.GetDoseStatistic(RoiName="Lungs",DoseType="Average")

esophagus_dose_2 = total_dose.GetDoseStatistic(RoiName="Esophagus",DoseType="Average")

restart_opt = 0

if heart_dose_2 < heart_dose_1 * 0.9:
  
    po.Objective.ConstituentFunctions[3].DoseFunctionParameters.DoseLevel = heart_dose_2 * 0.95

    restart_opt = 1

if lungs_dose_2 < lungs_dose_1 * 0.9:

    po.Objective.ConstituentFunctions[4].DoseFunctionParameters.DoseLevel = lungs_dose_2 *0.95

    restart_opt = 1
 
if esophagus_dose_2 < esophagus_dose_1 * 0.9:

    po.Objective.ConstituentFunctions[5].DoseFunctionParameters.DoseLevel = esophagus_dose_2 * 0.95

    restart_opt = 1


# Restart optimization if objectives have been changed

if restart_opt == 1:

    po.ResetOptimization()

    po.RunOptimization(ScalingOfSoftMachineConstraints=None)
    

# Compute final dose

beam_set.AccurateDoseAlgorithm.MCStatisticalUncertaintyForFinalDose = 0.005

beam_set.ComputeDose(ComputeBeamDoses=True, DoseAlgorithm="IonMonteCarlo", ForceRecompute=False)

beam_set.SetAutoScaleToPrimaryPrescription(AutoScale=True)


# Open the Plan Evaluation module

menu_item['Plan evaluation'].Button_Plan_evaluation.Click()


# Compute robust evaluation scenarios

retval_8 = beam_set.CreateRadiationSetScenarioGroup(Name="SR", UseIsotropicPositionUncertainty=False, PositionUncertaintySuperior=0.5, PositionUncertaintyInferior=0.5, PositionUncertaintyPosterior=0.5, PositionUncertaintyAnterior=0.5, PositionUncertaintyLeft=0.5, PositionUncertaintyRight=0.5, PositionUncertaintyFormation="DiagonalEndPoints", PositionUncertaintyList=None, DensityUncertaintyPercent=3.5, NumberOfDensityDiscretizationPoints=2, ShallAddScenariosOnPlanningExamination=True, NamesOfNonPlanningExaminations=[], ComputeScenarioDosesAfterGroupCreation=True, IncludeZeroPositionUncertainty=False)


patient.Save()
