"""
Set up and optimize dose escalated IMPT plans for LA-NSCLC patients
RayStation v. 2023B
10.04.2024
"""

from connect import *
from tkinter import *
from tkinter import ttk

try:
    db = get_current("PatientDB")
    patient = get_current("Patient")
    case = get_current("Case")
    patient_model = case.PatientModel
    examination = get_current("Examination")
    structure_set = patient_model.StructureSets[examination.Name]
except:
    print ('Pasient/case/CT er ikke lastet. Skiptet stoppes.')
    exit()
 

ui = get_current('ui')
ui.TitleBar.Navigation.MenuItem['Plan design'].Button.Click()


# ------------------------------ GUI for målvolum og doser ----------------------------

ctv_list = []
gtv_list = []
oar_list = []

for roi in patient_model.RegionsOfInterest:
    if roi.Type == 'Ctv':
        ctv_list.append(roi.Name)
        
for roi in patient_model.RegionsOfInterest:
    if roi.Type == 'Gtv':
        gtv_list.append(roi.Name)
        
for roi in patient_model.RegionsOfInterest:
    if roi.Type != 'Ctv' and roi.Type != 'Gtv' and roi.Type != 'Ptv':
        oar_list.append(roi.Name)
        
window1 = Tk()
window1.title('Velg strukturer som skal brukes i optimeringen')

lbl1 = Label(window1, text='CTV')
lbl1.grid(column=0, row=0)
lbl1.config(width=60, height=3)
ctv_var = StringVar()
ctvbox = ttk.Combobox(window1, values=ctv_list, textvariable=ctv_var)
ctvbox.grid(column=1, row=0)
ctvbox.config(width=18, height=10)
ctvbox.current(0)

lbl2 = Label(window1, text='GTVp')
lbl2.grid(column=0, row=1)
lbl2.config(width=60, height=3)
gtvp_var = StringVar()
gtvpbox = ttk.Combobox(window1, values=gtv_list, textvariable=gtvp_var)
gtvpbox.grid(column=1, row=1)
gtvpbox.config(width=18, height=10)

lbl3 = Label(window1, text='GTVn')
lbl3.grid(column=0, row=2)
lbl3.config(width=60, height=3)
gtvn_var = StringVar()
gtvnbox = ttk.Combobox(window1, values=gtv_list, textvariable=gtvn_var)
gtvnbox.grid(column=1, row=2)
gtvnbox.config(width=18, height=10)

lbl4 = Label(window1, text='BODY')
lbl4.grid(column=0, row=3)
lbl4.config(width=60, height=3)
body_var = StringVar()
bodybox = ttk.Combobox(window1, values=oar_list, textvariable=body_var)
bodybox.grid(column=1, row=3)
bodybox.config(width=18, height=10)
bodybox.current(0)

lbl5 = Label(window1, text='Lungs')
lbl5.grid(column=0, row=4)
lbl5.config(width=60, height=3)
lungs_var = StringVar()
lungsbox = ttk.Combobox(window1, values=oar_list, textvariable=lungs_var)
lungsbox.grid(column=1, row=4)
lungsbox.config(width=18, height=10)

lbl6 = Label(window1, text='Heart')
lbl6.grid(column=0, row=5)
lbl6.config(width=60, height=3)
heart_var = StringVar()
heartbox = ttk.Combobox(window1, values=oar_list, textvariable=heart_var)
heartbox.grid(column=1, row=5)
heartbox.config(width=18, height=10)

lbl7 = Label(window1, text='Esophagus')
lbl7.grid(column=0, row=6)
lbl7.config(width=60, height=3)
esoph_var = StringVar()
esophbox = ttk.Combobox(window1, values=oar_list, textvariable=esoph_var)
esophbox.grid(column=1, row=6)
esophbox.config(width=18, height=10)

lbl8 = Label(window1, text='Spinal canal (ev. spinal cord PRV)')
lbl8.grid(column=0, row=7)
lbl8.config(width=60, height=3)
spinal_var = StringVar()
spinalbox = ttk.Combobox(window1, values=oar_list, textvariable=spinal_var)
spinalbox.grid(column=1, row=7)
spinalbox.config(width=18, height=10)

