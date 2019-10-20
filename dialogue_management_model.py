#from __future__ import absolute_import
#from __future__ import division
#from __future__ import print_function
#from __future__ import unicode_literals

#import logging

#from rasa_core.agent import Agent
#from rasa_core.channels.console import ConsoleInputChannel
#from rasa_core.interpreter import RegexInterpreter
#from rasa_core.policies.keras_policy import KerasPolicy
#from rasa_core.policies.memoization import MemoizationPolicy
#from rasa_core.interpreter import RasaNLUInterpreter

#logger = logging.getLogger(__name__)

#def train_dialogue(domain_file = 'mental_domain.yml',model_path = './models/dialogue',training_data_file = './data/stories.md'):
 #   agent = Agent(domain_file,policies = [MemoizationPolicy(), KerasPolicy()])
  #  agent.train(training_data_file, max_history = 5, epochs = 500, batch_size = 50, validation_split = 0.2, augmentation_factor = 50)
   # agent.persist(model_path)
    #return agent
    
#def run_mental_bot(serve_forever = True):
 #   interpreter = RasaNLUInterpreter('./models/nlu/default/mentalnlu')
  #  agent = Agent.load('./models/dialogue',interpreter = interpreter)
    
   # if serve_forever:
    #    agent.handle_channel(ConsoleInputChannel())
        
    #return agent
    
    
#if __name__ == "__main__":
 #   train_dialogue()
  #  run_mental_bot()
    
    
import logging

from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.training import interactive
from rasa_core.utils import EndpointConfig

logger = logging.getLogger(__name__)

def train_dialogue(domain_file = 'mental_domain.yml',model_path = './models/dialogue',training_data_file = './data/stories.md'):
    agent = Agent(domain_file,policies = [MemoizationPolicy(), KerasPolicy(max_history=4, epochs=1000, batch_size=50)])
    data = agent.load_data(training_data_file)
    agent.train(data)
    agent.persist(model_path)
    return agent
    
def run_mental_bot(serve_forever = True):
    interpreter = RasaNLUInterpreter('./models/nlu/default/mentalnlu')
    agent = Agent.load('./models/dialogue',interpreter = interpreter)
    training_data_file='data/stories.md'
    if serve_forever:
        interactive.run_interactive_learning(agent,training_data_file)
        
    return agent

if __name__ == "__main__":
    train_dialogue()
    run_mental_bot()
