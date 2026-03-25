import numpy as np
import random

from utils.track_utils import compute_curvature, compute_slope
from agents.kart_agent import KartAgent

class Agent1(KartAgent):
    def __init__(self, env, path_lookahead=3):
        super().__init__(env)
        self.path_lookahead = path_lookahead
        self.agent_positions = []
        self.obs = None
        self.isEnd = False
        self.name = "Rayan Ibrahim" # On met mon nom et prénom
        self.last_error = 0.0

    def reset(self):
        self.obs, _ = self.env.reset()
        self.agent_positions = []
        self.last_error = 0.0

    def endOfTrack(self):
        return self.isEnd

    def choose_action(self, obs, steps):



        # Si on a fait 200 steps alors on recule
        if steps >= 59:
            accel = 0
            brake = True
            
            # paths starts renvoie la liste des noeuds avant le kart, si la liste est vide par défaut on met le steering à 0
            if len(obs["paths_end"][-1]) <= 0:
                steering = 0
            else:
                # sinon si on est à gauche du point on tourne à droite 
                if obs["paths_end"][-1][0] < 0:
                    print("negatif")
                    steering = -0.43
                else: # et si on est à droite on tourne à gauche
                    print("positif")
                    steering = 0.43
        else: # Sinon on tourne
            steering = 1.0
            accel = 0.2
            brake = False

        action = {
            "acceleration": accel,
            "steer": steering,
            "brake": brake, # bool(random.getrandbits(1)),
            "drift": 0, #bool(random.getrandbits(1)),
            "nitro": 0, #bool(random.getrandbits(1)),
            "rescue": 0, #bool(random.getrandbits(1)),
            "fire": 0, #bool(random.getrandbits(1)),
        }
        return action
