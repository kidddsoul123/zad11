import random

def generate_random_list(num_elements):
    random_list = [random.randint(5, 600) for _ in range(num_elements)]
    return random_list

num_elements = 16
random_list = generate_random_list(num_elements)
print(random_list)