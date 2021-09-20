class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def keys(log):
            key, content = log.split(' ', maxsplit=1)
            return (0,content,key) if content[0].isalpha() else (1,)
        
        return sorted(logs, key=keys)