package com.company;

public class Main {

    public static void main(String[] args) {
        final int X = 9;
        final int Y = 7;
        final int SCHIFF = 4;
        int stimmt = 0;

        char[][] spielfeld = new char[X][Y];
        int[][] schiffe = new int[SCHIFF][2];

        initialisieren(spielfeld);
        ausblenden(schiffe);

        do {
            anzeigen(spielfeld);
            int[] eingabe = rate();
            stimmt += eintragen(spielfeld, eingabe, schiffe);
        } while (SCHIFF != stimmt);
        anzeigen(spielfeld);
        System.out.println("Du hast gewonnen!");
    }

    static void initialisieren(char[][] spielfeld){
        for (int i=0; i<spielfeld.length; i++) {
            for (int j=0; j<spielfeld[0].length; j++) {
                spielfeld[i][j] = '+';
            }
        }
    }

    static void ausblenden(int[][] schiffe) {
        java.util.Random eingabe = new java.util.Random();
        for (int i = 0; i<4;) {
            int[] coordinate = {eingabe.nextInt(9), eingabe.nextInt(7)};
            if(!enthält(schiffe, coordinate)) {
                schiffe[i++] = coordinate;
            }
        }
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

    static int[] rate() {
        int[] erg = new int[2];

        java.util.Scanner scan = new java.util.Scanner(System.in);
        do {
            System.out.println("Please Enter (x, y) Coordinates, x ∋ [1, 9], y ∋ [1, 7]:");
            System.out.print("x = "); erg[0] = scan.nextInt() - 1;
            System.out.print("y = "); erg[1] = scan.nextInt() - 1;
        } while (erg[0] < 0 || erg[0] > 8 || erg[1] < 0 || erg[1] > 6);

        return erg;
    }

    static int eintragen(char[][] spielfeld, int[] eingabe, int[][] schiffe) {

        if (enthält(schiffe, eingabe)){
            spielfeld[eingabe[0]][eingabe[1]] = '⚓';
            return 1;
        }

        spielfeld[eingabe[0]][eingabe[1]] = '◽';
        windrichtungen(spielfeld, eingabe, schiffe);
        return 0;
    }

    private static boolean enthält(final int[][] array, final int[] coordinate) {
        for (final int[] item : array) {
            if (coordinate[0] == item[0] && coordinate[1] == item[1]) {
                return true;
            }
        }
        return false;
    }

    static void windrichtungen(char[][] spielfeld, int[] eingabe, int[][] schiffe) {
        String[][] schiffeNote = {
                {"··", "·", "···", "·", "··"},
                {"··", "·", "···", "·", "··"},
                {"··", "·", String.format("%d,%d", eingabe[0]+1, eingabe[1]+1), "·", "··"},
                {"··", "·", "···", "·", "··"},
                {"··", "·", "···", "·", "··"}
        };

        for (int[] item: schiffe){
            if (item[0] < eingabe[0] && item[1] < eingabe[1] && spielfeld[item[0]][item[1]] == '+') {
                schiffeNote[0][0] = "NW"; schiffeNote[1][1] = "⇖";
            }
            if (item[0] == eingabe[0] && item[1] < eingabe[1] && spielfeld[item[0]][item[1]] == '+') {
                schiffeNote[0][2] = "·N·"; schiffeNote[1][2] = "·⇑·";
            }
            if (item[0] > eingabe[0] && item[1] < eingabe[1] && spielfeld[item[0]][item[1]] == '+') {
                schiffeNote[0][4] = "NO";  schiffeNote[1][3] = "⇗";
            }
            if (item[0] < eingabe[0] && item[1] == eingabe[1] && spielfeld[item[0]][item[1]] == '+') {
                schiffeNote[2][0] = "W·"; schiffeNote[2][1] = "⇐";
            }
            if (item[0] > eingabe[0] && item[1] == eingabe[1] && spielfeld[item[0]][item[1]] == '+') {
                schiffeNote[2][4] = "·O";  schiffeNote[2][3] = "⇒";
            }
            if (item[0] < eingabe[0] && item[1] > eingabe[1] && spielfeld[item[0]][item[1]] == '+') {
                schiffeNote[4][0] = "SW"; schiffeNote[3][1] = "⇙";
            }
            if (item[0] == eingabe[0] && item[1] > eingabe[1] && spielfeld[item[0]][item[1]] == '+') {
                schiffeNote[4][2] = "·S·"; schiffeNote[3][2] = "·⇓·";
            }
            if (item[0] > eingabe[0] && item[1] > eingabe[1] && spielfeld[item[0]][item[1]] == '+') {
                schiffeNote[4][4] = "SO"; schiffeNote[3][3] = "⇘";
            }
        }
        kompass(schiffeNote);
    }

    static void kompass(String[][] windrichtungen) {
        System.out.println("Compass:\n _____________");
        String format = "|%1$-2s·%2$-1s·%3$-3s·%4$-1s·%5$-2s|%n";
        for(String[] line : windrichtungen){
            System.out.printf(format, (Object[]) line);
        }
        System.out.println(" ‾‾‾‾‾‾‾‾‾‾‾‾‾");
    }
}

//        String[][] schiffeNote = {
//                {"NW", "·", "·N·", "·", "NO"},
//                {"··", "⇖", "·⇑·", "⇗", "··"},
//                {"W·", "⇐", "5,5", "⇒", "·O"},
//                {"··", "⇙", "·⇓·", "⇘", "··"},
//                {"SW", "·", "·S·", "·", "SO"}
//        };
//        kompass(schiffeNote);

//        for (int i=0; i<schiffe.length; i++) {
//            System.out.println(String.format("(%d, %d)", schiffe[i][0]+1, schiffe[i][1]+1));
//        }
