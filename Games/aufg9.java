package com.company;

class Koordinate {
    int x;
    int y;
    Koordinate(int x, int y){
        this.x = x;
        this.y = y;
    }
}

class Schiff {
    Koordinate pos;
    boolean treffer;
    
    Schiff(Koordinate pos, boolean treffer) {
        this.pos = pos;
        this.treffer = treffer;
    }
}

public class Main {

    public static void main(String[] args) {
        final int X = 9;
        final int Y = 7;
        final int SCHIFF = 4;
        char[][] spielfeld = new char[X][Y];
        Schiff[] schiffe = new Schiff[SCHIFF];

        initialisieren(spielfeld);
        initialisieren(X, Y, schiffe);

        luschern(schiffe); // sp¨ater auskommentieren
        do {
            anzeigen(spielfeld);
            Koordinate eingabe = rate();
            char ergebnis = pruefe(schiffe, eingabe);
            eintragen(spielfeld, eingabe, ergebnis);
        } while (nichtGefunden(schiffe));

        System.out.println("You Win!");
    }

    static void initialisieren(char[][] spielfeld){
        for (int i=0; i<spielfeld.length; i++) {
            for (int j=0; j<spielfeld[0].length; j++) {
                spielfeld[i][j] = '+';
            }
        }
    }

    static void luschern(Schiff[] schiffe) {
    }

    static void initialisieren(int X, int Y, Schiff[] schiffe){
        java.util.Random eingabe = new java.util.Random();
        for (int i = 0; i<schiffe.length;) {
            Koordinate pos = new Koordinate(eingabe.nextInt(X), eingabe.nextInt(Y));
            if(!enthält(schiffe, pos)) {
                schiffe[i++] = new Schiff(pos, false);
            }
        }
    }

    private static boolean enthält(Schiff[] schiffe, Koordinate pos) {
        for (Schiff item : schiffe) {
            if (item != null && pos.x == item.pos.x && pos.y == item.pos.y) {
                return true;
            }
        }
        return false;
    }

    static void anzeigen(char[][] spielfeld){
        System.out.println("Game Board:");
        for (int i=0; i<spielfeld[0].length; i++) {
            for (int j = 0; j < spielfeld.length; j++) {
                System.out.printf("%s ", spielfeld[j][i]);
            }
            System.out.println();
        }
    }

    static Koordinate rate() {
        java.util.Scanner scan = new java.util.Scanner(System.in);
        int x, y;
        do {
            System.out.println("Please Enter (x, y) Coordinates, x ∋ [1, 9], y ∋ [1, 7]:");
            System.out.print("x = "); x = scan.nextInt() - 1;
            System.out.print("y = "); y = scan.nextInt() - 1;
        } while (x < 0 || x > 8 || y < 0 || y > 6);

        return new Koordinate(x, y);
    }

    private static char pruefe(Schiff[] schiffe, Koordinate eingabe) {
        for (Schiff item : schiffe) {
            if (eingabe.x == item.pos.x && eingabe.y == item.pos.y) {
                item.treffer = true;
                return  '⚓';
            }
        }
        return '◽';
    }

    private static void eintragen(char[][] spielfeld, Koordinate eingabe, char ergebnis) {
        spielfeld[eingabe.x][eingabe.y] = ergebnis;
    }

    private static boolean nichtGefunden(Schiff[] schiffe) {
        for (Schiff item: schiffe) {
            if (!item.treffer){
                return true;
            }
        }
        return false;
    }

}
