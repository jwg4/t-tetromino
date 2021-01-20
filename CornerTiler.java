package tiling;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics2D;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.io.PrintWriter;
import java.math.BigInteger;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Scanner;

import javax.swing.JFrame;


/*
 * This class reads a text picture as printed by the other classes,
 * solves the rest of the board, generates a ps (maybe) of the result.
 */
public class CornerTiler{
	private static Poly[] poly;
	private static boolean[][] board;
	private static int[][] tiled;
	private static int[] numused;
	private static int NUMTILE = 2;
	private static int HEIGHT = 4;
	private static int WIDTH = 6;
	private static int TET = 25;
	private static int MON = 4;
	private static BigInteger hashmemoMultiplier1, hashmemoMultiplier2;
	private static Map<BigInteger, BigInteger> hashmemo;
	private static BigInteger numSolutions;

	private static int unitSize = 20;
	private static JFrame drawFrame;
	private static boolean SHOWFRAME = true;

	private static int[] belowNum, aboveNum;
	private static int searchSpan, belowStart, aboveStart;


	public static void main(String[] args) {
		initialize();
		readBoard();
		findSolution();
		findRepresentatives();
	}

	// polyominos are encoded this way:
	// 1 | 4 | 7
	// 2 | 5 | 8
	// 3 | 6 | 9
	public static void initialize() {
		poly = new Poly[2];
		boolean ttet[] = { true, true, true, false, true, false };
		poly[0] = new Poly(3, 2, ttet, 4, false, Color.green, TET);
		boolean monon[] = { true };
		poly[1] = new Poly(1, 1, monon, 1, false, Color.magenta, MON);
		numused = new int[NUMTILE]; 
		numSolutions = new BigInteger("0");
		hashmemo = new HashMap<BigInteger, BigInteger>();
		BigInteger bigTwo = new BigInteger("2");
		hashmemoMultiplier1 = bigTwo.pow(3 * WIDTH);
		hashmemoMultiplier2 = hashmemoMultiplier1.multiply(new BigInteger("256"));
		if(SHOWFRAME){
			drawFrame = new JFrame();
			drawFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		}
		searchSpan = 96;
		belowNum = new int[100];
		aboveNum = new int[100];
	}