lbl9 = Label(window1, text='Chest wall/thoracic wall')
lbl9.grid(column=0, row=8)
lbl9.config(width=60, height=3)
wall_var = StringVar()
wallbox = ttk.Combobox(window1, values=oar_list, textvariable=wall_var)
wallbox.grid(column=1, row=8)
wallbox.config(width=18, height=10)

lbl10 = Label(window1, text='Mediastinum/connective tissue')
lbl10.grid(column=0, row=9)
lbl10.config(width=60, height=3)
ct_var = StringVar()
ctbox = ttk.Combobox(window1, values=oar_list, textvariable=ct_var)
ctbox.grid(column=1, row=9)
ctbox.config(width=18, height=10)

lbl11 = Label(window1, text='Trachea')
lbl11.grid(column=0, row=10)
lbl11.config(width=60, height=3)
trachea_var = StringVar()
tracheabox = ttk.Combobox(window1, values=oar_list, textvariable=trachea_var)
tracheabox.grid(column=1, row=10)
tracheabox.config(width=18, height=10)

lbl12 = Label(window1, text='Bronchi')
lbl12.grid(column=0, row=11)
lbl12.config(width=60, height=3)
bronchi_var = StringVar()
bronchibox = ttk.Combobox(window1, values=oar_list, textvariable=bronchi_var)
bronchibox.grid(column=1, row=11)
bronchibox.config(width=18, height=10)

lbl13 = Label(window1, text='Aorta')
lbl13.grid(column=0, row=12)
lbl13.config(width=60, height=3)
aorta_var = StringVar()
aortabox = ttk.Combobox(window1, values=oar_list, textvariable=aorta_var)
aortabox.grid(column=1, row=12)
aortabox.config(width=18, height=10)

lbl14 = Label(window1, text='Plexus brachialis')
lbl14.grid(column=0, row=13)
lbl14.config(width=60, height=3)
plexus_var = StringVar()
plexusbox = ttk.Combobox(window1, values=oar_list, textvariable=plexus_var)
plexusbox.grid(column=1, row=13)
plexusbox.config(width=18, height=10)

def Button_pressed():
    global ctv
    global gtvp
    global gtvn
    global body
    global lungs
    global heart
    global esophagus
    global spinal
    global chestwall
    global mediastinum
    global trachea
    global bronchi
    global aorta
    global plexus
    ctv = ctv_var.get()
    gtvp = gtvp_var.get()
    gtvn = gtvn_var.get()
    body = body_var.get() 
    lungs = lungs_var.get()
    heart = heart_var.get()
    esophagus = esoph_var.get()
    spinal = spinal_var.get()
    chestwall = wall_var.get()
    mediastinum = ct_var.get()
    trachea = trachea_var.get()
    bronchi = bronchi_var.get()
    aorta = aorta_var.get()
    plexus = plexus_var.get()
    window1.destroy()
	
button = Button(window1, text='Lagre', command=Button_pressed)
button.grid(column=1, row=15)

window1.rowconfigure(15, minsize=50)
window1.columnconfigure(1, minsize=200)

window1.mainloop()


# ------------------------------ GUI for feltvinkler ----------------------------

window2 = Tk()
window2.title('Angi feltvinkler')

lbl1 = Label(window2, text='Vinkel, felt 1 (grader)')
lbl2 = Label(window2, text='Vinkel, felt 2 (grader)')
lbl3 = Label(window2, text='Vinkel, felt 3 (grader)')
lbl1.grid(column=0, row=0)
lbl2.grid(column=0, row=1)
lbl3.grid(column=0, row=2)
lbl1.config(width=20, height=3)
lbl2.config(width=20, height=3)
lbl3.config(width=20, height=3)

ba1_var = DoubleVar()
box1 = Entry(window2, textvariable=ba1_var)
box1.grid(column=1, row=0)

ba2_var = DoubleVar()
box2 = Entry(window2, textvariable=ba2_var)
box2.grid(column=1, row=1)

ba3_var = DoubleVar()
box3 = Entry(window2, textvariable=ba3_var)
box3.grid(column=1, row=2)

