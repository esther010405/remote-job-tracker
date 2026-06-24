import asyncio
from pathlib import Path
from scraper import get_emploi
import pandas as pd

from telegram_sender import send_message

output = Path("outputs")
output.mkdir(exist_ok=True)

data = get_emploi()

df = pd.DataFrame(data)

df.to_excel(
    output / "jobs.xlsx",
    index=False
)


def load_sent_jobs():
    with open("sent_jobs.txt", "r" ) as f:
       ids=f.read().splitlines()
    
    print(ids)
    return ids
sent_jobs=load_sent_jobs()



for job in data:
    if job["id"] not in sent_jobs:
        print("Nouvelle offre :", job["titre"])
        message = f"""
        📢 Nouvelle offre Python

        🏢 Entreprise : {job['entreprise']}

        💼 Poste : {job['titre']}

        🔗 Lien : {job['lien']}
        """
        

        asyncio.run(
            send_message(message)
        )
        with open("sent_jobs.txt" , "a") as f :
            f.write(job["id"]+  "\n")  
            
print("Fichier créé avec succès !")

