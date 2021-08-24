n = int(input())

stars = [[' ' for _ in range(n)] for _ in range(n)]

def draw(size, x, y):
    global stars
    if size == 1:
        stars[y][x] = '*'

    else:
        next_size = size // 3
        for dy in range(3):
            for dx in range(3):
                if dx != 1 or dy !=1 :
                    draw(next_size, x+dx*next_size, y+dy*next_size)


draw(n,0,0)
for star in stars:
    print(''.join(star))
