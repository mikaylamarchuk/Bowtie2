import os as os
import glob as glob

#change input and output directory paths
Client = "EB"
genomeName = "hg-rRNA-IGenome"
inputdirectory = "/media/data/NovaSEQ_Runs/200317_A00639_0230_BHKLVYDRXX/Unaligned_NovaRS-21-FC01/"
outputdirectory = f"/media/data/NovaSEQ_Runs/200317_A00639_0230_BHKLVYDRXX/Bowtie2-RS-{Client}-RS24-{genomeName}/"
threads = "6" 

files = glob.glob(inputdirectory + "RS*.fastq.gz") 
files.sort()

for file in files:
	if Client in file:
		if "_R1_001" in file:
			file2 = file.replace("R1_001", "R2_001")
			stripped_file = file.replace(inputdirectory, "")
			head, sep, tail = stripped_file.partition('_S')
			sam = head + ".sam"
			log = head + ".log"
			print("nohup bowtie2 -x " + genomeName + " -1 " + file + " -2 " + file2 + " -S " + outputdirectory + sam + " 2> " + outputdirectory + log + " -p " + threads + " ; ")




