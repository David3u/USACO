import java.io.*;
import java.util.*;

public class Div7 {
   public static void main(String[] args) throws IOException {
      BufferedReader br = new BufferedReader(new FileReader("div7.in"));

      int cn = Integer.parseInt(br.readLine());
      int[] cows = new int[cn];

      for (int i = 0; i < cn; i++) {
         cows[i] = Integer.parseInt(br.readLine());
      }
      
      br.close();

      List<Integer> l = new ArrayList<>();
      l.add(0);
      int longest = 0;

      for (int e : cows) {
         int val = (l.get(l.size() - 1) + e) % 7;
         l.add(val);
         int dist = l.size() - 1 - l.indexOf(val);
         if (dist > longest) {
               longest = dist;
         }
      }

      BufferedWriter bw = new BufferedWriter(new FileWriter("div7.out"));
      bw.write(Integer.toString(longest));
      bw.close();
   }
}
