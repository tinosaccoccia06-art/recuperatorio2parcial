from modelos.repositorios.repositorio_animales import RepositorioAnimales
from modelos.repositorios.repositorio_duenos import RepositorioDuenos

_animales = None
_duenos = None

def obtenerRepoAnimales():
    global _animales
    if _animales is None:
        _animales = RepositorioAnimales()
    return _animales

def obtenerRepoDuenos():
    global _duenos
    if _duenos is None:
        _duenos = RepositorioDuenos()
    return _duenos

