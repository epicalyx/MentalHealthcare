#from rasa_nlu.training_data import load_data
#from rasa_nlu import config
#from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter

#def train_nlu(data,config,model_dir):
    #training_data = load_data(data)
    #trainer = Trainer(config.load("config.yml"))
    #trainer.train(training_data)
    #model_directory = trainer.persist(model_dir, fixed_model_name = 'mentalnlu')
    
    
#def run_nlu():
    #interpreter = Interpreter.load('./models/nlu/default/mentalnlu',config.load('config.yml'))
    #print(interpreter.parse(u"I am depressed today."))
#if __name__ == "__main__":
    #train_nlu('./data/nlu.md','config.yml','./models/nlu')
    #run_nlu()
    
from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config

# loading the nlu training samples
training_data = load_data("./data/nlu.md")

# trainer to educate our pipeline
trainer = Trainer(config.load("config.yml"))

# train the model!
interpreter = trainer.train(training_data)

# store it for future use
model_directory = trainer.persist("./models/nlu", fixed_model_name="mentalnlu")

#interpreter = Interpreter.load('./models/nlu/default/mentalnlu',config.load('config.yml'))
#print(interpreter.parse(u"I am depressed today."))


from rasa_nlu.test import run_evaluation
run_evaluation("./data/nlu.md", model_directory)