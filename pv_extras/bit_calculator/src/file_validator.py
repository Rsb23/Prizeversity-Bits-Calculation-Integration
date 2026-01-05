import magic


class FileValidator():
    def testFile(self, file: str | bytes, fromFile: bool = False) -> str:
        if fromFile:
            return magic.from_file(file, mime=True)
        else:
            return magic.from_buffer(file, mime=True)
    
    def isCSVFile(self, filepath: str, fromFile: bool = False) -> bool:
        res = self.testFile(filepath, fromFile)

        # MIME type references
        #   https://www.rfc-editor.org/rfc/rfc4180
        #   https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/MIME_types/Common_types
        if res == 'text/csv' or res == 'application/csv':
            return True
        else:
            return False