# DependencyManager
A helper script to download and extract archives from the web.
From CLI, launch the python script "MxNetDependencies.py" without any arguments. The script assumes presence of "MxNetDependencies.json" 
in current folder. 

Specify dependencies in following form:


   {  
   
   	   "Name":"OpenBlas",	
	   "Url": "https://iweb.dl.sourceforge.net/project/openblas/v0.2.19/OpenBLAS-v0.2.19-Win64-int32.zip",
	   "DownloadToLocation":"C:\\Users\\Administrator\\MyArchives",
	   "ExtractToLocation" :"C:\\Users\\Administrator\\MyExtracts",
	   "Extractor" : "\"C:\\Program Files\\7-zip\\7z.exe\" x {} -o{} -y"
	   
   },
    
   Note-  The path names should be ecnlosed in quotes if path components contain spaces. That explains why "Extractor" value is enquoted.
   Also, escape back slash characters. 
   
# Manual steps 

A. Install visual studio 2015. community edition -
  1. Sign up for Visual Studio Dev Essentials - https://www.visualstudio.com/dev-essentials/
  2. From downloads tab, choose "Visual Studio Community 2015 with Update 3"
  3. Run installer

B. Download GIT
   1. Download URL https://gitforwindows.org/
   2.Install. Choose default options on each screen.

C. Clone mxnet
    1. Launch git bash, mkdir "Work"
    2. git clone https://github.com/apache/incubator-mxnet.git mxnet
    3. cd mxnet
    4. git submodule update --init --recursive

D. Install cmake
   1. Download - https://cmake.org/files/v3.11/cmake-3.11.1-win64-x64.msi
   2. Install. Choose "Add cmake to the path for current user"

E. Install dependencies

    A MinGW
        1. Download URL https://sourceforge.net/projects/mingw-w64/files/latest/download?source=typ_redirect
        2. Install.
            Choose Architecture as "x86_64"
            Choose threads as "win32"
            Choose exception as "seh" ( SEH -  structured exception handling, windows native mechanism which underlies exception handling support in C++)
        3. Default location where to find relevant binaries -  C:\Program Files\mingw-w64\x86_64-7.3.0-win32-seh-rt_v5-rev0\mingw64\bin
    B Open Blas
        1. https://iweb.dl.sourceforge.net/project/openblas/v0.2.19/OpenBLAS-v0.2.19-Win64-int32.zip
        2. Find the zip file in the downloads folder
    C Open CV
        1. Download URL - https://phoenixnap.dl.sourceforge.net/project/opencvlibrary/opencv-win/3.4.1/opencv-3.4.1-vc14_vc15.exe


F. Build Mxnet library

   Configure dependencies
   
   1. create a folder called "ThirdParty" under "Work" folder created above. ( typically C:\Users\Administrator\Work)
   2. Create a temp folder under "work" "C:\Users\Administrator\Work\temp"

    Setup Copy OpenBlas
        1. Extract "OpenBLAS-v0.2.19-Win64-int32.zip" under temp folder
        2. Find a folder "OpenBLAS-v0.2.19-Win64-int32" in the extracted items
        3. Copy the contents of this folder to   C:\Users\Administrator\Work\ThirdParty\OpenBlas

    Setup OpenCV
        1. Extract "opencv-3.4.1-vc14_vc15.exe" under the temp folder
        2. Copy the OpenCV folder to C:\Users\Administrator\Work\ThirdParty

 G. Build Command
 
 
        1. Start "VS2015 x64 Native Tools Command Prompt" from the start menu
        2. cd    "C:\Users\Administrator\Work\MxNet"
        3. cmake CMakeLists.txt -DOpenBLAS_INCLUDE_DIR=C:\Users\Administrator\Work\ThirdParty\OpenBLAS\include -   DOpenBLAS_LIB=C:\Users\Administrator\Work\ThirdParty\OpenBLAS\lib\libopenblas.dll.a -DOpenCV_DIR=C:\Users\Administrator\Work\ThirdParty\opencv\build  -DUSE_CUDA=OFF -G "Visual Studio 14 2015 Win64"
        4. devenv mxnet.sln /build "Release|x64"  /project ALL_BUILD.vcxpro
