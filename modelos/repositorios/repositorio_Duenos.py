from modelos.entidades.dueno import Dueno
import json

class RepositorioDuenos:
    ruta_archivo = "datos/duenos.json"

    def __init__(self):
        self.__duenos = []
        self.__cargarDuenos()

    def __cargarDuenos(self):
        try:
            with open(RepositorioDuenos.ruta_archivo, "r") as archivo:
                lista_dicc = json.load(archivo)
                for d in lista_dicc:
                    self.__duenos.append(Dueno.fromDiccionario(d))
        except FileNotFoundError:
            print("No se encontró el archivo de dueños")
        except Exception as e:
            print("Error cargando los dueños del archivo.\n" + str(e))

    def __guardarDuenos(self):
        try:
            with open(RepositorioDuenos.ruta_archivo, "w") as archivo:
                lista_dicc = [d.toDiccionario() for d in self.__duenos]
                json.dump(lista_dicc, archivo, indent=4)
        except Exception as e:
            print("Error guardando los dueños en el archivo.\n" + str(e))

    def obtenerDuenos(self):
        return self.__duenos

    def obtenerDuenoPorDNI(self, dni: str):
        for d in self.__duenos:
            if d.obtenerDNI() == dni:
                return d
        return None

    def existeDueno(self, dni: str):
        return self.obtenerDuenoPorDNI(dni) != None

    def agregarDueno(self, dueno: Dueno):
        if self.existeDueno(dueno.obtenerDNI()):
            raise Exception(f"El dueño con DNI {dueno.obtenerDNI()} ya existe")
        self.__duenos.append(dueno)
        self.__guardarDuenos()

    def actualizarDueno(self, dni: str, dueno_nuevo: Dueno):
        """Actualiza los datos (NO se puede modificar el DNI). Retorna True si se actualizó."""
        for i, d in enumerate(self.__duenos):
            if d.obtenerDNI() == dni:
                # no permitimos cambiar el DNI
                if dueno_nuevo.obtenerDNI() != dni:
                    raise Exception("No está permitido modificar el DNI de un dueño")
                self.__duenos[i] = dueno_nuevo
                self.__guardarDuenos()
                return True
        return False

    def eliminarDueno(self, dni: str):
        for i, d in enumerate(self.__duenos):
            if d.obtenerDNI() == dni:
                self.__duenos.pop(i)
                self.__guardarDuenos()
                return True
        return False
