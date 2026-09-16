//author: michal giczela, jan 16 2026, MY gem game, for fun (jus figure it out)


import java.awt.Font;



/**
 * Enum representing the possible gem colors
 */
enum GemType
{
    GREEN, BLUE, ORANGE, WILDCARD
}

public class Gem
{
    // --------------------
    // INSTANCE VARIABLES
    // --------------------
    private GemType color;
    private int points;

    // stores the gem's color (GREEN, BLUE, or ORANGE)
    /*
    int r = (int)(Math.random() * 3);
    if (r == 0){
        color = GemType.GREEN;
    }else if (r == 1) {
        color = GemType.BLUE;
    }else{
        color = GemType.ORANGE;
    }
    */


    // stores the gem's point value
    /*
    int[] pts = {0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50};

    int rnad = (int)(Math.random() * pts.length);
    this.points = pts[rnad];
    */
    // --------------------
    // CONSTRUCTORS
    // --------------------

    // create a gem with random color and random point value
    public Gem()
    {
        
        
        int r = (int)(Math.random() * 3);
        if (r == 0)
        {
            color = GemType.GREEN;
        }
        else if (r == 1) 
        {
            color = GemType.BLUE;
        }
        else
        {
            color = GemType.ORANGE;
        }
        
        int r2 = (int)(Math.random() * 8);
        if (r2 == 0)
        {
            color = GemType.WILDCARD;
            
        }
        
        if  (color == GemType.WILDCARD)
        {
            int wildCardPtValue = 99;
            this.points = wildCardPtValue;
        }
        else
        {
            int[] pts = {0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50};
            int rnad = (int)(Math.random() * pts.length);
            this.points = pts[rnad];  
        }


        
        
       
        
        
        
        
        // randomly assign a GemType
        // randomly assign a point value from the allowed set
    }

    // create a gem with the specified color and point value
    public Gem(GemType type, int points)
    {
        this.color = type;
        this.points = points;
        // assign instance variables
    }


    // --------------------
    // METHODS
    // --------------------

    // return a string representation of the gem
    public String toString()
    {
        // return formatted string describing gem

        return color + " " + points;
    }

    // get the type (color) of the gem
    public GemType getType()
    {
        // return gem color
        
        return color;
    }

    // get the point value of the gem
    public int getPoints()
    {
        // return gem point value
        return points;
        
    }

    // draw gem at (x, y) using StdDraw
    public void draw(double x, double y)
    {
        // draw image based on gem color
        // draw point value in white text over image
        String image;

        if (color == GemType.GREEN)
        {
            image = "gem_green.png";
        }
        else if (color == GemType.BLUE)
        {
            image = "gem_blue.png";
        }
        else if (color == GemType.ORANGE)
        {
            image = "gem_orange.png";
        }
        else
            image = "wild_card_gem.png";


        StdDraw.picture(x, y, image);

        StdDraw.setPenColor(StdDraw.WHITE);
        StdDraw.setFont(new Font("Comic Sans", Font.BOLD, 16));
        StdDraw.text(x, y, "" + points);
    }


    // --------------------
    // TESTER MAIN METHOD
    // --------------------
/*
    //tester
    public static void main(String [] args)
    {
        final int maxGems = 16;
        
        // Create a gem of each type
        Gem green  = new Gem(GemType.GREEN, 10);
        Gem blue   = new Gem(GemType.BLUE, 20);
        Gem orange = new Gem(GemType.ORANGE, 30);
        System.out.println(green  + ", " + green.getType()  + ", " + green.getPoints());        
        System.out.println(blue   + ", " + blue.getType()   + ", " + blue.getPoints());
        System.out.println(orange + ", " + orange.getType() + ", " + orange.getPoints());
        green.draw(0.3, 0.7);
        blue.draw(0.5, 0.7);
        orange.draw(0.7, 0.7);
        
        // A row of random gems
        for (int i = 0; i < maxGems; i++)
        {
            Gem g = new Gem();
            g.draw(1.0 / maxGems * (i + 0.5), 0.5);
        }
    }
*/
}