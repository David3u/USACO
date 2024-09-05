import java.io.*;
import java.util.*;

public class maxcross {
   public static void main(String[] args) throws IOException {
      BufferedReader br = new BufferedReader(new FileReader("maxcross.in"));
      StringTokenizer st = new StringTokenizer(br.readLine());

      int lights = Integer.parseInt(st.nextToken());
      int intv = Integer.parseInt(st.nextToken());
      int broken = Integer.parseInt(st.nextToken());

      Set<Integer> brokenLights = new HashSet<>();
      for (int i = 0; i < broken; i++) {
         brokenLights.add(Integer.parseInt(br.readLine()));
      }
      br.close();

      int[] ll = new int[lights + 1];
      for (int i = 1; i <= lights; i++) {
         ll[i] = ll[i - 1];
         if (!brokenLights.contains(i)) {
               ll[i]++;
         }
      }

      int best = lights;
      for (int i = 0; i <= lights - intv; i++) {
         int brokenCount = intv - (ll[i + intv] - ll[i]);
         best = Math.min(best, brokenCount);
      }

      BufferedWriter bw = new BufferedWriter(new FileWriter("maxcross.out"));
      bw.write(String.valueOf(best));
      bw.close();
   }
}
