class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        result = collections.Counter()
        for subdomain in cpdomains:
            visitcount, subdomain = subdomain.split()
            visitcount = int(visitcount)
            split = subdomain.split(".")
            length = len(split)
            for i in range(length):
                result[".".join(split[i:])] += visitcount
        return [str(val) + " " + key for key, val in result.items()] 