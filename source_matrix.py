import random
import numpy as np
from scipy.stats import *
multivariate_normal
import matplotlib.pyplot as plt
from math import *

precision=3
N=1000 
sigma =2
mu = 10
data = np.random.randn(N) * sigma + mu

fichier = open("matrice.mac", "w")
fichier.write("/control/alias enableXrayBoundary 1")
fichier.write("\n#========================VERBOSITY#========================")
fichier.write("\n#/control/execute mac/verbose.mac")
fichier.write("\n#=======================")
fichier.write("\n# VISUALISATION")
fichier.write("\n#============")
fichier.write("\n#/control/execute mac/visu.mac")
fichier.write("\n#/vis/disable")
fichier.write("\n#============= GEOMETRY")

fichier.write("\n/gate/geometry/setMaterialDatabase data/GateMaterials.db")
fichier.write("\n# World")
fichier.write("\n/gate/world/geometry/setXLength 50 cm")
fichier.write("\n/gate/world/geometry/setYLength 50 cm")
fichier.write("\n/gate/world/geometry/setZLength 50 cm")
fichier.write("\n/gate/world/setMaterial Vacuum ")
fichier.write("\n# PHYSICS===================")
fichier.write("\n/gate/physics/addPhysicsList            emstandard_opt4")
fichier.write("\n/gate/physics/addProcess XrayBoundary")
fichier.write("\n/gate/physics/displayCuts")
fichier.write("\n#===============DETECTORS==============DETECTION PLANE")
fichier.write("\n/gate/world/daughters/name                   	Detector")
fichier.write("\n/gate/world/daughters/insert                 	box")
fichier.write("\n/gate/Detector/geometry/setXLength      	13 cm")
fichier.write("\n/gate/Detector/geometry/setYLength      	13 cm")
fichier.write("\n/gate/Detector/geometry/setZLength      	1 mm")
fichier.write("\n/gate/Detector/placement/setTranslation 	0 0 20 cm")
fichier.write("\n/gate/Detector/setMaterial              	Vacuum")
fichier.write("\n# FLUENCE OF GAMMA")
fichier.write("\n/gate/actor/addActor FluenceActor         	DetFluence")
fichier.write("\n/gate/actor/DetFluence/attachTo     		Detector")
fichier.write("\n/gate/actor/DetFluence/stepHitType   		pre")
fichier.write("\n/gate/actor/DetFluence/setResolution 		100 100 1")
fichier.write("\n/gate/actor/DetFluence/save 			output/fluence_XrayBoundary.mhd")
fichier.write("\n/gate/Detector/vis/setColor              	yellow")
fichier.write("\n#==========INITIALISATION")
fichier.write("\n#==========")
fichier.write("\n/gate/run/initialize")
fichier.write("\n#==========BEAMS")
fichier.write("\n#==========\n")

for I, nombre in zip(range(N), data):
          
    
   
    CHAINE= "\n/gate/source/addSource mybeam"+ str(I) + "      " +"gps"
    fichier.write(CHAINE)
    
    
    
    
    CHAINE1="\n/gate/source/mybeam"+str(I)+"/gps/particle     gamma"
    fichier.write(CHAINE1)
    CHAINE2="\n/gate/source/mybeam"+str(I)+"/gps/energy       52. keV"
    fichier.write(CHAINE2)
    CHAINE3="\n/gate/source/mybeam"+str(I)+"/gps/pos/type     Plane"
    fichier.write(CHAINE3)
    CHAINE4="\n/gate/source/mybeam"+str(I)+"/gps/pos/shape    Circle"
    fichier.write(CHAINE4)
    
    x=random.uniform(-6,6)
    y=random.uniform(-6,6)
    chaine="\n/gate/source/mybeam"+ str(I)+"/gps/pos/centre " + f"{x:.{precision}f}"+"  "+ f"{y:.{precision}f}" + " "+ "5. cm"
    fichier.write(chaine)
                                                                                          
                                                                                                         
                                                                                                         
    CHAINE5="\n/gate/source/mybeam"+str(I)+"/gps/pos/radius    30. um"
    fichier.write(CHAINE5)

    CHAINE8="\n/gate/source/mybeam"+str(I)+"/gps/ang/type beam2d"
    fichier.write(CHAINE8)
    
    CHAINE9="\n/gate/source/mybeam"+str(I)+"/gps/ang/sigma_x   1. deg"
    fichier.write(CHAINE9)
    CHAINEE="\n/gate/source/mybeam"+str(I)+"/gps/ang/sigma_y   1. deg"
    fichier.write(CHAINEE)
    CHAINE0= "\n/gate/source/mybeam"+str(I)+"/setIntensity " + "   "+ f"{nombre:.{precision}f}"  
    fichier.write(CHAINE0)
                                                                         
    Tir = 0 
    while(Tir <1):
        Tir=Tir+1
        x=random.uniform(0,0.0001)
        y=random.uniform(0, 0.0001)
        z= 1
        m= sqrt(x*x+y*y+z*z)
        X=x/m
        Y=y/m
        Z=z/m
        M= sqrt(X*X+Y*Y+Z*Z)

        CHAINE7= "\n/gate/source/mybeam"+ str(I) + "/gps/direction    "+f" {X}"+f" {Y}"+ f" {Z}"+"\n"
        fichier.write(CHAINE7)
  
fichier.write("/gate/source/list")
fichier.write("\n#========== Init & Visu")
fichier.write("\n#==========")
fichier.write("\n/vis/disable")
fichier.write("\n#/control/execute mac/visu.mac")
fichier.write("\n#========== START BEAMS")
fichier.write("\n#==========")
fichier.write("\n/gate/random/setEngineName MersenneTwister")
fichier.write("\n/gate/random/setEngineSeed auto")
fichier.write("\n/gate/application/noGlobalOutput")
fichier.write("\n/gate/application/setTotalNumberOfPrimaries 1e7")
fichier.write("\n/gate/application/start")
fichier.close()
