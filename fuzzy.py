import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def fuzzy(vacantArray : list[dict[str, any]],vacant_raisonnement_form,vacant_physique_form,vacant_public_form):
    weighted_average_candidate = ctrl.Antecedent(np.arange(0,11,1),'average')

    weighted_average_candidate.automf(number=3,names=['fisico','social','intelectual'])

    # QUAL ARRANGE DEVO COLOCAR
    vagas = ctrl.Consequent(np.arange(0,100,1),'vagas')

    automf_names = []
    rules = []
    for vacant in vacantArray:
        v_name = vacant.get('vacant_name')
        v_raisonnement = vacant.get('vacant_raisonnement') # mais a direita 
        v_public = vacant.get('vacant_public') # meio
        v_physique = vacant.get('vacant_physique') # mais a esquerda
        
        automf_names.append(v_name)
        
        weighted_average = ((v_raisonnement * 99) + (v_public * 50) + (v_physique * 1))/(99 + 50 + 1)
        
        vagas[v_name] = fuzz.trimf(vagas.universe,[weighted_average * 1,weighted_average * 5,weighted_average * 9.9])

        if (v_physique/(v_public + v_raisonnement)) >= 0.5 : 
            rules.append(ctrl.Rule(weighted_average_candidate['fisico'], vagas[v_name]))
        if (v_public/(v_physique + v_raisonnement)) >= 0.5 :
            rules.append(ctrl.Rule(weighted_average_candidate['social'], vagas[v_name]))
        if (v_raisonnement/(v_physique + v_public)) >= 0.5 : 
            rules.append(ctrl.Rule(weighted_average_candidate['intelectual'], vagas[v_name]))

    vagas.view()    
    
    recomendacao_vaga = ctrl.ControlSystem(rules)

    recomendacao = ctrl.ControlSystemSimulation(recomendacao_vaga)

    recomendacao.input['average'] = ((vacant_raisonnement_form * 99) + (vacant_public_form * 50) + (vacant_physique_form * 1))/(99 + 50 + 1)
   
    recomendacao.compute()

    vagas.view(sim = recomendacao)

