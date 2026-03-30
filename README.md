# Práctica 1: Particiones de Equivalencia con Pytest

Este proyecto implementa funciones en Python y sus respectivas pruebas unitarias utilizando la técnica de **Particiones de Equivalencia (PE)**. El objetivo es validar rangos de datos y el manejo de excepciones.

## Instalación y configuración del entorno

Las siguientes instrucciones están diseñadas exclusivamente para **Linux Ubuntu** y estan a forma de _copy paste_, así que solo es necesario que abra su terminal y siga los pasos a continuación:

1. Descargue MiniConda usando instalador oficial:
   ```bash
   wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
   ```
2. Una vez termine la descarga, debera ejecutar el script de instalación:
   ```bash
   bash Miniconda3-latest-Linux-x86_64.sh
   ```
3. Actualice su terminal para reconocer el comando:
   ```bash
   source ~/.bashrc
   ```
4. Se debe crear el entorno virtual dedicado para la materia:
   ```bash
   conda create -n TPS python=3.10 -y
   ```
5. Activamos y accedemos al entorno que hemos creado
   ```bash
    conda activate TPS
   ```
   A continuación se muestra una imagen de como como debe verse tu terminal para este momento. Si tiene el entorno (TPS) a su izquierda, podemos   continuar.

   <div align="center">
       <img width="427" height="55" alt="image" src="https://github.com/user-attachments/assets/a1465598-2072-49a5-a3d5-10accd689af6" />
   </div>
   
6. Con el entorno TPS activo, instale las herramientas de prueba:
   ```bash
    conda install pytest
   ```
   
## Descarga del proyecto y ejecución

Una vez que el entorno **TPS** esté configurado y activo, siga estos pasos para obtener el código y validar las funciones.

1. Clonaremos el repositorio para descargar el proyecto en su máquina local y ejecutar las pruebas:
   ```bash
   git clone git@github.com:7mo-TecnicasPruebasSoftware/Practica1_ParticionesEquivalencia.git
   ```

2. Asegúrese de que su directorio se vea de la siguiente forma antes de ejecutar las pruebas. La separación entre el código fuente y tests es vital para las buenas prácticas de ingeniería de software:
   ```
   practica1
   ├── src/
   │   ├── __init__.py
   │   ├── calcular_temperatura.py
   │   └── clasificar_calificacion.py
   └── tests/
       ├── __init__.py
       ├── test_calcular_temperatura.py
       └── test_clasificar_calificacion.py
   ```

3. Para ejecutar las pruebas y verificar las Particiones de Equivalencia, utilice el módulo pytest.
   
   __Importante: Ejecute el comando desde la raíz del proyecto para que Python localice correctamente los módulos.__
   ```
   python -m pytest -v
   ```

5. ¿Qué esperar de los resultados?
   Al ejecutar el comando anterior, la terminal deberá mostrar un listado de los casos de prueba. Cada uno representa una partición (Válida o Inválida):
   * __PASSED:__ Indica que la función retornó el valor esperado o lanzó la excepción correcta (ValueError o TypeError).
   * __FAILED:__ Indica un error en la lógica de la función o en la expectativa del test.
  
## Análisis de Particiones de Equivalencia

Para el diseño de las pruebas, se dividieron los datos de entrada en grupos lógicos para garantizar la cobertura total de la especificación.

### Problema 1: Cálculo de Temperatura
### Tabla de Particiones de Equivalencia: `calcular_temperatura`

<div align="center">
    
| Clase de Equivalencia | Rango / Valor de Prueba | Resultado Esperado | Tipo de Partición |
| :--- | :--- | :--- | :--- |
| **Temperatura Fría** | $-273 \le x \le 15$ | `"Frío"` | Válida |
| **Temperatura Templada**| $16 \le x \le 25$ | `"Templado"` | Válida |
| **Temperatura Caliente** | $26 \le x \le 10,000$ | `"Caliente"` | Válida |
| **Error Rango Menor** | $-274$ | `ValueError` | Inválida |
| **Error Rango Mayor** | $10,001$ | `ValueError` | Inválida |
| **Tipo de dato erróneo** | `"calorcito"` | `TypeError` | Inválida |

</div>

### Problema 2: Clasificación de Calificación
### Tabla de Particiones de Equivalencia: `clasificar_calificacion`

<div align="center">

| Clase de Equivalencia | Rango / Valor | Resultado Esperado | Tipo |
| :--- | :--- | :--- | :--- |
| **Reprobado** | $[0, 5.9]$ | "Reprobado" | Válida |
| **Aprobado** | $[6, 8]$ | "Aprobado" | Válida |
| **Sobresaliente** | $[9, 10]$ | "Sobresaliente" | Válida |
| **Nota Inválida** | $x < 0$ o $x > 10$ | `ValueError` | Inválida |
| **Entrada no numérica** | "Diez" | `TypeError` | Inválida |

</div>


