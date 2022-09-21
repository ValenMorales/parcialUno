class Solucion:
    def __init__(self):
        self.estructura={
            "serie": "",
            "number_seasons": 0,
            "original_lenguage":"",
            "features_seasons":[{
            "season_number": 0,
            "season_name": "",
            "premier_date":"" ,
            "cast": [],
            "episodes": [{
            "episode_name": "",
            "time_duration": ""

            }]
        }] }


    def llenar_estructura(self):
        self.estructura["serie"]= input("ingresa el nombre de la serie ")
        numTemporadas=int(input("cuantas temporadas tiene? "))
        self.estructura["number_seasons"]= numTemporadas
        self.estructura["original_lenguage"]= input("lenguaje orignal: ")
        for i in range(numTemporadas):
            self.estructura["features_seasons"][0][0]= input("numero de la temporada ")
            self.estructura["features_seasons"][0][1]= input("nombre")
            self.estructura["features_seasons"][0][2]= input("fecha premier")
            numero= int(input("Cuantas personas forman parte del elenco?"))
            print("ingresa cada persona del elenco")
            lista_elenco= []
            for i in range(numero):
                nombre= input(i+1)
                lista_elenco.append(nombre)
            self.estructura["features_seasons"][0][3]= lista_elenco
            self.estructura["features_seasons"][0]["episodes"][0]["episode_name"]= input("nombre del episodio")
            self.estructura["features_seasons"][0]["episodes"][0]= input("tiempo de duracion del episodio")


    def buscar_actor(self, nombre):
        for i in self.estructura["features_seasons"][0][3]:
            if i==nombre:
                return self.estructura["serie"]
'''
    def buscar_fecha(self, fecha):
        if self.estructura["features_seasons"][0][2]== fecha

'''