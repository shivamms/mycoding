class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        subdomains = {}
        for cpd in cpdomains:
            split1 = cpd.split(" ")
            visitcount = int(split1[0])
            if split1[1] not in subdomains.keys():
                subdomains[split1[1]] = visitcount
            else:
                subdomains[split1[1]] = subdomains[split1[1]] + visitcount
            dotcount = split1[1].count(".")
            if dotcount == 1:
                split2 = split1[1].split(".")
                if split2[1] not in subdomains.keys():
                    subdomains[split2[1]] = visitcount
                else:
                    subdomains[split2[1]] = subdomains[split2[1]] + visitcount
            elif dotcount == 2:
                split3 = split1[1].split(".",1)
                if split3[1] not in subdomains.keys():
                    subdomains[split3[1]] = visitcount
                else:
                    subdomains[split3[1]] = subdomains[split3[1]] + visitcount
                split4 = split3[1].split(".",1)
                if split4[1] not in subdomains.keys():
                    subdomains[split4[1]] = visitcount
                else:
                    subdomains[split4[1]] = subdomains[split4[1]] + visitcount
        return [str(val) + " " + key for key, val in subdomains.items()]
            