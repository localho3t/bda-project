import os

class UtilsHelper:

    @staticmethod
    def file_exists(path):
        if os.path.exists(path):
            return True
        print("[!] path Error")
        return False