# Importing the Libraries

from tensorflow.keras.models import load_model
import numpy as np
import pickle

# Load the model and tokenizer

model = load_model('nextword1.h5')
tokenizer = pickle.load(open('tokenizer1.pkl', 'rb'))

def Predict_Next_Words(model, tokenizer, text):
    """
        In this function we are using the tokenizer and models trained
        and we are creating the sequence of the text entered and then
        using our model to predict and return the the predicted word.
    
    """
    # for i in range(3):
    print(text)
    print(model)
    sequence = tokenizer.texts_to_sequences([text])[0]
    sequence = np.array(sequence)
    print(sequence)
    preds = model.predict(sequence)
    print(preds)
    # Convert the prediction list to a numpy array
    preds_array = np.array(preds)

    # Get the indices of the maximum values
    max_indices = np.argsort(preds_array)[0, ::-1]

    # # Extract the second and third maximum indices
    # second_max_index = max_indices[1]
    # third_max_index = max_indices[2]
    preds = max_indices[0]
    # print("Second maximum index:", second_max_index)
    # print("Third maximum index:", third_max_index)
    # print('preds: ',len(preds[0]))
    predicted_word = ""
    # print(len(tokenizer.word_index.items()))
    for key, value in tokenizer.word_index.items():
        # print('val: ',value,key)
        # print(int(value))
        # print(int(preds))
        if int(value) == int(preds):
            print(key)
            predicted_word = key
            print(predicted_word)
            break
    
    print(predicted_word)
    return predicted_word

"""
    We are testing our model and we will run the model
    until the user decides to stop the script.
    While the script is running we try and check if 
    the prediction can be made on the text. If no
    prediction can be made we just continue.

"""

# text1 = "at the dull"
# text2 = "collection of textile"
# text3 = "what a strenuous"
# text4 = "stop the script"

while(True):

    text = input("Enter your line: ")
    
    if text == "stop the script":
        print("Ending The Program.....")
        break
    
    else:
        try:
            text = text.split(" ")
            text = text[-1]

            text = ''.join(text)
            print(text)
            prr=Predict_Next_Words(model, tokenizer, text)
            print("prrr: ",prr)
            
        except:
            continue