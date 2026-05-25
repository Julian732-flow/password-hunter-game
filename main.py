import random
import string

# ==========================================
# EXCEPCIONES PERSONALIZADAS
# ==========================================
class LongitudInvalidaError(Exception):
    """Excepción lanzada cuando la longitud es menor a 8."""
    pass

class TipoDatoInvalidoError(Exception):
    """Excepción lanzada cuando la entrada no es un número entero."""
    pass

class ContrasenaInvalidaError(Exception):
    """Excepción lanzada cuando la contraseña no cumple los requisitos de seguridad."""
    pass


# ==========================================
# CLASE: CONTRASEÑA
# ==========================================
class Contrasena:
    CARACTERES_ESPECIALES = "¿¡?=)(/¨*+-%&$#!."

    def __init__(self, longitud: int):
        self.longitud = longitud
        self.valor = ""

    def generar_aleatoria(self):
        """Genera una contraseña aleatoria sin orden predecible."""
        if self.longitud < 8:
            raise LongitudInvalidaError("La longitud mínima debe ser de 8 caracteres.")

        # Asegurar al menos un carácter de cada tipo obligatorio
        mayuscula = random.choice(string.ascii_uppercase)
        minuscula = random.choice(string.ascii_lowercase)
        numero = random.choice(string.digits)
        especial = random.choice(self.CARACTERES_ESPECIALES)

        # Completar el resto de la longitud con caracteres que no se repitan
        pool_restante = (string.ascii_letters + string.digits + self.CARACTERES_ESPECIALES)
        caracteres_usados = {mayuscula, minuscula, numero, especial}
        pool_filtrado = [c for c in pool_restante if c not in caracteres_usados]

        if len(pool_filtrado) < (self.longitud - 4):
            raise ValueError("Longitud excesiva para generar caracteres sin repetir.")

        resto = random.sample(pool_filtrado, self.longitud - 4)
        lista_contrasena = [mayuscula, minuscula, numero, especial] + resto
        random.shuffle(lista_contrasena)
        
        self.valor = "".join(lista_contrasena)
        return self.valor

    def validar(self) -> bool:
        """Valida estrictamente que la contraseña cumpla todas las condiciones."""
        if len(self.valor) < 8:
            return False
        
        if len(self.valor) != len(set(self.valor)):
            return False

        tiene_mayuscula = any(c in string.ascii_uppercase for c in self.valor)
        tiene_minuscula = any(c in string.ascii_lowercase for c in self.valor)
        tiene_numero = any(c in string.digits for c in self.valor)
        tiene_especial = any(c in self.CARACTERES_ESPECIALES for c in self.valor)

        if not (tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_especial):
            raise ContrasenaInvalidaError("La contraseña generada rompió las reglas de seguridad.")
        
        return True

# ==========================================
# CLASES: COFRES (Herencia y Polimorfismo)
# ==========================================
class Cofre:
    def __init__(self, nombre: str, puntos: int):
        self.nombre = nombre
        self.puntos = puntos

    def abrir(self) -> int:
        """Devuelve los puntos otorgados por el cofre."""
        return self.puntos


class CofreComun(Cofre):
    def __init__(self):
        super().__init__("Común", 10)


class CofreRaro(Cofre):
    def __init__(self):
        super().__init__("Raro", 25)


class CofreLegendario(Cofre):
    def __init__(self):
        super().__init__("Legendario", 50)


class CofreMaldito(Cofre):
    def __init__(self):
        super().__init__("Maldito", -20)