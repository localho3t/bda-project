from helpers.utils import UtilsHelper
import mimetypes
import pandas as pd

class ReadFile:
    
    
    def __init__(self) :
        self.version = "v0.1"

    def read_csv(self):
        pass

    def check_type_file(self):
        try:
            if UtilsHelper.file_exists(self.path):
                mime_type, _ = mimetypes.guess_type(self.path)

                if mime_type:
                    return mime_type
                else:
                    return "[!] Error Type ..."
        except:
            print("[!] not define")
            
    def set_file_path(self,path):
        if UtilsHelper.file_exists(path):
            self.path = path

    def get_file_path(self):
        try:
            return self.path
        except:
            print("[!] not define")