from abaqus import *
from abaqusConstants import *
import os
import job

folder_path = r"E:\ABAQUS study\paramodle\linkage_opti\140_457"

for file in os.listdir(folder_path):
    if file.endswith(".inp"):
        file_name = os.path.splitext(file)[0]
	jobName=file_name
    mdb.JobFromInputFile(name=jobName, inputFileName=jobName + '.inp',
        numCpus = 4, numDomains = 4)
    mdb.jobs[jobName].submit()
    mdb.jobs[jobName].waitForCompletion()
