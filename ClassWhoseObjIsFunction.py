class Product:
    def __call__(self,a,b):
        self.a=a
        self.b= b
        print(self.a*self.b)
ans=Product()
ans(10,20)


