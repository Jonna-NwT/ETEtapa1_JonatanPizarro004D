# ETEtapa1_JonatanPizarro004D

name = Jonatan Pizarro 
seccion = 004D


datos para superuser:
user: caosnew
pass: caosnew

#si no le funciona el superusuario intente crear uno para poder ingresar al admin.

code para bbd: 

CREATE USER C##caosnewwIDENTIFIED BY caosneww;
GRANT CONNECT, RESOURCE TO C##caosneww;
ALTER USER C##caosneww DEFAULT TABLESPACE USERS QUOTA UNLIMITED ON USERS;

y una ultima cosita al modificar el email ta validando que antes tenga caracteres y despues del @ tiene que tener un caracter al menos y luego un punto y luego 2 caracteres almenos. por si le tira error o se cae la pagina.
