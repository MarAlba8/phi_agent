from time import sleep

from conscious.conscious import Conscious
from subconscious.general_evaluator import general_evaluator
from subconscious.general_evaluator_bce import general_evaluator_bce
from subconscious.subconscious_by_sense import SubconsciousBySense

from settings import SENSES
from utils.bce import BCE


class Mind:
    def __init__(self):
        self.conscious = Conscious()
        senses = SENSES

        self.senses = {}
        for sense in senses:
            self.senses[sense] = SubconsciousBySense(conscious=self.conscious, sense=sense)

        self.bce_winners = {}
        self.states_new_thoughts = {}
        self.new_thoughts_by_sense = {}

    def call_internal_comparator(self, agent_bce: BCE, bce_senses: dict):
        """
        Receive all seven BCE by sense and send it to each sense accordingly
        :param agent_bce:
        :param bce_senses:
        :return: BCE that wins inside the internal comparator
        """
        for sense in self.senses:
            self.bce_winners[sense] = {}
            self.bce_winners[sense] = self.senses[sense].bce_comparator(agent_bce, bce_senses[sense])

        return self.bce_winners

    def update_attention(self, memories):

        for sense in self.senses:
            self.new_thoughts_by_sense[sense] = self.senses[sense].thought_picker(
                memories[sense]
            )

        self.states_new_thoughts = general_evaluator(
            self.new_thoughts_by_sense
        )

        ##version 2
        # for state in self.states_new_thoughts:
        len_biological = len(self.states_new_thoughts["biological"])
        len_cultural= len(self.states_new_thoughts["cultural"])
        len_emotional = len(self.states_new_thoughts["emotional"])

        max_len_state_thoughts = max(len_biological, len_cultural, len_emotional)
        for i in range(max_len_state_thoughts):
            if i < len_biological:
                thought = self.states_new_thoughts["biological"][i]
                self.conscious.update_scope(state="biological", thought=thought)

            if i < len_cultural:
                thought = self.states_new_thoughts["cultural"][i]
                self.conscious.update_scope(state="cultural", thought=thought)

            if i < len_emotional:
                thought = self.states_new_thoughts["emotional"][i]
                self.conscious.update_scope(state="emotional", thought=thought)

            sleep(1)


    def get_unified_bce(self, bce_by_senses: dict):
        unified_bce = general_evaluator_bce(
            bce_by_senses=bce_by_senses
        )
        return unified_bce

    #     self.send_thoughts_to_memory()
    #
    # def send_thoughts_to_memory(self):
    #     memory_data = {
    #         "thoughts": self.conscious.get_thoughts_in_scope()
    #     }
    #     #print(f"Sending memory data: {memory_data}")
    #    #self.memory.update_memory(memory_data)