def Button_pressed():
    global ba1
    global ba2
    global ba3
    ba1 = ba1_var.get()
    ba2 = ba2_var.get()
    ba3 = ba3_var.get()
    window2.destroy()

button = Button(window2, text='Lagre', command=Button_pressed)
button.grid(column=1, row=3)

window2.rowconfigure(3, minsize=50)
window2.columnconfigure(1, minsize=200)

window2.mainloop()


# ----------------------- Add treatment plan -------------------------

new_plan = case.AddNewPlan(PlanName="IMPT eskalert", ExaminationName=examination.Name)
patient.Save()
new_plan.SetCurrent()

new_bs = new_plan.AddNewBeamSet(Name="IMPT eskalert", ExaminationName=examination.Name, MachineName="ProB360_Columbus", Modality="Protons", TreatmentTechnique="ProtonPencilBeamScanning", PatientPosition="HeadFirstSupine", NumberOfFractions=33, RbeModelName="Constant 1.1")
new_bs.SetDefaultDoseGrid(VoxelSize={ 'x': 0.3, 'y': 0.3, 'z': 0.3 })

ctv_center = structure_set.RoiGeometries[ctv].GetCenterOfRoi()
iso_data = new_bs.CreateDefaultIsocenterData(Position=ctv_center)

beam_1 = new_bs.CreatePBSIonBeam(SnoutId="S1", SpotTuneId="4.0", RangeShifter="RS_3cm", MinimumAirGap=5, IsocenterData=iso_data, Name="Beam 1", GantryAngle=ba1)
beam_2 = new_bs.CreatePBSIonBeam(SnoutId="S1", SpotTuneId="4.0", RangeShifter="RS_3cm", MinimumAirGap=5, IsocenterData=iso_data, Name="Beam 2", GantryAngle=ba2)
beam_3 = new_bs.CreatePBSIonBeam(SnoutId="S1", SpotTuneId="4.0", RangeShifter="RS_3cm", MinimumAirGap=5, IsocenterData=iso_data, Name="Beam 3", GantryAngle=ba3)

await_user_input('Ready to start optimization? Check beam angles, range shifter, air gap, optimization algorithm (Monte Carlo 10000 ions/spot), dose algorithm (Monte Carlo 0.5% uncert.). Resume script execution.')

patient.Save()


#----------------------- Optimize plan - Round 1 --------------------------

ui.TitleBar.Navigation.MenuItem['Plan optimization'].Button.Click()
plan = get_current("Plan")
beam_set = get_current("BeamSet")
po = plan.PlanOptimizations[0]

# Add objectives for CTV and BODY

obj_num = 0
const_num = 0

with CompositeAction('Add optimization function'):
    ctv_min = po.AddOptimizationFunction(FunctionType="MinDose", RoiName=ctv, IsRobust=True, UseRbeDose=True)
    po.Objective.ConstituentFunctions[obj_num].DoseFunctionParameters.DoseLevel = 6600
    po.Objective.ConstituentFunctions[obj_num].DoseFunctionParameters.Weight = 100
    obj_num = obj_num + 1
  
if gtvp:    
    with CompositeAction('Add optimization function'):
        gtvp_min = po.AddOptimizationFunction(FunctionType="MinEUD", RoiName=gtvp, IsRobust=True, UseRbeDose=True)
        po.Objective.ConstituentFunctions[obj_num].DoseFunctionParameters.DoseLevel = 9500
        po.Objective.ConstituentFunctions[obj_num].DoseFunctionParameters.Weight = 100
        obj_num = obj_num + 1  
    with CompositeAction('Add optimization function'):
        gtvp_max = po.AddOptimizationFunction(FunctionType="MaxEUD", RoiName=gtvp, IsRobust=True, UseRbeDose=True)
        po.Objective.ConstituentFunctions[obj_num].DoseFunctionParameters.DoseLevel = 9500
        po.Objective.ConstituentFunctions[obj_num].DoseFunctionParameters.Weight = 100
        obj_num = obj_num + 1     