	public static boolean solve(int siStart) {
		int si = 0, sj = 0; // Hold leftmost of topmost open square
		Poly currentPoly;
		boolean canFit; // can the board take the current polyomino?
		BigInteger bitmap; // for memoizing the number of ways to finish tiling
		BigInteger numLocalStart = new BigInteger("0"); // starting number of
		// solutions
		boolean canMemoize = false;
		BigInteger bigHasher = BigInteger.ZERO;
		bitmap = new BigInteger("0");
		String pic;
		boolean solvable = false;

		// set si and sj to be the leftmost of the topmost open squares
		boolean emptyFlag = false;

		// drawBoard();
		/*
		try {
			Thread.sleep(50);
		} catch (InterruptedException e) {
		}
		 */

		for (int i = siStart; i <= HEIGHT; i++)
			for (int j = 1; j <= WIDTH; j++)
				if (!board[i][j]) {
					emptyFlag = true;
					si = i;
					sj = j;
					i = HEIGHT + 2; // Kludge to end the loops
					j = WIDTH + 2;
				}

		if (emptyFlag == false) {

			drawBoard();
			/*
			try {

				Thread.sleep(500);
			} catch (InterruptedException e) {
			}
			 */
			//generateImage();
			numSolutions = numSolutions.add(BigInteger.ONE);
			return true;
		}

		// Let's do the dynamic programming stuff
		// Find the bitmap of the fringe of the board
		if (sj > 2)
			canMemoize = false;
		else {
			canMemoize = true;
			int bitloc = 0;
			for (int iloc = si; (iloc <= si + 2) && (iloc <= HEIGHT); iloc++)
				for (int jloc = 1; jloc <= WIDTH; jloc++) {
					if (board[iloc][jloc]) 
						bitmap = bitmap.setBit(bitloc);
					bitloc++;
				}

			// See if we have memo-ized this value
			bigHasher = hashmemoMultiplier2
					.multiply(new BigInteger(new Integer(si).toString()))
					.add(hashmemoMultiplier1.multiply(new BigInteger(
							new Integer(numused[1]).toString()))).add(bitmap);
			BigInteger numFromHere = hashmemo.get(bigHasher);

			if (numFromHere != null) {
				numSolutions = numSolutions.add(numFromHere);
				if(numFromHere.compareTo(BigInteger.ZERO) > 0)
					return true;
				else
					return false;
			}
			else{ // Try the other direction as well . . .
				bitloc = 0;
				bitmap = new BigInteger("0");
				for(int iloc = si; (iloc <= si + 2) && (iloc <= HEIGHT); iloc++)
					for(int jloc = WIDTH; jloc >= 1; jloc--){
						if(board[iloc][jloc]){
							bitmap = bitmap.setBit(bitloc);
						}
						bitloc++;
					}
				// See if we have memo-ized this value
				bigHasher = hashmemoMultiplier2.multiply(new BigInteger(new Integer(si).toString()))
						.add(hashmemoMultiplier1.multiply(new BigInteger(new Integer(numused[1]).toString()))).add(bitmap);
				numFromHere = hashmemo.get(bigHasher);
				if(numFromHere != null){
					numSolutions = numSolutions.add(numFromHere);
					if(numFromHere.compareTo(BigInteger.ZERO) > 0)
						return true;
					else
						return false;
				}
				else{
					numLocalStart = numSolutions;
				}
			} 

		}

		for (int polyNum = 0; polyNum < NUMTILE && !solvable; polyNum++) {
			if (poly[polyNum].numAllowed > numused[polyNum]) {
				for (int orNum = 0; orNum < poly[polyNum].numShapes && !solvable; orNum++) {
					currentPoly = poly[polyNum].shapes[orNum];
					int offset = currentPoly.offset;
					if (offset < sj && sj + currentPoly.w - offset < WIDTH + 2
							&& si + currentPoly.l < HEIGHT + 2) {
						canFit = true;
						for (int pj = 0; pj < currentPoly.w; pj++)
							for (int pi = 0; pi < currentPoly.l; pi++)
								if (currentPoly.b[pj * currentPoly.l + pi]
										&& board[si + pi][sj + pj - offset])
									canFit = false;
						if (canFit) {
							numused[polyNum]++;
							for (int pj = 0; pj < currentPoly.w; pj++)
								for (int pi = 0; pi < currentPoly.l; pi++)
									if (currentPoly.b[pj * currentPoly.l + pi]) {
										board[si + pi][sj + pj - offset] = true;
										tiled[si + pi][sj + pj - offset] = 1 + numused[polyNum];
										if (polyNum == NUMTILE - 1)
											tiled[si + pi][sj + pj - offset] = -19;

									}
							solvable = solvable | solve(si);
							numused[polyNum]--;
							for (int pj = 0; pj < currentPoly.w; pj++)
								for (int pi = 0; pi < currentPoly.l; pi++)
									if (currentPoly.b[pj * currentPoly.l + pi]) {
										board[si + pi][sj + pj - offset] = false;
										tiled[si + pi][sj + pj - offset] = -1;
									}
						}
					}
				}
			}
		}
		if (canMemoize) {
			hashmemo.put(bigHasher, numSolutions.subtract(numLocalStart));
		}
		return solvable;
	}

	/*
	 * Builds a board with a staircase at the top.
	 */
	public static void readBoard(){
		int x[][] = new int[100][15]; // 100 tall, 15 wide

		WIDTH = 15;
		if(SHOWFRAME){
			drawFrame.setPreferredSize(new Dimension(WIDTH*unitSize+10, 50*unitSize + 40));
			drawFrame.pack();
			drawFrame.setVisible(true);
		}
		// Finally fill the "board" and "tiled" arrays for use with the "solved" function
		board = new boolean[100][WIDTH + 2];
		tiled = new int[100][WIDTH + 2];
		for (int i = 0; i <= HEIGHT + 1; i++)
			for (int j = 0; j <= WIDTH + 1; j++) {
				board[i][j] = false;
				tiled[i][j] = -1;
			}

		/*
		// Set the top boundary shape to be a staircase
		for(int i = 1; i <= WIDTH - 1; i++){
			for(int j = i+1; j <= WIDTH; j++){
				board[i][j] = true;
				tiled[i][j] = 17;
			}
		}
		*/
		
		// Set the top region to have on its left a cylinder boundary 6333419
		for(int i = 1; i <= WIDTH; i++){
			for(int j = 1; j  <= 3; j++){
				board[i][j] = true;
				tiled[i][j] = 99;
			}
		}
		int[][] bdry6333419 = {{2,1}, {6, 1}, {7, 1}, {8, 1}, {8, 2}, {9, 1}, {9, 2}, {10, 1}, {12, 1}, {14, 1}, {15, 1}, {15, 2}};
		for(int[] b : bdry6333419){
			for(int j = 1; j <= 3; j++)
			board[b[0]][b[1]+3] = true;
			tiled[b[0]][b[1]+3] = 99;
		}
	}




