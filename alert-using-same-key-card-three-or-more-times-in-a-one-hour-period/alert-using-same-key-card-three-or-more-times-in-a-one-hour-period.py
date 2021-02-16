class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        usedic = defaultdict(list)
        names = []
        for name, time in zip(keyName, keyTime):
            hour, minutes = time.split(":")
            time = int(hour)*60 + int(minutes) 
            usedic[name].append(time)
        for name, times in usedic.items():
            times.sort()
            length = len(times)
            for i in range(2,length):
                if times[i] <= times[i-2] + 60:
                    names.append(name)
                    break
        return sorted(names)