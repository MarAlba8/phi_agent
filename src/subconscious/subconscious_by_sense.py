from conscious.conscious import Conscious
from utils.bce import BCE


class SubconsciousBySense:
    def __init__(self, conscious: Conscious, sense: str):
        self.sense = sense
        self.conscious = conscious

        self.bce_winners = {}
        self.bce_modified = {}

    def start_process(self, memories: dict):
        current_thoughts = self.conscious.get_phis()

        ##TODO: Ask for memories to Daniel
        ## sending self.states_modified


        new_thoughts = self.thought_picker(memories, current_thoughts, self.bce_modified)
        return new_thoughts

    def bce_comparator(self, agent_bce: BCE, neuronal_network_bce: dict):
        for state in neuronal_network_bce.keys():
            rn_value = neuronal_network_bce[state]
            if state == "biological":
                agent_value = agent_bce.biologico
            elif state == "cultural":
                agent_value = agent_bce.cultural
            elif state == "emotional":
                agent_value = agent_bce.emocional

            if rn_value > agent_value:
                self.bce_winners[state] = rn_value
                self.bce_modified[state] = 1
            elif agent_value > rn_value:
                self.bce_winners[state] = agent_bce
                self.bce_modified[state] = 0

        # TODO: Aplicar logica difusa

        return self.bce_winners

    # def primary_evaluator(self, agent_states: dict, new_states: dict):
    #     bce_modified = self.bce_modified
    #
    #     for state in agent_states:
    #         if agent_states[state] != new_states[state]:
    #             bce_modified[state] = 1
    #         else:
    #             bce_modified[state] = 0
    #
    #     return bce_modified

    def thought_picker(self, memories: dict, current_thoughts: dict, states_modified: dict):
        """
        #Multiplexor
        Take memories and current thoughts, for those states that were modified by a memory
        creates a new thought and remove the old ones
        :param memories: data from the memory
        :param current_thoughts: current thoughts inside phi windows
        :param states_modified: have what states were modified by a memory and those
        that weren't
        :return: Descriptors of the new thoughts
        """

        new_thoughts = {}
        for state in current_thoughts:
            if states_modified[state]:
                new_thoughts[state] = memories[state]  # solo regresa los estados que se actualizaron
        return new_thoughts