	public static void findSolution(){

		// Now find the least number of gaps needed to tile from the boundary
		// on down, to various heights.
		for(HEIGHT = 48; HEIGHT < searchSpan; HEIGHT++){
			// Set the number of monominos we are allowed
			poly[0].numAllowed = 10000;
			
			// Staircase monomino function
			//poly[1].numAllowed = ((HEIGHT*WIDTH-(WIDTH-1)*WIDTH/2) % 4) - 4;
			
			// boundary 6333419 monomino function
			poly[1].numAllowed = ((HEIGHT * WIDTH - 45 - 12) % 4) - 4;
			
			boolean solved = false;
			while(!solved){
				hashmemo.clear();
				poly[1].numAllowed += 4;
				numused[0] = numused[1] = 0;
				solved = solve(1);
			}

			System.out.println("Solved Bottom to height " + HEIGHT + "  with " + poly[1].numAllowed + " monominos");
		}
	}

	public static void findRepresentatives(){
		for(int class16 = 0; class16 < 16; class16++){
			for(int adder=0; adder < 64; adder += 16){
				int h = class16 + adder;
				// Find the best way to make h
				int min = 20;
				for(int i = 0; i < h; i++){
					int j = h - i;
					if(i >= belowStart && i < belowStart + searchSpan &&
							j >= aboveStart && j < aboveStart + searchSpan){
						if(belowNum[i] + aboveNum[j] < min)
							min = belowNum[i] + aboveNum[j];
					}
				}
				// Now print out all the best ways to make h
				System.out.print("Height " + h + "\tMin = " + min + ":\t");
				for(int i = 0; i < h; i++){
					int j = h - i;
					if(i >= belowStart && i < belowStart + searchSpan &&
							j >= aboveStart && j < aboveStart + searchSpan){
						if(belowNum[i] + aboveNum[j] == min)
							System.out.print(i + "(" + belowNum[i] + ")-" + j + "(" + aboveNum[j] + ")  ");
					}
				}
				System.out.println("");
			}
			System.out.println("");
		}
	}


	public static void generateImage(){
		String boundaryString = "rururdrurdrdrrurrurrrdrur";
		int lb = locateBoundary(boundaryString);
		System.out.println(lb);
		PrintWriter p = null;
		try
		{
			p = new PrintWriter("Paper/graphic2" + WIDTH + "x" + HEIGHT + ".eps");
		}
		catch(IOException ex)
		{
			ex.printStackTrace();
		}		
		// Add stuff that all our images will have
		p.println("%!PS-Adobe-3.0 EPSF-3.0\n" +
				"%%BoundingBox: 0 0 " + (10*WIDTH+4) + " " + (10*HEIGHT+4) + "\n" +
				"/cp {closepath} bind def\n" +
				"/ef {eofill} bind def\n" +
				"/l {lineto} bind def\n" +
				"/m {moveto} bind def\n" +
				"/n {newpath} bind def\n" +
				"/s {stroke} bind def\n" +
				"0.000 0.000 0.000 setrgbcolor\n" +
				"0.050 setlinewidth\n" +
				"1 setlinejoin 1 setlinecap\n");
		// reflect or not, depending on which way the boundary goes
		if(lb > 0)
			p.println("2 " + (10*HEIGHT+2) + " translate\n" +
					"10 -10 scale");
		else
			p.println((10*WIDTH+2) + " " + (10*HEIGHT+2) + " translate\n" +
					"-10 -10 scale");

		// Print the tile boundaries
		p.print("n 0 0 m " + WIDTH + " 0 l s\n");
		p.print("n 0 0 m 0 " + HEIGHT + " l s\n");
		p.print("n 0 " + HEIGHT + " m " + WIDTH + " " + HEIGHT + " l s\n");
		p.print("n " + WIDTH + " 0 m " + WIDTH + " " + HEIGHT + " l s\n");
		for(int i = 1; i <= HEIGHT; i++){
			for(int j = 1; j <= WIDTH; j++){
				// Look right
				if(j < WIDTH && tiled[i][j] != tiled[i][j+1])
					p.print("n " + j + " " + (i-1) + " m " +
							j + " " + i + " l s\n");
				// look down
				if(i < HEIGHT && tiled[i][j] != tiled[i+1][j])
					p.print("n " + (j-1) + " " + i + " m " +
							j + " " + i + " l s\n");
				// shade the monominos
				if(tiled[i][j] == -19)
					p.print("n " + (j-1) + " " + (i-1) + " m " +
							j + " " + (i-1) + " l " +
							j + " " + i + " l " +
							(j-1) + " " + i + " l cp gsave 0.500 0.500 0.500 setrgbcolor 1.000 eofill grestore s\n");
			}
		}

		// Print a nice dark boundary
		int y = Math.abs(lb) - 1;
		int x = lb > 0 ? 0 : WIDTH;
		p.println("0.250 setlinewidth\n");
		p.print("n "+ x + " " + y + " m ");
		for(int t = 0; t < boundaryString.length(); t++){
			char dir = boundaryString.charAt(t);
			switch(dir){
			case 'r':
				x = lb > 0 ? x+1 : x-1;
				break;
			case 'u':
				y--;
				break;
			case 'd':
				y++;	
				break;
			}
			p.print(x + " " + y + " l ");
		}
		p.println(" s");
		p.print("\nshowpage");	
		p.close();
	}


