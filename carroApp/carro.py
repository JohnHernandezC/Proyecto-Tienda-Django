class carro():
    def __init__(self,request):
        self.request = request
        self.session=request.session
        carro= self.session.get('carro')
        if not carro:
            carro=self.session["carro"]={}#por si no hay un carro se crea uno con la clave y el valor