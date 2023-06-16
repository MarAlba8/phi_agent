import threading
from time import sleep

from conscious.scope import Scope


class Conscious:

    def __init__(self):
        self.biological_scope = Scope("biological")
        self.cultural_scope = Scope("cultural")
        self.emotional_scope = Scope("emotional")

        self.biological_phi = None
        self.cultural_phi = None
        self.emotional_phi = None

        self._scopes = {
            "biological": self.biological_scope,
            "cultural": self.cultural_scope,
            "emotional": self.emotional_scope
        }

        self._phi_windows = {
            "biological": self.biological_phi,
            "cultural": self.cultural_phi,
            "emotional": self.emotional_phi
        }

        # Llamar nuevo hilo
        self._initiate_consciousness()

    def _initiate_consciousness(self):
        print("starting consciousness")
        def show_current_thought():
            while True:
                print("phi windows")
                print(self._phi_windows)
                self.update_phis()

        thread = threading.Thread(target=show_current_thought)
        thread.start()

    def get_phis(self):
        return self._phi_windows

    def update_phis(self, state=None, thought=None):
        if thought and state:
            self._phi_windows[state] = thought
            ## TODO: call Memory
        else:
            states = self._phi_windows.keys()
            for state in states:
                new_thought = self._scopes[state].get_next_thought()
                self._phi_windows[state] = new_thought

        sleep(1)

        ##TODO: Update memory in

    def update_scope(self, state: str, thoughts: list):
        scope = self._scopes[state]

        for thought in thoughts:
            has_thought = self.is_a_repeated_thought(
                scope=scope,
                thought=thought
            )
            if not has_thought:
                scope.add_new_thought(thought=thought)

            self.update_phis(state, thought)

    def is_a_repeated_thought(self, scope: Scope, thought: str):
        has_thought = scope.has_thought(thought=thought)
        return has_thought

    def get_thoughts_in_scope(self):
        thoughts = []
        for state in self._scopes:
            scope = self._scopes[state]
            thoughts.append(scope.get_current_thoughts())
        return thoughts
