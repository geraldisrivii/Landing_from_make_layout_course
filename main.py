import os
initial_names = sorted(os.listdir("initial"))
new_names = sorted(os.listdir("src/img"))
for index in range(len(initial_names)):
    os.rename("src/img/" + new_names[index], "src/img/" + initial_names[index][:-4] + ".webp")
