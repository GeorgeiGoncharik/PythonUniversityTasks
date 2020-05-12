import random

if __name__ == "__main__":
    with open('numbers', 'w') as f:
        f.writelines('{}\n'.format(random.randint(-1000000, 1000000)) for _ in range(500000000))
