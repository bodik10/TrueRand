class TrueRandom():
    def __init__(self):
        self.url = "www.random.org"
        self.services = ["integers", "sequences", "strings", "quota"]

    def __getattr__(self, attrname):
        if attrname in self.services:
            return lambda **x: self.request(service=attrname, **x)
        else:
            raise AttributeError

    def request(self, service, **args):
        from urllib.request import urlopen, Request
        from urllib.parse import urlencode, urlunsplit
        from urllib.error import HTTPError, URLError # HTTPError if 503 request, URLError if timed out
        
        data = urlencode(args)
        url = urlunsplit(['https', self.url, service, data, ''])
        if service != 'quota': self.checkQuota()
        try:
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'}) # prevent 'HTTP Error 403: Forbidden'
            res = urlopen(req, timeout=60)
            seq = res.read().decode()
        except HTTPError as error: # service returns 503 code (Service Unavailable)
            seq = error.read().decode()
        except URLError as error:  # timed out (missing or slow internet connection)
            seq = "Error: Timed out\nService may be out of work temporary\nTry again later\nAlso try to check your internet connection"
        else:
            res.close()
        return self.split(seq, args.get('num', None))

    def split(self, seq, n):
        import re
        if re.search("^Error", seq):
            raise Exception(seq)
        L = re.split("\n", seq[:-1])
        if n is not None and len(L) != int(n):
            raise Exception ("Error: Unexpected result was returned")
        else:
            return L

    def checkQuota(self):
        self.quota_left = int(self.quota(format='plain')[0])
        if self.quota_left <= 0:
            raise Exception ("Error: You're out of your quota.\nTry again later or increase the quota for your IP at random.org")
        

import random

def all_possibles_combinations(n, s):
    if type(n) is not int: return
    eval_code = "[''.join((%s))%s]" % (",".join(["i%s" % i for i in range(1,n+1)]),             # (a,b,c)
                                       "".join([" for i%s in s" % i for i in range(1,n+1)]))    # for a in s for b in s for c in s
    
    return eval(eval_code, {"s":s})

class PseudoRandom:
    def __init__(self):
        self.len = len
        
    def baseconv(self, data, base): # converts list of numbers to another base
        bases = {'2': bin, '8': oct, '16': hex}
        return list(map(lambda x: bases[base](x)[2:], data)) # lambda for remove '0b' from '0b110011'
        
    def integers(self, num, min, max, base='10', **args):
        assert max > min, "Error: The maximum value must be greater than the minimum value"
        res = [random.randint(min, max) for i in range(num)]
        if base != '10':
            return self.baseconv(res, base)
        return res

    def sequences(self, min, max, **args):
        assert max > min, "Error: The maximum value must be greater than the minimum value"
        res = list(range(min, max+1))
        random.shuffle(res)
        return res

    def strings(self, num, len, digits, upperalpha, loweralpha, unique, **args):
        import string
        s = ""
        if digits == upperalpha == loweralpha == 'off':
            raise Exception ("Error: Not enough parameters")
        if digits == 'on':      s += string.digits
        if upperalpha == 'on':  s += string.ascii_uppercase
        if loweralpha == 'on':  s += string.ascii_lowercase


        if unique == 'on':
            all = self.len(s) ** len
            res=[]
            
            if num > all:
                raise Exception ("Error: you requested %s unique strings, but there are only %s possible strings with the parameters you have chosen" % (num, self.len(s) ** len))

            if all > 100000:
                while self.len(res) < num:
                    comb = "".join([s[random.randint(0, self.len(s)-1)] for i in range(len)])
                    if comb not in res:
                        res.append(comb)
                return res
  
            all_comb = all_possibles_combinations(len, s)
            
            if self.len(all_comb) == num:
                return all_comb
            if num < all/2:
                while self.len(res) < num:
                    res.append(all_comb.pop(random.randint(0, self.len(all_comb)-1))) # random GET from all_comb if num LESS than a half of all
            else:
                res = all_comb
                while self.len(res) != num:
                    res.pop(random.randint(0, self.len(res)-1)) # random POP from all_comb and return it if num LESS than a half of all
            return res

       
        return ["".join([s[random.randint(0, self.len(s)-1)] for i in range(len)]) for j in range(num)]

    def quota(self, format): return "---"
    
if __name__ == '__main__':
    r1 = TrueRandom()
    print(
        r1.integers(num=10, min=1, max=20, col=1, base=10, format='plain', rnd='new'),
        r1.integers(num=1, min=1, max=105, col=1, base=10, format='plain', rnd='new'),
        r1.sequences(min=1, max=20, col=1, format='plain', rnd='new'),
        r1.strings(num=10, len=10, digits='on', upperalpha='on', loweralpha='on', format='plain', rnd='new'),
        r1.strings(num=3, len=8, digits='on', upperalpha='off', loweralpha='off', format='plain', rnd='new'),
        r1.quota(format='plain'),
    sep="\n")

    r2 = PseudoRandom()
    print(
        r2.integers(num=10, min=1, max=10, base='10', format='plain', rnd='new'),
        r2.integers(num=1, min=1, max=100, base='10', format='plain', rnd='new'),
        r2.integers(num=20, min=1, max=100, base='16'),

        r2.sequences(min=10, max=15),

        r2.strings(num=10, len=8, digits='on', upperalpha='on', loweralpha='on', unique='off'),
    sep="\n")
    

