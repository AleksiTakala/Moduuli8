import mysql.connector


def icaokoodi(idd):
        sql = "SELECT ident, name, municipality from airport"
        sql += " WHERE ident ='" + idd + "'"
        print(sql)
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
        if kursori.rowcount > 0:
                for rivi in tulos:
                        print({rivi[1]}, {rivi[2]})
        return


yhteys = mysql.connector.connect(
        host = '127.0.0.1',
        port = 3306,
        database = 'flight_game',
        user = 'root',
        password = 'miten',
        autocommit = True
    )

id = input('Anna ICAO koodi ')
icaokoodi(id)