"""Sistema de Gestión Académica - Innovatec Education."""

NOTA_MINIMA = 10.5


def calcular_promedio(notas):
    """Devuelve el promedio de una lista de notas (de 0 a 20)."""
    if not notas:
        raise ValueError("Debe ingresar al menos una nota")
    for nota in notas:
        if nota < 0 or nota > 20:
            raise ValueError(f"Nota inválida: {nota}")
    return round(sum(notas) / len(notas), 2)


def obtener_estado(promedio):
    """Indica si el alumno aprobó o desaprobó."""
    if promedio >= NOTA_MINIMA:
        return "APROBADO"
    return "DESAPROBADO"


def generar_reporte(alumnos):
    """Crea una línea de reporte por cada alumno."""
    reporte = []
    for nombre, notas in alumnos.items():
        promedio = calcular_promedio(notas)
        estado = obtener_estado(promedio)
        reporte.append(f"{nombre:<8} | Promedio: {promedio:>5} | {estado}")
    return reporte


if __name__ == "__main__":
    alumnos = {
        "Ana": [15, 17, 14],
        "Luis": [8, 10, 9],
        "María": [18, 19, 20],
    }
    print("=" * 45)
    print("  SISTEMA DE GESTIÓN ACADÉMICA - INNOVATEC")
    print("=" * 45)
    for linea in generar_reporte(alumnos):
        print(linea)