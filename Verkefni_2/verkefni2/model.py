from verkefni2 import app

class book:
    def __init__(self,bokalisti):
        self.nafn = bokalisti["nafn"]
        self.utgefandi = bokalisti["utgefandi"]
        self.utgafuar = bokalisti["utgafuar"]
        self.hofundur = bokalisti["hofundur"]
        self.url=bokalisti["url"]
    def nafn(self):
        return self.nafn
    def url(self):
        return self.url
    def lysing(self):
        strengur=self.nafn+" var gefinn út árið "+self.utgafuar+" af "+self.utgefandi+" og var skrifuð af "+self.hofundur
        return strengur

class urlCheck:
    def __init__(self,bokalisti,url):
        self.bokalisti=bokalisti
        self.url=url
    def check(self):
        for x in self.bokalisti:
            if self.url==x.url:
                return x
bokalisti=[book({"nafn":"The Fellowship Of The Ring","utgefandi":"George Allen & Unwin","utgafuar":"1954","hofundur":"J. R. R. Tolkein","url":"The-Fellowship-Of-The-Ring"}),
           book({"nafn":"The Two Towers","utgefandi":"George Allen & Unwin","utgafuar":"1954","hofundur":"J. R. R. Tolkein","url":"The-Two-Towers"}),
           book({"nafn":"Return Of The King","utgefandi":"George Allen & Unwin","utgafuar":"1955","hofundur":"J. R. R. Tolkein","url":"Return-Of-The-King"})]