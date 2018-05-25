# DependencyManager
A helper script to download and extract archives from the web.
From CLI, launch the python script "MxNetDependencies.py" without any arguments. The script assumes presence of "MxNetDependencies.json" 
in current folder. 

Specify dependencies in following form ;
   {
	   "Name":"OpenBlas",	
	   "Url": "https://iweb.dl.sourceforge.net/project/openblas/v0.2.19/OpenBLAS-v0.2.19-Win64-int32.zip",
	   "DownloadToLocation":"C:\\Users\\Administrator\\MyArchives",
	   "ExtractToLocation" :"C:\\Users\\Administrator\\MyExtracts",
	   "Extractor" : "\"C:\\Program Files\\7-zip\\7z.exe\" x {} -o{} -y"
		},
    
   Note-  The path names should be ecnlosed in quotes if path components contain spaces. That explains why "Extractor" value is enquoted.
    ALso, escape back slash characters. 
