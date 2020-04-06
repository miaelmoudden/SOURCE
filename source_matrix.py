import random
import numpy as np
from scipy.stats import *
multivariate_normal
import matplotlib.pyplot as plt



data = np.random.randn(100) * sigma + mu


Tir = 0
while (Tir < 100): 
    Tir=Tir+1
    z= random.uniform(0.9,1)
 

m= np.array([0,0])
v = np.eye(2)*4
mu = 10
sigma = 2.0
rvs = multivariate_normal(mean=m, cov=v)
tirages = rvs.rvs(100)

fichier = open("test3.mac", "w")
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
fichier.write("\n/gate/Detector/placement/setTranslation 	0 0 -25 cm")
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

 
    
for I in range(np.shape(tirages)[0]):
     for nombre in data:

    
        CHAINE= "\n/gate/source/addSource mybeam"+ str(I) + "   " +"gps\n"
        fichier.write(CHAINE)
        CHAINE1= "\n/gate/source/mybeam"+ str(I) + "/gps/particle   gamma"
        fichier.write(CHAINE1)
   
        CHAINE0= "\n/gate/source/mybeam"+str(I)+"/setIntensity " + "  "+ str(nombre)
        fichier.write(CHAINE0)
      
           
        CHAINE7= "\n/gate/source/mybeam"+ str(I) + "/gps/direction    0 0 "+ str(z)
        fichier.write(CHAINE7)
        
    
        CHAINE2= "\n/gate/source/mybeam"+ str(I) + "/gps/energy   40. keV"
        fichier.write(CHAINE2)
        CHAINE3= "\n/gate/source/mybeam"+ str(I) + "/gps/pos/type   Plane"
        fichier.write(CHAINE3)
        CHAINE4= "\n/gate/source/mybeam"+ str(I) + "/gps/pos/shape   Rectangle"
        fichier.write(CHAINE4)
        chaine="\n/gate/source/mybeam"+str(I)+"/gps/pos/centre " + str( tirages[I,0]) +" "+ str(tirages[I,1]) + " "+ "20 cm"
        fichier.write(chaine)
        CHAINE5= "\n/gate/source/mybeam"+ str(I) + "/gps/pos/halfx    1.5 mm"
        fichier.write(CHAINE5)
        CHAINE6= "\n/gate/source/mybeam"+ str(I) + "/gps/pos/halfy    1.5 mm"
        fichier.write(CHAINE6)
    
    
        CHAINE8= "\n/gate/source/mybeam"+ str(I) + "/gps/ang/type beam2d"
        fichier.write(CHAINE8)
        CHAINE9= "\n/gate/source/mybeam"+ str(I) + "/gps/ang/sigma_x   1. deg"
        fichier.write(CHAINE9)
        CHAINE10= "\n/gate/source/mybeam"+ str(I) + "/gps/ang/sigma_y   1. deg"
        fichier.write(CHAINE10)    
        
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
