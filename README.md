## Programozás 2 ZH feladat

A feladat egy meeting room foglaló webapplikáció prototípusának elkészítése.

A prototípusnak csak a következő hét foglalásait kell tudnia kezelni, és az éles rendszerhez képest csökkentett funkcionalitással bír.
(Iteratív szoftverfejelsztés FTW.)

A felhasználókat nem kell authentikálni, bárki nevében lehet foglalni.

A történt módosítások kerüljenek mentésre adatbázisba vagy fájlba, és a következő indításnál töltse be őket az alkalmazás.

### Elvárt funkciók

- Személyek kezelése
  - Listázás
  - Hozzáadás
  - Lefoglalt időtartamok személyenkénti összegzése és megjelenítése oszlopdiagramon
- Termek kezelése
  - Listázás
  - Hozzáadás
  - Lefoglalt időtartamok termenkénti összegzése és megjelenítése oszlopdiagramon
- Teremfoglalások kezelése
  - Terem foglaltságának megjelenítése
    - Terem legördülő menüből választható
    - Táblázat 5 oszloppal (hétfő-péntek), soronként 1 óra
      - Zöld: elérhető
      - Piros: foglalt
        - Személy neve jelenjen meg
  - Terem foglalása
    - Időtartam megadása
      - Nap (hétfő, kedd, ...)
      - Kezdési idő (egész óra: 8h, 9h, ..., 15h)
      - Befejezési idő (egész óra: 9h, 10h, ..., 16h)
        - Ha kezdés >= befejezés, akkor hibaüzenet
    - Személy kiválasztása legördülő menüből
    - Ellenőrzés
      - Ha a terem az időtartam bármely részében már foglalt, hibaüzenet
      - Különben a teremfoglalás mentése
      - (Egy személy több termet is foglalhat egy időben, ezt nem kell ellenőrizni)

Törlés nincs: hétvégén újraindítják az alkalmazást, és törlik az adatbázist/fájlt.
