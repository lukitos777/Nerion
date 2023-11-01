import eel

buckets: list = [0 for i in range(5)]
pointer = 0
res = ''

def run(code: str):
    global pointer, res, buckets
    for el in code:
        if el == '>': pointer += 1
        elif el == '<': pointer -= 1
        elif el == '+': buckets[pointer % 5] += 1
        elif el == '-': buckets[pointer % 5] -= 1
        elif el == '^': buckets[pointer % 5] *= 2
        elif el == '_': buckets[pointer % 5] //= 2
        elif el == '.': res += chr(buckets[pointer % 5])

@eel.expose
def get_code(code: str):
    global pointer, buckets
    with open('file.txt', 'w') as file:
        file.write(code)
    with open('file.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            run(line)
    update_text()
    pointer = 0
    buckets = [0, 0, 0, 0, 0]

@eel.expose
def update_text():
    global res
    eel.set_text(res)
    res = ''


def main():
    eel.init('web')
    eel.start('index.html', mode='edge', size=(700, 850))

if __name__ == '__main__':
    main()