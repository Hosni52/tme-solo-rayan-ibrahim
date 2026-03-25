import numpy as np
import random

from utils.track_utils import compute_curvature, compute_slope
from agents.kart_agent import KartAgent


class Agent6(KartAgent):
    def __init__(self, env, path_lookahead=3):
        super().__init__(env)
        self.path_lookahead = path_lookahead
        self.agent_positions = []
        self.obs = None
        self.isEnd = False
        self.name = "Rayan Ibrahim" # On met mon prénom et mon nom dans agent 6

    def reset(self):
        self.obs, _ = self.env.reset()
        self.agent_positions = []

    def endOfTrack(self):
        return self.isEnd

    def choose_action(self, obs):
        acceleration = random.random()
        steering = random.random()
        action = {
            "acceleration": 0.2, # mettre une acceleration constante pour tourner sur lui même
            "steer": 1.0, # On met un steer constant
            "brake": False, # bool(random.getrandbits(1)),
            "drift": 0,
            "nitro": 0, #bool(random.getrandbits(1)),
            "rescue":0, #bool(random.getrandbits(1)),
            "fire":  0, #bool(random.getrandbits(1)),
        }
        return action
