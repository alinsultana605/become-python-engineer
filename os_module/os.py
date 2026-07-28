import os
from datetime import datetime

# print(dir(os))

print(os.getcwd())
# print(help(os.getcwd))
# os.mkdir('OS-Demo-2/Sub-Dir-1')
# os.makedirs('OS-Demo-2/Sub-Dir-1')
# os.rmdir('OS-Demo-2/Sub-Dir-1')
# os.removedirs('OS-Demo-2/Sub-Dir-1')
# os.rename('test.txt', 'demo.txt')
# mod_time = os.stat('readme.md').st_mtime
# print(datetime.fromtimestamp(mod_time))
# print(os.stat('readme.md'))
# print(os.listdir())

# for dirpath, dirname, filename in os.walk(os.getcwd()):
#     print('Current Path:', dirpath)
#     print('Directories:', dirname)
#     print('Files:', filename)
#     print()

# print(os.environ.get('HOME'))
# # file_path = os.environ.get('HOME') + 'test.txt'
# file_path = os.path.join(os.environ.get('HOME'), 'test.txt')

# with open(file_path, 'w') as f:
#     f.wte

print(os.path.exists('/tmp/text.txt'))
print(os.path.splitext('/tmp/text.txt'))


"""
🧩 1. Ce este modulul os?
Modulul os îți permite să interacționezi cu sistemul de operare:

lucrul cu directoare și fișiere

obținerea informațiilor despre sistem

manipularea căilor

variabile de mediu

rularea de comenzi în shell

Este unul dintre cele mai folosite module din Python.

📁 2. Lucrul cu directoare
🔹 os.getcwd()
Returnează directorul curent.

python
import os
print(os.getcwd())
🔹 os.chdir(path)
Schimbă directorul curent.

python
os.chdir("C:/Users/Sultana/Desktop")
🔹 os.listdir(path)
Listează fișierele dintr-un director.

python
print(os.listdir())
📂 3. Crearea directoarelor
✔ os.mkdir(path)
Creează un singur director.

✔ os.makedirs(path)
Creează toată structura de directoare necesară.

Diferența ai învățat-o deja.

🗑️ 4. Ștergerea directoarelor
✔ os.rmdir(path)
Șterge un singur director gol.

✔ os.removedirs(path)
Șterge recursiv directoare goale (director + părinți).

📄 5. Lucrul cu fișiere
🔹 os.remove(path)
Șterge un fișier.

python
os.remove("test.txt")
🔹 os.rename(src, dst)
Redenumește sau mută un fișier.

python
os.rename("vechi.txt", "nou.txt")
🧭 6. Lucrul cu căi (path-uri)
Deși Corey explică os.path, în practică azi folosim pathlib.
Dar teoria lui include:

🔹 os.path.join()
Construiește o cale corectă pentru sistemul tău.

python
path = os.path.join("folder", "fisier.txt")
🔹 os.path.exists()
Verifică dacă o cale există.

🔹 os.path.isdir() / os.path.isfile()
Verifică tipul obiectului.

🌍 7. Variabile de mediu
🔹 os.environ
Accesezi variabilele de mediu.

python
print(os.environ.get("HOME"))
Poți și seta:

python
os.environ["API_KEY"] = "12345"
🧨 8. Rularea de comenzi în shell
🔹 os.system(command)
Rulează o comandă în terminal.

python
os.system("dir")  # Windows
os.system("ls")   # Linux/Mac
Corey explică că nu este recomandat în aplicații mari — se folosește subprocess.

🧱 9. Funcții utile din os
🔹 os.stat(path)
Informații despre fișier (mărime, timp modificare etc.)

🔹 os.walk(path)
Parcurge recursiv directoare — foarte util pentru proiecte mari.

python
for dirpath, dirnames, filenames in os.walk("."):
    print(dirpath, dirnames, filenames)
🎯 10. De ce este important modulul os?
Pentru că:

este baza pentru orice aplicație care lucrează cu fișiere

îl folosești în automatizări, scripturi, servere, proiecte web

este necesar pentru administrarea sistemelor

este folosit în combinație cu shutil, pathlib, subprocess

"""