if gtvn:    
    with CompositeAction('Add optimization function'):
        gtvn_min = po.AddOptimizationFunction(FunctionType="MinEUD", RoiName=gtvn, IsRobust=True, UseRbeDose=True)
        po.Objective.ConstituentFunctions[obj_num].DoseFunctionParameters.DoseLevel = 7400
        po.Objective.ConstituentFunctions[obj_num].DoseFunctionParameters.Weight = 100
        obj_num = obj_num + 1  
    with CompositeAction('Add optimization function'):
        gtvn_max = po.AddOptimizationFunction(FunctionType="MaxEUD", RoiName=gtvn, IsRobust=True, UseRbeDose=True)
        po.Objective.ConstituentFunctions[obj_num].DoseFunctionParameters.DoseLevel = 7400
        po.Objective.ConstituentFunctions[obj_num].DoseFunctionParameters.Weight = 100
        obj_num = obj_num + 1

with CompositeAction('Add optimization function'):
    body_fo = po.AddOptimizationFunction(FunctionType="DoseFallOff", RoiName=body, UseRbeDose=True)
    po.Objective.ConstituentFunctions[obj_num].DoseFunctionParameters.HighDoseLevel = 6600
    po.Objective.ConstituentFunctions[obj_num].DoseFunctionParameters.LowDoseLevel = 1000
    po.Objective.ConstituentFunctions[obj_num].DoseFunctionParameters.LowDoseDistance = 1.5
    po.Objective.ConstituentFunctions[obj_num].DoseFunctionParameters.Weight = 5
    obj_num = obj_num + 1
        
# Add robust max dose constraints for OARs

if spinal:
    with CompositeAction('Add optimization function'):
        spinal_max = po.AddOptimizationFunction(FunctionType="MaxDvh", RoiName=spinal, IsConstraint=True, IsRobust=True, UseRbeDose=True)
        po.Constraints[const_num].DoseFunctionParameters.DoseLevel = 5000
        po.Constraints[const_num].DoseFunctionParameters.AbsoluteVolume = 0.05
        po.Constraints[const_num].DoseFunctionParameters.IsAbsoluteVolume = True
        const_num = const_num + 1

if heart:
    with CompositeAction('Add optimization function'):
        heart_max = po.AddOptimizationFunction(FunctionType="MaxDvh", RoiName=heart, IsConstraint=True, IsRobust=True, UseRbeDose=True)
        po.Constraints[const_num].DoseFunctionParameters.DoseLevel = 7400
        po.Constraints[const_num].DoseFunctionParameters.AbsoluteVolume = 1
        po.Constraints[const_num].DoseFunctionParameters.IsAbsoluteVolume = True
        const_num = const_num + 1

if esophagus:
    with CompositeAction('Add optimization function'):
        esoph_max = po.AddOptimizationFunction(FunctionType="MaxDvh", RoiName=esophagus, IsConstraint=True, IsRobust=True, UseRbeDose=True)
        po.Constraints[const_num].DoseFunctionParameters.DoseLevel = 7000
        po.Constraints[const_num].DoseFunctionParameters.AbsoluteVolume = 1
        po.Constraints[const_num].DoseFunctionParameters.IsAbsoluteVolume = True
        const_num = const_num + 1
        
if chestwall:
    with CompositeAction('Add optimization function'):
        cw_max = po.AddOptimizationFunction(FunctionType="MaxDvh", RoiName=chestwall, IsConstraint=True, IsRobust=True, UseRbeDose=True)
        po.Constraints[const_num].DoseFunctionParameters.DoseLevel = 7400
        po.Constraints[const_num].DoseFunctionParameters.AbsoluteVolume = 1
        po.Constraints[const_num].DoseFunctionParameters.IsAbsoluteVolume = True
        const_num = const_num + 1

if mediastinum:
    with CompositeAction('Add optimization function'):
        ct_max = po.AddOptimizationFunction(FunctionType="MaxDvh", RoiName=mediastinum, IsConstraint=True, IsRobust=True, UseRbeDose=True)
        po.Constraints[const_num].DoseFunctionParameters.DoseLevel = 7400
        po.Constraints[const_num].DoseFunctionParameters.AbsoluteVolume = 1
        po.Constraints[const_num].DoseFunctionParameters.IsAbsoluteVolume = True
        const_num = const_num + 1

