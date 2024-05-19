# importarea pachetelor necesare
from imutils import paths
import numpy as np
import imutils
import cv2
import json

def scor_culoare(image):
    # impartirea imaginilor in componentele RGB
    (B, G, R) = cv2.split(image.astype("float"))
    # media fiecarei colori
    valoare_R = np.mean(R)
    valoare_G = np.mean(G)
    valoare_B = np.mean(B)
    return valoare_R, valoare_G, valoare_B

# introducerea locatiei directorului
director_imagini = input("Scrie locatia directorului cu imagini: ")

# initializarea rezultatelor
print("[INFO] Calcularea fiecarui scor pentru fiecare imagine...")
rezultate = {"rosu": [], "verde": [], "albastru": []}

for caleimagine in paths.list_images(director_imagini):
    # incarcarea fiecarei imagini, schimbarea rezolutiei pentru o calculare mai rapida si introducerea fiecarui scor de culoare pentru fiecare imagine
    imagine = cv2.imread(caleimagine)
    imagine = imutils.resize(imagine, width=250)
    valoare_R, valoare_G, valoare_B = scor_culoare(imagine)

    # determinarea culori predominanta
    if valoare_R > valoare_G and valoare_R > valoare_B:
        dominant = "rosu"
    elif valoare_G > valoare_R and valoare_G > valoare_B:
        dominant = "verde"
    else:
        dominant = "albastru"

    # adaugarea locatiei imagini si scorul acesteia
    rezultate[dominant].append({
        "locatie": caleimagine,
        "scor": {
            "rosu": valoare_R,
            "verde": valoare_G,
            "albastru": valoare_B
        }
    })

# salvarea rezultatelor intr-un fisier JSON
fisier = "grupare_imagini_si_scoruri.json"
with open(fisier, "w") as f:
    json.dump(rezultate, f, indent=4)

print(f"[INFO] Rezultatele sunt salvate in {fisier}")
