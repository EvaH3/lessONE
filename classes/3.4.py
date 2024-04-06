class trans():

    def __init__(self, s, s1):
        self.s = s
        self.s1 = s1

    def tte(self):
        dic = {"а":"a","б":"b","в":"v","г":"g","д":"d","е":"e","ж":"j","з":"z","и":"i","й":"y","к":"k","л":"l","м":"m","н":"n","о":"o","п":"p","р":"r","с":"s","т":"t","у":"u","ф":"f","х":"h","ц":"ts","ч":"ch","ш":"sh","щ":"sh","ъ":"","ы":"","ь":"","ю":"yi","я" : "ya"," ":"-"}
        self.s = self.s.lower()
        for i in range (len(self.s)):
            self.s1 = self.s1 + dic.get(self.s[i])
        return (self.s1)


f = open('xyz.txt', 'w')
s = input()
while s != '':
    a = trans(s, '')
    b=a.tte()
    print(b)
    f.write(b)
    f.write('\n')
    s = input()