if trachea:
    with CompositeAction('Add optimization function'):
        cw_max = po.AddOptimizationFunction(FunctionType="MaxDvh", RoiName=trachea, IsConstraint=True, IsRobust=True, UseRbeDose=True)
        po.Constraints[const_num].DoseFunctionParameters.DoseLevel = 7400
        po.Constraints[const_num].DoseFunctionParameters.AbsoluteVolume = 1
        po.Constraints[const_num].DoseFunctionParameters.IsAbsoluteVolume = True
        const_num = const_num + 1

if bronchi:
    with CompositeAction('Add optimization function'):
        bronchi_max = po.AddOptimizationFunction(FunctionType="MaxDvh", RoiName=bronchi, IsConstraint=True, IsRobust=True, UseRbeDose=True)
        po.Constraints[const_num].DoseFunctionParameters.DoseLevel = 7400
        po.Constraints[const_num].DoseFunctionParameters.AbsoluteVolume = 1
        po.Constraints[const_num].DoseFunctionParameters.IsAbsoluteVolume = True
        const_num = const_num + 1

if aorta:
    with CompositeAction('Add optimization function'):
        aorta_max = po.AddOptimizationFunction(FunctionType="MaxDvh", RoiName=aorta, IsConstraint=True, IsRobust=True, UseRbeDose=True)
        po.Constraints[const_num].DoseFunctionParameters.DoseLevel = 7400
        po.Constraints[const_num].DoseFunctionParameters.AbsoluteVolume = 1
        po.Constraints[const_num].DoseFunctionParameters.IsAbsoluteVolume = True
        const_num = const_num + 1

if plexus:
    with CompositeAction('Add optimization function'):
        bp_max = po.AddOptimizationFunction(FunctionType="MaxDvh", RoiName=plexus, IsConstraint=True, IsRobust=True, UseRbeDose=True)
        po.Constraints[const_num].DoseFunctionParameters.DoseLevel = 7400
        po.Constraints[const_num].DoseFunctionParameters.AbsoluteVolume = 1
        po.Constraints[const_num].DoseFunctionParameters.IsAbsoluteVolume = True
        const_num = const_num + 1
        
#Set optimization and robustness parameters and start optimization

opt_param = po.OptimizationParameters

with CompositeAction('Set optimization parameters'):
    opt_param.Algorithm.MaxNumberOfIterations = 200
    opt_param.Algorithm.OptimalityTolerance = 1E-06
    opt_param.PencilBeamScanningProperties.NumberOfIterationsBeforeSpotWeightBounding = 40
    opt_param.SaveRobustnessParameters(PositionUncertaintyAnterior=0.5, PositionUncertaintyPosterior=0.5, PositionUncertaintySuperior=0.5, PositionUncertaintyInferior=0.5, PositionUncertaintyLeft=0.5, PositionUncertaintyRight=0.5, DensityUncertainty=0.035, PositionUncertaintySetting="Universal", IndependentLeftRight=True, IndependentAnteriorPosterior=True, IndependentSuperiorInferior=True, ComputeExactScenarioDoses=False, NamesOfNonPlanningExaminations=[], PatientGeometryUncertaintyType="PerTreatmentCourse", PositionUncertaintyType="PerTreatmentCourse", TreatmentCourseScenariosFactor=1000)

po.RunOptimization()


# ---------------------------- Optimize plan - Round 2 ---------------------------

# Add mean dose objectives for OARs based on achieved dose distribution in Round 1

total_dose = plan.TreatmentCourse.TotalDose

if heart:
    heart_dose_1 = total_dose.GetDoseStatistic(RoiName=heart,DoseType="Average")
    with CompositeAction('Add optimization function'):
        heart_mean = po.AddOptimizationFunction(FunctionType="MaxEud", RoiName=heart, UseRbeDose=True)
        po.Objective.ConstituentFunctions[obj_num].DoseFunctionParameters.DoseLevel = heart_dose_1 * 0.9
        po.Objective.ConstituentFunctions[obj_num].DoseFunctionParameters.Weight = 5
        obj_num_heart = obj_num
        obj_num = obj_num + 1

