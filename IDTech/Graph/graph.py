import numpy as np
import matplotlib.pyplot as plt

data = {
    "Suits": 100,
    "Breaking Bad": 50,
    "Doctor Who": 100,
    "Fallout": 10,
    "Loki": 20,
    "The Simpsons": 200,
}

shows = list(data.keys())
episodes = list(data.values())
fig = plt.figure(figsize = (10, 5))


plt.bar(shows, episodes, color = "green", width = 0.8)
plt.show()