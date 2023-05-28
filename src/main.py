import sys
print(sys.path)

from mind.mind import Mind
from utils.utils import bce_agent_to_mind_translator
from utils.bce import BCE


if __name__ == '__main__':
    # -------------------- Test Michael
    # from rn_7_sentidos import RN_7_sentidos
    # from agente_inteligente import Agente_Inteligente
    #
    # rn_sentidos = RN_7_sentidos()
    # agente_inteligente = Agente_Inteligente()
    #
    # # Lista de eventos de entradas
    # eventos = ["evento_a", "evento_b", "evento_c", "evento_d", "evento_e", "evento_f", "evento_g", "evento_h", "evento_i"]
    #
    # # entrada de eventos a la red neuronal de michael
    # bce_7 = rn_sentidos.recibir_evento(eventos)  # -> (BCE, #RN, evento):

    mind = Mind()

    # bce for testing (Michael)
    bce = BCE()
    agent_bce = BCE()

    bce_7 = [[[0, bce], 'sight'],
             [[2, bce], 'hearing'],
             [[0, bce], 'taste'],
             [[2, bce], 'touch'],
             [[0, bce], 'body'],
             [[0, bce], 'smell']]

    rn_bce_by_senses = bce_agent_to_mind_translator(bce_senses=bce_7)
    bce_winner = mind.call_internal_comparator(agent_bce=agent_bce, bce_senses=rn_bce_by_senses)

    # memories for testing (Daniel)
    # memory = Memory()
    # memories = memory.memories

    memories = {
        'hearing': {
            'biological': "hearing:biological",
            'cultural': "hearing:cultural",
            'emotional': "hearing:emotional"
        },
        'touch': {
            'biological': "touch:biological",
            'cultural': "touch:cultural",
            'emotional': "touch:emotional"
        },
        'sight': {
            'biological': "sight:biological",
            'cultural': "sight:cultural",
            'emotional': "sight:emotional"
        },
        'smell': {
            'biological': "smell:biological",
            'cultural': "smell:cultural",
            'emotional': "smell:emotional"
        },
        'taste': {
            'biological': "taste:biological",
            'cultural': "taste:cultural",
            'emotional': "taste:emotional"
        },
        'body': {
            'biological': "body:biological",
            'cultural': "body:cultural",
            'emotional': "body:emotional"
        }
    }

    mind.update_attention(memories=memories)
