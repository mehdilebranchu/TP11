class duree:
    def __init__(self,h,m,s):
        self.__h =h
        self.__m =m
        self.__s=s
    def __add__(self, other):
        h=self.__h + other.__h
        m=self.__m + other.__m
        s=self.__s + other.__s
        if s >= 60 :
            m+=1
            s = s - 60

        if m >= 60 :
            h+=1
            m = m - 60
        return duree(h,m,s)

    def __str__(self):
        return 'duree :'+str(self.__h)+' h '+str(self.__m)+' min '+str(self.__s)+' sec'
if __name__ == "__main__":
    d1 = duree(1,26,54)
    d2 = duree(2,34,2)
    d3 = d1+d2
    print(d3)