	// Finds a boundary described by string b. Looks only at row 4 or below
	public static int locateBoundary(String b){
		boolean foundit = false;
		int i;
		for(i = 2; i <= HEIGHT; i++){
			int x = 0;
			int y = i;
			foundit = true;
			for(int t = 0; t < b.length(); t++){
				char dir = b.charAt(t);
				switch(dir){
				case 'r':
					if(y != 1 && tiled[y][x+1] == tiled[y-1][x+1])
						foundit = false;
					x++;
					break;
				case 'u':
					if(tiled[y-1][x] == tiled[y-1][x+1])
						foundit = false;
					y--;
					break;
				case 'd':
					if(tiled[y][x] == tiled[y][x+1])
						foundit = false;
					y++;	
					break;
				}
				if(!foundit)
					break;
			}
		}
		if(foundit)
			return i;

		// Check the right-to-left direction
		for(i = 4; i <= HEIGHT; i++){
			int x = WIDTH;
			int y = i;
			foundit = true;
			for(int t = 0; t < b.length(); t++){
				char dir = b.charAt(t);
				switch(dir){
				case 'r':
					if(tiled[y][x] == tiled[y-1][x])
						foundit = false;
					x--;
					break;
				case 'u':
					if(tiled[y-1][x] == tiled[y-1][x+1])
						foundit = false;
					y--;
					break;
				case 'd':
					if(tiled[y][x] == tiled[y][x+1])
						foundit = false;
					y++;
					break;
				}
				if(!foundit)
					break;
			}
			if(foundit)
				return -i;
		}
		System.out.println("DISASTER!");
		return 0;
	}


	private static String drawBoardPic() {
		String pic = "";

		for (int i = 1; i <= HEIGHT; i++) {
			// Draw borders above tile row i
			pic = pic + "+";
			for (int j = 1; j <= WIDTH; j++) {
				if (tiled[i][j] != tiled[i - 1][j])
					pic = pic + "--";
				else
					pic = pic + "  ";
				pic = pic + "+";
			}
			pic = pic + "\n";

			// Draw borders between the tiles in row i
			pic = pic + "|  ";
			for (int j = 1; j < WIDTH; j++) {
				if (tiled[i][j] != tiled[i][j + 1])
					pic = pic + "|  ";
				else
					pic = pic + "   ";
			}
			pic = pic + "|\n";
		}

		// Draw borders below the bottom row
		pic = pic + "+";
		for (int j = 1; j <= WIDTH; j++) {
			pic = pic + "--+";
		}

		return pic;
	}


	private static void drawBoard() {
		int inset = unitSize / 5;
		Graphics2D g = (Graphics2D) drawFrame.getGraphics();
		g.setColor(Color.gray);
		for (int i = 1; i <= HEIGHT; i++)
			for (int j = 1; j <= WIDTH; j++) {
				int cc = tiled[i][j];
				if (tiled[i][j] == -1)
					g.setColor(Color.gray);
				else if (tiled[i][j] == -19)
					g.setColor(Color.black);
				else
					g.setColor(new Color(cc * 13 % 256, cc * 51 % 256,
							cc * 77 % 256));

				g.fillRect(unitSize * (j - 1) + 5, unitSize * i + 5, unitSize,
						unitSize);
				if (tiled[i][j] == -19) {
					g.setColor(Color.white);
					g.fillRect(unitSize * (j - 1) + 5 + inset, unitSize * i + 5
							+ inset, unitSize - 2 * inset, unitSize - 2 * inset);
				}
			}
	}
}
