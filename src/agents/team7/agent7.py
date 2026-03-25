import numpy as np
import random

from utils.track_utils import compute_curvature, compute_slope
from agents.kart_agent import KartAgent

class Agent7(KartAgent):
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

    def choose_action(self, obs):

        paths = obs['paths_end']

        if len(paths) == 0: # par défaut si aucun noeud n'est donné dans la liste paths_end
            x = 0,
            z = 8.0  
        else:
            # On calcule la vitesse actuelle pour adapter la distance de visée.
            speed = np.linalg.norm(obs['velocity'])

            # Plus on va vite, plus on regarde loin
            lookahead = 8.0 + (speed * 2.0)

            # On plafonne la visée
            lookahead = min(lookahead, 10.0)

            target_vector = paths[-1]  # Par défaut on prend le noeud le plus loin pour éviter tout bug

            # On cherche le premier point qui dépasse notre distance de visée calculée
            for p in paths:
                if p[2] > lookahead:
                    target_vector = p
                    break

            # On enregistre l'écart latéral x et l'écart avant z du point cible
            x = target_vector[0]
            z = target_vector[2]

        # On imagine ici un triangle rectangle où x est le côté opposé et z le côté adjacent
        # Pour simplifier, on utilise directement le ratio x / z comme erreur
        # plus x est grand (loin du centre), plus l'angle est grand
        error_angle = x / z

        # La dérivée mesure la vitesse à laquelle on corrige l'erreur.
        # Formule = (Erreur de maintenant) - (Erreur d'avant).
        # Elle sert d'amortisseur pour éviter les zigzags.
        error_diff = error_angle - self.last_error
        self.last_error = error_angle

        # Steering = (Force brute vers la cible * un coeff) + (Freinage pour pas dépasser * un coeff)
        steering = (error_angle * 6.0) + (error_diff * 13.0)

        # On limite entre -1 et 1
        steering_normalise = np.clip(steering, -1, 1)

        action = {
            "acceleration": 0.5,
            "steer": steering,
            "brake": False, # bool(random.getrandbits(1)),
            "drift": 0, #bool(random.getrandbits(1)),
            "nitro": 0, #bool(random.getrandbits(1)),
            "rescue": 0, #bool(random.getrandbits(1)),
            "fire": 0, #bool(random.getrandbits(1)),
        }
        return action
