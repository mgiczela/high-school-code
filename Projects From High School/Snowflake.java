import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.util.Stack;

import javax.swing.JFrame;
import javax.swing.JPanel;

class SnowFlakePanel extends JPanel
{
    private java.util.Random rand = new java.util.Random();

    public SnowFlakePanel()
    {
        super.setPreferredSize(new Dimension(400, 400));
        super.setBackground(Color.WHITE);
    }

    @Override
    public void paintComponent(Graphics g)
    {
        super.paintComponent(g);

        int width  = getWidth();
        int height = getHeight();

        //draw code below
        g.setColor(Color.BLUE);
        //g.drawLine(100, (height / 2), width - 100, (height / 2));
        //drawSnowflake(g, (width / 2), (height / 2), (width / 4), 3);
        
        
        for(int i = 0; i < 30; i++)
        {
            int red = rand.nextInt(200);
            int green = rand.nextInt(200);
            int blue = rand.nextInt(200);
            
            g.setColor(new Color(red, green, blue));
            
            int randX = rand.nextInt(width);
            int randY = rand.nextInt(height);
            
            int randWidth = rand.nextInt(5, 25);
            int randDepth = rand.nextInt(1 ,4);
            drawSnowflake(g, randX, randY, randWidth, randDepth);
            

        }
        
        //helper meathod: drawSnowflake (draws one snowfalke at given center x and y and line lenght l)
        
        

        //end drawing code
    }

    //helper meathod: drawSnowflake (draws one snowfalke at given center x and y and line lenght l)
    public void drawSnowflake(Graphics g, int centerX, int centerY, int lineLen, int depth)
    {
        //x2 = centerX + len * cos(angle)
        //y2 = centerY + len * sin(angle)
        
        //increment by pi/3 radians
        //so the angle is (i * (Math.PI / 3)) 
        if (depth == 0)
        {
            return;
        }
        
        for (int i = 0; i < 6; i++)
        {
            
            double angle = (double) i * (Math.PI / 3.0);
            double endX = (double) centerX + (double) lineLen * Math.cos(angle); 
            double endY = (double) centerY + (double) lineLen * Math.sin(angle); 
            g.drawLine(centerX, centerY, (int) endX, (int) endY);
            drawSnowflake(g, (int) endX, (int) endY, (int)(lineLen / 4), depth-1);
            
           
        }
    }
    
    

    // other meathods 

    // #2
    public static int productOfEvens(int n)
    {
        if (n > 0)
            return (2 * n) * productOfEvens(n - 1);
        else
            return 1;
    }

    // #3
    public static double sumReciprocals(int n)
    {
        if (n == 1)
            return 1.0;
        return (1.0 / n) + sumReciprocals(n - 1);
    }

    // #5
    public String conversion(int n, int base)
    {
        if (n == 0)
            return "";
        else
            return conversion(n / base, base) + (n % base);
    }

    // #6
    public static int matchingDigits(int a, int b)
    {
        if (a == 0 && b == 0)
            return 0;

        int match = (a % 10 == b % 10) ? 1 : 0;
        return match + matchingDigits(a / 10, b / 10);
    }

    // #7
    public static void doubleUp(Stack<Integer> nums)
    {
        if (!nums.isEmpty())
        {
            Integer val = nums.pop();
            doubleUp(nums);
            nums.push(val);
            nums.push(val);
        }
    }

    // #8
    public void printThis(int n)
    {
        boolean even = (n % 2 == 0);
        int middleLength = even ? 2 : 1;
        int arrows = (n - middleLength) / 2;

        for (int i = 0; i < arrows; i++)
            System.out.print("<");

        if (even)
            System.out.print("**");
        else
            System.out.print("*");

        for (int i = 0; i < arrows; i++)
            System.out.print(">");

        System.out.println();
    }

    public static void printNums2(int n)
    {
        if (n <= 0)
            return;
        else if (n == 1)
            System.out.print("1 ");
        else if (n == 2)
            System.out.print("1 1 ");
        else
        {
            int v = (n + 1) / 2;
            System.out.print(v + " ");
            printNums2(n - 2);
            System.out.print(v + " ");
        }
    }
}


public class Snowflake
{
    public static void main(String[] args)
    {
        JFrame frame = new JFrame("Snowflake");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(new SnowFlakePanel());
        frame.pack();
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }
}
