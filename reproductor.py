from pygame import mixer
class Reproductor:
    #atributos
    archivo = None

    #Constructor
    def __init__(self, archivo):
        self.archivo = archivo
        mixer.init()
        mixer.music.load(archivo)
    
    def play(self):
        mixer.music.play()
        return "Reproduciendo música"
    
    def pause(self):
        mixer.music.pause()
        return "La música se ha pausado"
    
    def unpause(self):
        mixer.music.unpause()
        return "La música está continuando"
    
    def stop(self):
        mixer.music.stop()
        return "La música se detuvo"
    
    def volume(self,v):
        mixer.music.set_volume(v)
        return "volumen a",(100*v), "%"
    
if __name__ == "__main__":
    file = "wefere.mp3"
    musica = Reproductor(file)
    while True:
        print("1- PLAY | 2- PAUSE | 3- STOP | 4- UNPAUSE | 5- VOLUME")
        accion = int(input("Opción: "))
        if(accion == 1):
            resp = musica.play()

        elif(accion == 2):
            resp = musica.pause()

        elif(accion == 3):
            resp = musica.stop()

        elif(accion == 4):
            resp = musica.unpause()

        elif(accion == 5):
            vol = float(input("Vol 0 -- 100"))
            if(vol >= 0 and vol <= 100):
                vol /=100
                resp = musica.volume(vol)

        '''if(accion == 5):
            vol = float(input("Volumen (ingrese un número de 0 a 1: )"))
            resp = musica.volume(vol)
        '''
        
    
        print(resp)