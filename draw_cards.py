import random
import numpy as np

random_cards=np.random.choice(range(19,37), size=6, replace=False)
random_cards=np.sort(random_cards)
print(f"Random cards: {random_cards}")

murder_cards=np.random.choice(random_cards,size=2,replace=False)
print(f"Murder cards {np.sort(murder_cards)}")
