TUTORIAL
========

Se asume que estan en un sistema operativo Debian-like (Debian, Ubuntu, Mint, etc).

Y que son usuarios root.

**1)**
Lo primero y ciertamente una de las cosas mas importantes es revisar el archivo (/etc/apt/sources.list) donde estan las fuentes de todos los repositorios del sistema operativo, si estan en un Debian 7 "Wheezy" ese archivo deberia tener algo como esto:

```
deb http://http.debian.net/debian wheezy main
deb-src http://http.debian.net/debian wheezy main

deb http://http.debian.net/debian wheezy-updates main
deb-src http://http.debian.net/debian wheezy-updates main

deb http://security.debian.org/ wheezy/updates main
deb-src http://security.debian.org/ wheezy/updates main
```

**2)**
Actualizar la lista de repositorios con:

`aptitude update`

**3)**
Lo siguiente es instalar las cosas necesarias para el proyecto, que son basicamente python, flask, psycopg2 y postgres. Para eso:

`aptitude install python python-dev python-pip postgresql-9.1 postgresql-client-9.1 libpq-dev`

Los tres primeros instalan el interprete de python, las dependencias necesarias para compilar los paquetes de python y el manejador de paquetes de python pip.

Las dos siguientes instalan un servidor de postgres y un cliente para conectarnos.

La ultima instala unas dependencias necesarias para el psycopg2.

**4)**
Instalamos flask y psycopg2:

`pip install flask psycopg2`

**5)**
Finalmente para configurar una base de datos en postgres, primero debemos cambiarnos al usuario postgres, conectarnos al servidor, crear la base de datos, crear un usuario con permisos sobre esa base de datos y despues podemos conectarnos con ese usuario y crear tablas etc, como ejemplo:

```
su postgres
psql
create database ati_database;
create user ati with password 'ati';
grant all privileges on database ati_database to ati;
\q
psql -U ati -W -d ati_database -h localhost
...
```


**EXITO!**
