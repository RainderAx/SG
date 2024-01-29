import csv


def collecter_donnees(personnage, pers2, gojo,broly):
    # Collecter les données pertinentes
    donnees = {
        'score_personnage': personnage.score,
        'score_pers2': pers2.score,
        'gojo_x': gojo.x,
        'gojo_y': gojo.y,
        'gojo_score' : gojo.score,
        
    }
    return donnees

def ecrire_donnees_csv(donnees, fichier_csv):
    with open(fichier_csv, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=donnees.keys())
        if file.tell() == 0: 
            writer.writeheader()  
        writer.writerow(donnees)
