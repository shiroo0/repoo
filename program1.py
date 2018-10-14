kotel = "=^_^="
iloscKotelow = input("Ile chce kotow :D ")
try:
    iloscKotelow = int(iloscKotelow)
except ValueError as owcaError:
    print("Nie wpsiałeś liczby całkowitej")
    iloscKotelow = 7
x = iloscKotelow * "=^_^= "
print(x)

#Zadanie domowe
"""
Napisac program ktory generuje dowolna piramide z kotelow.
Załozenia:
Jeśli uzytkownik wpisze liczbe ujemna to powinno go okrzyczec i wypisac
do konsoli =^!^=
Przykład:
dla iloscKotelow = 3

Wynik:
"=^_^="
"=^_^=""=^_^="
"=^_^=""=^_^=""=^_^="
Hint: Pętle for i ify
0.5 pkt wiecej za przeslanie githubem
"""

