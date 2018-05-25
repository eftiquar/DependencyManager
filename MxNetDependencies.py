

import sys , json, traceback, os


def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)

def Extract(extractor,archive,extract_location):
   
    extractCommand = extractor.format(archive, extract_location)
    print("\r\nExtracting {} to \r\n{} \r\n".format(archive,extract_location))
    os.system("\"" + extractCommand + "\"")

def processDependency(url, download_location, extract_location,extractor):
    import wget as w
    if not os.path.exists(download_location):
        os.makedirs(download_location)

    print("\r\nDownloading:\r\n{}\r\n".format(url))
    file = w.download(url,out=download_location )
    escapedFile = "\"" + file + "\""
    print("\r\nDownloaded:\r\n{}\r\n".format(escapedFile))
    Extract( extractor ,escapedFile ,  extract_location )
 
    return file

    
def main():
    print("*****This script expects a JSON input file named \"MxNetDependencies.json\" in current folder. Please specify new dependencies in same form as existing dependencies.****")
    install_and_import('wget')

    try: 
        with open('MxNetDependencies.json') as f:
            dependencies = json.load(f)
            for dep in dependencies['Dependencies']:
                url = dep['Url']
                downloadLocation = dep['DownloadToLocation']
                extractLocation =  dep['ExtractToLocation']
                extractor = dep['Extractor']
                if len(extractor):            
                    processDependency(url,downloadLocation,extractLocation,dep['Extractor'])
   
     
    except Exception as ex:
        errorDescription = "Fatal Error. Exception processing dependencies JSON - {}, Stack Trace - {}".format(ex.message,traceback.format_exc())
        print(errorDescription) 
        return -1

    return 0     
        

if __name__ == "__main__":
    sys.exit(main())

