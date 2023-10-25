eleve_note = {"Thorez": 20, "Salvador": 2, "Guirao": 16, "Boisson-Serre": 7}

top_student = max(eleve_note, key=eleve_note.get)

print("Le meilleur étudiant est ", top_student)