def save(tkFenster0, e1, var, ausgabe, f0_len):
    # Speichern der Text-Datei
    # Wenn kein Benutzer eingetragen ist, kann nicht gespeichert werden
    if len(e1.get()) == 0:
        print("Mitarbeiter eintragen!")

    else:
        # Eintrag des ersten Eintrags mit der Methode 'w'-write
        file = open("Reinigungsplan" + "_" + str(e1.get()) + ".txt", 'w')
        file.write("[" + str(var[0].get()) + "]" + " - " + ausgabe[0])
        file.close()

        for i in range(1, f0_len, 1):
            # Alle weiteren Einträge mit der Methode 'a'-append
            file = open("Reinigungsplan" + "_" + str(e1.get()) + ".txt", 'a')
            file.write("[" + str(var[i].get()) + "]" + " - " + ausgabe[i])
            file.close()

        tkFenster0.destroy()