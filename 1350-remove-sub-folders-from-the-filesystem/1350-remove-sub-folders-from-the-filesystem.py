class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        folders.sort()
        
        result = []
        last = ""  # the last top-level folder we kept
        
        for folder in folders:
            # If `folder` is NOT under `last`, keep it:
            # either last == "" (first iteration)
            # or folder doesn't start with last + "/"
            if not last or not folder.startswith(last + "/"):
                result.append(folder)
                last = folder
        
        return result
        