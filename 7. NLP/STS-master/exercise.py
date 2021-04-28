# Can you figure out how to get the embeddings?

# take a look at the shape of the target 
# take a look at the shape of the output
# take a look at the shape of the embedding


# for "yellow"  and "blue" extract the tokens
# put them into a tensor
# get the embeddings of those 2 words
# use np.inner to get the semantic simmilarity 
# what about blue and car?

# can you come up with a different way of computing the semantic simmilarity?

import torch
import numpy as np
import data_handler as dh
model = torch.load('transformer_model1.pth', map_location=torch.device('cpu'))

_,_,_,vocab = dh.get_data()

# index (dtype = int) of the word (token) return from vocab

yellow = vocab['yellow']
blue = vocab['blue']
car = vocab['car']
print('Index of word yellow is: ',yellow)
print('Index of word blue is: ',blue)
print('Index of word car is: ',car)

# convert the index into tensor 

yellow = torch.tensor(yellow)
blue = torch.tensor(blue)
car = torch.tensor(car)


# get the embeddings of the words

yellow = model.encoder(yellow)
blue = model.encoder(blue)
car = model.encoder(car)

# convert the embeddings into numpy array
yellow = yellow.detach().numpy()
blue = blue.detach().numpy()
car = car.detach().numpy()

print('Similarity b/w yellow and blue is: ',np.inner(yellow,blue))
print('Similarity b/w blue and car is: ',np.inner(blue,car))

