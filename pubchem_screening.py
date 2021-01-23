import os
import requests
import sys

#sys.argv[1] == path to the file with list of compounds to download (each in the new line)
#missing writes out if file not download (because not found in PubChem)

with open(sys.argv[1]) as generic_database:
    folder = os.path.dirname(sys.argv[1])
    missing = open(f"{folder}/missing.txt","a+")
    Lines = generic_database.readlines()
    for line in Lines:
        compound_name = line.replace('\n','')
        PUBCHEMurl = f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{compound_name.replace(" ","_").rstrip()}/SDF'
        try:
            response = requests.get(PUBCHEMurl)
            if response.status_code == 200:
                print(compound_name)
                with open(f"{folder}/{compound_name}.sdf","wb") as f:
                    f.write(response.content)
                print("... Saved!")
        except Exception:
            print(f"Error with {line}")
            missing.write(f"{line}")
            pass
missing.close()
