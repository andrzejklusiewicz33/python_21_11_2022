def zaokraglij(x):
    def dekorator(fun):
        def wewnetrzna(*args,**kwargs):
            return round(fun(*args,**kwargs),x)
        return wewnetrzna
    return dekorator