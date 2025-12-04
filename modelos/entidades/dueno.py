class Dueno:
    @classmethod
    def fromDiccionario(cls, diccionario: dict):
        # Espera claves: dni, nombre, apellido, animal_favorito
        return cls(diccionario["dni"], diccionario["nombre"], diccionario["apellido"], diccionario.get("animal_favorito"))

    def __init__(self, dni: str, nombre: str, apellido: str, animal_favorito: str = None):
        if not isinstance(dni, str) or not dni.isdigit() or dni.strip() == "":
            raise ValueError("El DNI debe ser un string de dígitos no vacío")
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre debe ser un string no vacío")
        if not isinstance(apellido, str) or not apellido.strip():
            raise ValueError("El apellido debe ser un string no vacío")
        if animal_favorito is not None and (not isinstance(animal_favorito, str) or not animal_favorito.strip()):
            raise ValueError("El animal favorito debe ser un string no vacío o None")

        self._dni = dni
        self._nombre = nombre
        self._apellido = apellido
        self._animal_favorito = animal_favorito

    def obtenerDNI(self):
        return self._dni

    def obtenerNombre(self):
        return self._nombre

    def obtenerApellido(self):
        return self._apellido

    def obtenerAnimalFavorito(self):
        return self._animal_favorito

    def establecerNombre(self, nombre: str):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre debe ser un string no vacío")
        self._nombre = nombre

    def establecerApellido(self, apellido: str):
        if not isinstance(apellido, str) or not apellido.strip():
            raise ValueError("El apellido debe ser un string no vacío")
        self._apellido = apellido

    def establecerAnimalFavorito(self, animal_favorito: str):
        if animal_favorito is not None and (not isinstance(animal_favorito, str) or not animal_favorito.strip()):
            raise ValueError("El animal favorito debe ser un string no vacío o None")
        self._animal_favorito = animal_favorito

    def toDiccionario(self):
        return {
            "dni": self._dni,
            "nombre": self._nombre,
            "apellido": self._apellido,
            "animal_favorito": self._animal_favorito
        }