if lungs:
    lungs_dose_1 = total_dose.GetDoseStatistic(RoiName=lungs,DoseType="Average")
    with CompositeAction('Add optimization function'):
        lungs_mean = po.AddOptimizationFunction(FunctionType="MaxEud", RoiName=lungs, UseRbeDose=True)
        po.Objective.ConstituentFunctions[obj_num].DoseFunctionParameters.DoseLevel = lungs_dose_1 * 0.9
        po.Objective.ConstituentFunctions[obj_num].DoseFunctionParameters.Weight = 5
        obj_num_lungs = obj_num
        obj_num = obj_num + 1

if esophagus:
    esoph_dose_1 = total_dose.GetDoseStatistic(RoiName=esophagus,DoseType="Average")
    with CompositeAction('Add optimization function'):
        esoph_mean = po.AddOptimizationFunction(FunctionType="MaxEud", RoiName=esophagus, UseRbeDose=True)
        po.Objective.ConstituentFunctions[obj_num].DoseFunctionParameters.DoseLevel = esoph_dose_1 * 0.9
        po.Objective.ConstituentFunctions[obj_num].DoseFunctionParameters.Weight = 5
        obj_num_esoph = obj_num
        obj_num = obj_num + 1

# Restart optimization with new objectives

po.ResetOptimization()
po.RunOptimization()


# ---------------------------- Optimize plan - Round 3 ---------------------------

# Adjust OAR objectives if achieved dose is lower than initial objective + 0.1 Gy

total_dose = plan.TreatmentCourse.TotalDose

restart_opt = 0

if heart:
    heart_dose_2 = total_dose.GetDoseStatistic(RoiName=heart,DoseType="Average")
    if heart_dose_2 < (heart_dose_1 * 0.9 + 10):
        po.Objective.ConstituentFunctions[obj_num_heart].DoseFunctionParameters.DoseLevel = heart_dose_2 * 0.9
        restart_opt = 1

if lungs:
    lungs_dose_2 = total_dose.GetDoseStatistic(RoiName=lungs,DoseType="Average")
    if lungs_dose_2 < (lungs_dose_1 * 0.9 + 10):
        po.Objective.ConstituentFunctions[obj_num_lungs].DoseFunctionParameters.DoseLevel = lungs_dose_2 * 0.9
        restart_opt = 1

if esophagus:
    esoph_dose_2 = total_dose.GetDoseStatistic(RoiName=esophagus,DoseType="Average")
    if esoph_dose_2 < (esoph_dose_1 * 0.9 + 10):
        po.Objective.ConstituentFunctions[obj_num_esoph].DoseFunctionParameters.DoseLevel = esoph_dose_2 * 0.9
        restart_opt = 1

# Restart optimization if objectives have been changed

if restart_opt == 1:
    po.ResetOptimization()
    po.RunOptimization()
    

# Compute final dose

beam_set.AccurateDoseAlgorithm.MCStatisticalUncertaintyForFinalDose = 0.005
beam_set.ComputeDose(ComputeBeamDoses=True, DoseAlgorithm="IonMonteCarlo", ForceRecompute=False)

# Compute robust evaluation scenarios

robusteval = beam_set.CreateRadiationSetScenarioGroup(Name="5mm/3.5%", UseIsotropicPositionUncertainty=False, PositionUncertaintySuperior=0.5, PositionUncertaintyInferior=0.5, PositionUncertaintyPosterior=0.5, PositionUncertaintyAnterior=0.5, PositionUncertaintyLeft=0.5, PositionUncertaintyRight=0.5, PositionUncertaintyFormation="DiagonalEndPoints", PositionUncertaintyList=None, DensityUncertaintyPercent=3.5, NumberOfDensityDiscretizationPoints=2, ShallAddScenariosOnPlanningExamination=True, NamesOfNonPlanningExaminations=[], ComputeScenarioDosesAfterGroupCreation=True, IncludeZeroPositionUncertainty=False)

patient.Save()
