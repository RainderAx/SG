import csv


def collecter_donnees(personnage, pers2, gojo,broly):
    # Collecter les données pertinentes
    donnees = {
        'personnage_x': personnage.x,
        'personnage_y': personnage.y,
        
        'pers2_x': pers2.x,
        'pers2_y': pers2.y,

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
