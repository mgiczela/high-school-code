//michal giczela


public class GemList
{
    // --------------------
    // NESTED NODE CLASS
    // --------------------

    private class Node
    {
        // stores a Gem object
        private Gem gem;
        private Node next;
        // reference to the next Node
        public Node(Gem gem, Node next)
        {
            this.gem = gem;
            this.next = next;
        }
        
    }


    // --------------------
    // INSTANCE VARIABLES
    // --------------------

    // reference to the first node in the list
    private Node head;
    private Node tail;
    
    // number of gems in the list
    private int size;


    // --------------------
    // CONSTRUCTOR
    // --------------------

    // create an empty GemList
    public GemList()
    {
        // initialize empty list
        head = null;
        tail = null;
        size = 0;
    }


    // --------------------
    // METHODS
    // --------------------

    // return the number of gems in the list
    public int size()
    {
        // return size counter
        return size;
    }

    // draw all gems in the list at the given y-coordinate
    public void draw(double y)
    {
        Node current = head;
        int index = 0;

        double gemWidth = 1.0 / GemGame.MAX_GEMS;

        while (current != null)
        {
            double x = (index + 0.5) * gemWidth;

            current.gem.draw(x, y);

            current = current.next;
            index++;
        }
    }



    // return a string representation of the list
    public String toString()
    {
        // return arrow-separated string of gems
        Node current = head;
        String toPrint = "";
        while(current != null)
        {
            toPrint += current.gem.toString();
            if (current.next != null)
            {
                toPrint += " -> "; // only add the arrow if we arent at the end of the linked list
            }
            current = current.next;
        }

        return toPrint;
    }

    // insert the given gem before the specified index
    // if index >= size, insert at the end
    public void insertBefore(Gem gem, int index) 
    {
        Node newNode = new Node(gem, null); // make sure case matches

        // handle empty list or inserting at head
        if (index <= 0 || size == 0) 
        {
            newNode.next = head;
            head = newNode;
            if (size == 0) {
                tail = newNode;
            }
            size++;
            return;
        }

        // handle inserting in the middle
        if (index < size) 
        {
            Node prev = head;
            for (int i = 0; i < index - 1; i++) 
            {
                prev = prev.next;
            }
            newNode.next = prev.next;
            prev.next = newNode;
            size++;
            return;
        }

        // handle inserting at the end
        tail.next = newNode;
        tail = newNode;
        size++;
    }


    // calculate the total score of the list
    // applies block multipliers for consecutive same-color gems
    public int score()
    {
        int totalScore = 0;
        Node current = head;
    
        while (current != null)
        {
            int blockCounter = 0;
            int blockSum = 0;
    
            // if current is wildcard, steal the color from the next gem
            GemType blockColor = current.gem.getType();
            if (blockColor == GemType.WILDCARD && current.next != null)
            {
                blockColor = current.next.gem.getType();
            }
    
            // build the block
            while (current != null && 
                   (current.gem.getType() == blockColor || current.gem.getType() == GemType.WILDCARD))
            {
                blockCounter++;
                blockSum += current.gem.getPoints();
                current = current.next;
            }
    
            totalScore += blockSum * blockCounter;
        }
    
        return totalScore;
    }




    // --------------------
    // TESTER MAIN METHOD
    // --------------------

    public static void main(String [] args)
    {
      GemList list = new GemList();
      System.out.println(list);
      System.out.println("size = " + list.size() + ", score = " + list.score());
        list.draw(0.9);        
      
      list.insertBefore(new Gem(GemType.BLUE, 10), 0);
      System.out.println("\n" + list);
      System.out.println("size = " + list.size() + ", score = " + list.score());
      list.draw(0.8);
      
      list.insertBefore(new Gem(GemType.BLUE, 20), 99);  // not a mistake, should still work
      System.out.println("\n" + list);
      System.out.println("size = " + list.size() + ", score = " + list.score());
      list.draw(0.7);
      
      list.insertBefore(new Gem(GemType.ORANGE, 30), 1);
      System.out.println("\n" + list);
      System.out.println("size = " + list.size() + ", score = " + list.score());
      list.draw(0.6);
      
      list.insertBefore(new Gem(GemType.ORANGE, 10), 2);
      System.out.println("\n" + list);
      System.out.println("size = " + list.size() + ", score = " + list.score());
      list.draw(0.5);
      
      list.insertBefore(new Gem(GemType.ORANGE, 50), 3);
      System.out.println("\n" + list);
      System.out.println("size = " + list.size() + ", score = " + list.score());
      list.draw(0.4);
      
      list.insertBefore(new Gem(GemType.GREEN, 50), 2);
      System.out.println("\n" + list);
      System.out.println("size = " + list.size() + ", score = " + list.score());
      list.draw(0.3);        
    }
}