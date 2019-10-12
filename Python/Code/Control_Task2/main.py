import itertools

## x -> z

step = 0

def HanoiTowers(height,firstTower, secondTower, middleTower):
    if height >= 1:
        HanoiTowers(height - 1,firstTower,middleTower,secondTower)
        move(firstTower,secondTower)
        HanoiTowers(height - 1,middleTower,secondTower,firstTower)

def move(tfrom,tto):
    global step
    step += 1
    print(step, "moving disk from", tfrom, "to",tto)


def fibonacci():
    prev, cur = 0, 1
    while True:
        yield prev
        prev, cur = cur, prev + cur

def main():
    print("Fibonacci: ")
    fib = int(input())
    for i in fibonacci():
        print(i)
        if i > fib:
            break

    print("Hanoi tower: ")
    n = input()
    HanoiTowers(n,"A","B","C")

if __name__ == "__main__":
    main()