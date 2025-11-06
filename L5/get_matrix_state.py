data = open('game-of-life.txt', 'r')
lines = data.readlines()
x_size = 0
y_size = 0
x_dim = len(lines[0])//13
y_dim = len(lines)//13

start = 3,6
new_mat = []
for i in range(y_dim):
    ln_arr = []
    for j in range(x_dim):
        chars = lines[start[1]+13*i][start[0]+13*j:start[0]+13*j+7]
        if chars.count(' ') == len(chars):
            ln_arr += [0]
        else:
            ln_arr += [1]
    new_mat += [ln_arr]

with open("initial_state.txt", 'w') as f:
    for ln in new_mat:
        f.write("".join([str(b) for b in ln]))
        f.write("\n")
