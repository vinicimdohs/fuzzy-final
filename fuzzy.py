import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def fuzzy(vacantArray : list[dict[str, any]],vacant_raisonnement_form,vacant_physique_form,vacant_public_form):
    # QUAL ARRANGE DEVO COLOCAR ??
    raisonnemet = ctrl.Antecedent(np.arange(0,11,1),'raciocinio')
    public = ctrl.Antecedent(np.arange(0,11,1),'publico')
    physique = ctrl.Antecedent(np.arange(0,11,1),'vigor')

    raisonnemet.automf(number=3,names=['baixo','medio','alto'])
    public.automf(number=3,names=['baixo','medio','alto'])
    physique.automf(number=3,names=['baixo','medio','alto'])

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
        
        vagas[v_name] = fuzz.trimf(vagas.universe,[weighted_average * 0.1,weighted_average * 5,weighted_average * 9.9])

        # weighted_average_vacant = ((vacant_raisonnement_form * 99) + (vacant_public_form * 50) + (vacant_physique_form * 1))/(99 + 50 + 1)
        # DEFINIR AS REGRAS COMPARAR O VALOR INPUTADO : BAIXO||MEDIO|ALTO , com os valores da vaga para DEFINIR AS REGRAS
        # if weighted_average_vacant < 3.3:
        raisonnemet_rule = 'baixo' # || medio || alto
        public_rule = 'medio' # || baixo || alto
        physique_rule = 'alto' # baixo || medio

        #Se a média do caboco tá batendo com a média da vaga, então pimba
        rule = ctrl.Rule(raisonnemet[raisonnemet_rule]| public[public_rule] | physique[physique_rule], vagas[v_name]) 
        rule2 = ctrl.Rule(raisonnemet[raisonnemet_rule]| public[public_rule] | physique[physique_rule], vagas[v_name])
        rule3 = ctrl.Rule(raisonnemet[raisonnemet_rule]| public[public_rule] | physique[physique_rule], vagas[v_name])
        rules.append(rule)

    vagas.view()    
    
    recomendacao_vaga = ctrl.ControlSystem(rules)

    recomendacao = ctrl.ControlSystemSimulation(recomendacao_vaga)

    recomendacao.input['raciocinio'] = vacant_raisonnement_form
    recomendacao.input['publico'] = vacant_public_form
    recomendacao.input['vigor'] = vacant_physique_form

    recomendacao.compute()

    vagas.view(sim = recomendacao)

