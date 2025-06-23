# 🐍 Juego de Snake

## Descripción General

Este proyecto consiste en la implementación del clásico juego **Snake** utilizando el lenguaje de programación **Python** y la biblioteca gráfica estándar **`tkinter`**. El objetivo del juego es controlar una serpiente que debe comer comida aparecida aleatoriamente en el tablero, evitando colisionar con sus propios segmentos o los bordes del área de juego.

El diseño del programa se ha realizado completamente desde cero, sin depender de librerías externas.

---

## 🧩 Funcionalidades Implementadas

- Movimiento continuo de la serpiente por medio de las teclas de dirección del teclado.
- Generación aleatoria de comida en posiciones válidas (fuera del cuerpo de la serpiente).
- Crecimiento de la serpiente al consumir comida.
- Incremento progresivo de la velocidad del juego a medida que la serpiente crece.
- Detección automática de colisiones contra los bordes y contra sí misma.
- Sistema de puntuación en tiempo real.

---

## 📦 Requisitos del Sistema

- **Lenguaje**: Python 3.x
- **Librería Gráfica**: `tkinter` (incluida por defecto en instalaciones estándar de Python)

No se requiere instalación adicional de dependencias.

---

## ▶️ Instrucciones de Uso

1. Asegúrate de tener instalado Python 3.x en tu sistema.
2. Descarga o clona el repositorio que contiene el archivo principal: `snake_game.py`.
3. Abre una terminal o consola y navega hasta la carpeta donde se encuentra el archivo.
4. Ejecuta el juego con el siguiente comando:

```bash
python snake_game.py
```

5. Usa las **flechas del teclado** para controlar la serpiente.
6. El juego termina cuando la serpiente choca contra los bordes o contra su propio cuerpo, mostrando el mensaje **"Game Over"**.

---

## 🎮 Controles

| Tecla         | Acción               |
|---------------|----------------------|
| ⬆️ Flecha Arriba   | Mover hacia arriba     |
| ⬇️ Flecha Abajo    | Mover hacia abajo      |
| ⬅️ Flecha Izquierda| Mover hacia la izquierda|
| ➡️ Flecha Derecha  | Mover hacia la derecha |

---

## 📄 Estructura del Código

El código está organizado en funciones claras y modulares:

- **Variables globales**: Almacenan el estado del juego (serpiente, comida, puntuación, dirección).
- **Funciones principales**:
  - `place_food()`: Genera comida en una posición válida.
  - `create_objects()`: Dibuja los elementos del juego en el lienzo.
  - `change_direction()`: Maneja la entrada del usuario para cambiar la dirección.
  - `move_snake()`: Lógica central del movimiento y detección de eventos.
  - `check_collision()`: Detecta si ocurre una colisión.

---

## 🔒 Consideraciones de Seguridad y Licencia

Este proyecto no hace uso de recursos externos ni conexiones a Internet. Todo el código es de elaboración propia y puede ser utilizado libremente con fines académicos o educativos.

**Licencia**: MIT License (ver detalles en el archivo `LICENSE`, si lo incluyes).

---

## 📝 Notas Finales

Este proyecto cumple con los objetivos de aprendizaje relacionados con manejo de eventos, estructuras de datos, interfaces gráficas sencillas y lógica de videojuegos. Es ideal como base para futuras mejoras como la integración de inteligencia artificial, guardado de puntajes altos o modo multijugador.
