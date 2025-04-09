# TuProyectoFinal+RodriguezA
Python Comisión 75140

Alumno: Andres Rodriguez

## De qué se trata el proyecto

Este proyecto consiste en un blog donde cada programador pueden compartir su historia, la cual puede clasificar en categorias. tambien puede leer las historias de las demas y filtrarlas a traves de una barra de busqueda

## Cómo ejecutarlo

para ejecutarlo deberas activar el entorno virtual .venv/Scripts/activate
el cual debes crear con el comando: python -m virtualenv .venv

- la unica dependencia que utilice fue Django instalada a traves del comando pip install django

EXTRA
django admin super user
nombre: admin
clave: 123

la base de datos ya esta comentada, es decir, subida a github

## Características

1. mi proyecto cuenta con dos aplicaciones: historia y core

2. utilice estilos bootstrap para los html

3. tengo un archivo base, donde se fijaron los componentes(navbar y footer) y con un block content se crearon las paginas, los componentes se agregaron con include al archivo base.html

4. puse en practica lo de la carpeta static ya que ahi se almacenan los estilos y una foto utilizada en el about. no puse link externo a linkedin, ya que no tengo. pero mi footer tiene un link que te lleva a la pagina de coderhouse argentina 

5. implemente una barra de busqueda, la cual funciona por nombres

## Mejoras a futuro

1. agregar un login 

2.agregar un logout, no lo pude hacer por falta de tiempo

3. me gustaria dar mi propio estilo a la pagina creando mi archivo css

4. agregar un sitio de consultas a la pagina

5. permitir que los usuarios den like a las historias

6. hacer las pruebas en una rama de prueba, no en un repositorio aparte, como en este caso