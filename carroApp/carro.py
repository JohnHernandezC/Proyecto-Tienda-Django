class Carro:
    def __init__(self,request):
        self.request = request
        self.session=request.session
        carro=self.session.get("carro")
        if not carro:
            carro=self.session["carro"]={ }#por si no hay un carro se crea uno con la clave y el valor
        #else:
        self.carro=carro #trae el carro que ya esta almacenado en la session
            
    def agregar(self,producto):
        if (str(producto.id) not in self.carro.keys()):#agregar un nuevo producto al carro
            self.carro[producto.id]={
                "producto_id":producto.id,
                "nombre":str(producto.nombrep),
                "precio":producto.precio,
                "cantidad":1,
                "imagen": producto.imagen.url
            }
        else:
            for key, value in self.carro.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]+1
                    value["precio"]=float(value["precio"]+producto.precio)
                    break
        self.guardar_carro()
        
    def guardar_carro(self):
      self.session["carro"]=self.carro
      self.session.modified=True
    
    def eliminacion(self,producto):
      producto.id=str(producto.id)
      if producto.id in self.carro:
        del self.carro[producto.id]#
        self.guardar_carro()
        
    def restar_unidades(self, producto):
        for key, value in self.carro.items():
            if key==str(producto.id):
                value["cantidad"]=value["cantidad"]-1
                value["precio"]=float(value["precio"]-producto.precio)
                if value["cantidad"]<1:
                    self.eliminacion(producto)
                break
        self.guardar_carro()
    
    def limpiarCarro(self):
        self.session["carro"]={}
        self.session.modified=True

    