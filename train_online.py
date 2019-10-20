#from __future__ import absolute_import
#from __future__ import division
#from __future__ import print_function
#from __future__ import unicode_literals

#import logging

#from rasa_core.agent import Agent
#from rasa_core.channels.console import ConsoleInputChannel
#from rasa_core.interpreter import RegexInterpreter
#from rasa_core.policies import FallbackPolicy, KerasPolicy, MemoizationPolicy
#from rasa_core.interpreter import RasaNLUInterpreter

#logger = logging.getLogger(__name__)


#def run_mental_online(input_channel, interpreter,
 #                         domain_file="mental_domain.yml",
  #                        training_data_file='data/stories.md'):
   # agent = Agent(domain_file,
    #              policies=[MemoizationPolicy(), KerasPolicy()],
     #             interpreter=interpreter)

#    agent.train_online(training_data_file,
 #                      input_channel=input_channel,
  #                     max_history=2,
   #                    batch_size=50,
    #                   epochs=200,
     #                  max_training_samples=300)

    #return agent


#if __name__ == '__main__':
 #   logging.basicConfig(level="INFO")
    #nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/mentalnlu')
    #run_mental_online(ConsoleInputChannel(), nlu_interpreter)
    
    
    
    
    
    
    
#from future import absolute_import
#from future import division
#from future import print_function
#from future import unicode_literals

import logging

from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.training import interactive
from rasa_core.utils import EndpointConfig

logger = logging.getLogger(__name__)

def run_mental_online(interpreter,
domain_file="mental_domain.yml",
training_data_file='data/stories.md'):
    action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
    agent = Agent(domain_file,
        policies=[MemoizationPolicy(max_history=2), KerasPolicy(max_history=4, epochs=1000, batch_size=50)],
        interpreter=interpreter,
        action_endpoint=action_endpoint)
    data = agent.load_data(training_data_file)			   
    agent.train(data)
    interactive.run_interactive_learning(agent, training_data_file)
    return agent

if __name__ == '__main__':
    logging.basicConfig(level="INFO")
    nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/mentalnlu')
    run_mental_online(nlu_interpreter)
