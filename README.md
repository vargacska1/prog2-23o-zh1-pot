## Programozás 2 ZH feladat

A feladat egy meeting room foglaló webapplikáció prototípusának elkészítése.

A prototípusnak csak a következő hét foglalásait kell tudnia kezelni, és az éles rendszerhez képest csökkentett funkcionalitással bír.
(Iteratív szoftverfejelsztés FTW.)

A történt módosítások kerüljenek mentésre adatbázisba vagy fájlba, és a következő indításnál töltse be őket az alkalmazás.

### Elvárt funkciók

- Termek kezelése
  - Listázás
  - Hozzáadás
  - Termek egész hetes kihasználtságának összehasonlítása oszlopdiagramon
- Teremfoglalások kezelése
  - Terem foglaltságának megjelenítése
    - Terem legördülő menüből választható
    - Táblázat 5 oszloppal (hétfő-péntek), soronként 1 óra
      - Zöld: elérhető
      - Piros: foglalt
        - Esemény megnevezése jelenjen meg
  - Terem foglalása
    - Időtartam megadása
      - Nap (hétfő, kedd, ...)
      - Kezdési idő (egész óra: 8h, 9h, ..., 15h)
      - Befejezési idő (egész óra: 9h, 10h, ..., 16h)
        - Ha kezdés >= befejezés, akkor hibaüzenet
    - Esemény nevének megadása (nem kell, hogy egyedi legyen)
    - Ellenőrzés
      - Ha a terem az időtartam bármely részében már foglalt, hibaüzenet
      - Különben a teremfoglalás mentése

Törlés nincs: hétvégén újraindítják az alkalmazást, és törlik az adatbázist/fájlt.
