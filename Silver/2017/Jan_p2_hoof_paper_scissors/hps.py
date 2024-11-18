f = open("hps.in", "r")
fl = f.read().split("\n")

num = int(fl.pop(0))

h_list = [0]
p_list = [0]
s_list = [0]

for _ in range(num):
   h_list.append(h_list[-1])
   p_list.append(p_list[-1])
   s_list.append(s_list[-1])

   i = fl.pop(0)

   if i == "S":
      s_list[-1] += 1

   elif i == "H":
      h_list[-1] += 1
   
   elif i == "P":
      p_list[-1] += 1

best_value = max(s_list[-1], h_list[-1], p_list[-1])

def get_intv(l,s,e):
   return l[e] - l[s-1]

for e in range(1,num + 1):
   curr_value = max(
      get_intv(h_list,1,e),
      get_intv(s_list,1,e),
      get_intv(p_list,1,e)
   ) + max(
      get_intv(h_list,e,num),
      get_intv(s_list,e,num),
      get_intv(p_list,e,num)
   )

   if curr_value > best_value:
      best_value = curr_value

with open("hps.out", "w") as f:
   f.write(str(best_value))