import java.io.*;
import java.util.*;

public class hps {

   private static int get_intv(List<Integer> list, int start, int end) {
      return list.get(end) - list.get(start - 1);
   }

   public static void main(String[] args) throws IOException {

      BufferedReader br = new BufferedReader(new FileReader("hps.in"));

      int num = Integer.parseInt(br.readLine());

      List<Integer> h_list = new ArrayList<>(Collections.singletonList(0));
      List<Integer> p_list = new ArrayList<>(Collections.singletonList(0));
      List<Integer> s_list = new ArrayList<>(Collections.singletonList(0));

      for (int i = 0; i < num; i++) {
         h_list.add(h_list.get(h_list.size() - 1));
         p_list.add(p_list.get(p_list.size() - 1));
         s_list.add(s_list.get(s_list.size() - 1));

         String move = br.readLine();

         if (move.equals("S")) {
               s_list.set(s_list.size() - 1, s_list.get(s_list.size() - 1) + 1);
         } else if (move.equals("H")) {
               h_list.set(h_list.size() - 1, h_list.get(h_list.size() - 1) + 1);
         } else if (move.equals("P")) {
               p_list.set(p_list.size() - 1, p_list.get(p_list.size() - 1) + 1);
         }
      }

      br.close();

      int best_value = Math.max(Math.max(s_list.get(s_list.size() - 1), h_list.get(h_list.size() - 1)), p_list.get(p_list.size() - 1));

      for (int e = 1; e <= num; e++) {
         int curr_value = Math.max(
               Math.max(get_intv(h_list, 1, e), get_intv(s_list, 1, e)),
               get_intv(p_list, 1, e)
         ) + Math.max(
               Math.max(get_intv(h_list, e, num), get_intv(s_list, e, num)),
               get_intv(p_list, e, num)
         );

         if (curr_value > best_value) {
               best_value = curr_value;
         }
      }

      BufferedWriter bw = new BufferedWriter(new FileWriter("hps.out"));
      bw.write(String.valueOf(best_value));
      bw.close();
   }
}
