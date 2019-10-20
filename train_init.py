from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals


from rasa_core.policies import FallbackPolicy, KerasPolicy, MemoizationPolicy
from rasa_core.agent import Agent
from tensorflow.python.framework import ops
ops.reset_default_graph()


import logging

if __name__ == '__main__':
	logging.basicConfig(level='INFO')
	
	#training_data_file = agent.load_data('./data/stories.md')
	#model_path = './models/dialogue'
	
	agent = Agent('mental_domain.yml', policies = [MemoizationPolicy(), KerasPolicy(epochs=1000, batch_size=50)])
	training_data_file = agent.load_data('./data/stories.md')
	agent.train(
			training_data_file)
			#epochs = 1000,
			#validation_split = 0.2)
			
	agent.persist('./models/dialogue')

