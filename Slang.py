#    __
#                      .'  '.
#                  _.-'/  |  \
#     ,        _.-"  ,|  /  0 `-.
#     |\    .-"       `--""-.__.'=====================-,
#     \ '-'`        .___.--._)=========================|
#      \            .'      |                          |
#       |     /,_.-'        |              By:         |
#     _/   _.'(             |          JOSE DONDIS     |
#    /  ,-' \  \            |                          |
#    \  \    `-'            |                          |
#     `-'                   '--------------------------'

#Importamos nuestro sqlite3 Mopri
import sqlite3

#Aqui va a ta la base rey 
conexion = sqlite3.connect ("slangbase.db)")

cursor = conexion.cursor()

# cursor.execute("CREATE TABLE IF NOT EXISTS palabras "\
#     "(palabra VARCHAR(100), significado VARCHAR(100))")

#cursor.execute("INSERT INTO palabras VALUES"\
#    "('mopri', 'Significa: Primo')")

#Para agregar palabras puedes utilizar el siguiente comando "cursor.execute("INSERT INTO palabras VALUES"\
#    "('mopri', 'Significa: Primo')")

#Para utilizar esta aplicacion descarga DB BROWSER FOR SQLITE y arrastra la base de datos "slangbase.db" en la aplicacion de SQLITE


conexion.commit()

#Que xopa, ahora cerramos nuestra conexion de
conexion.close()
