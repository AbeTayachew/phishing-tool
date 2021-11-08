from .schema import Text
import pickle
from model_creation import clean_address, clean_body, clean_text
class Service(object):

  def processText(text):
    print("processing...")
    print(text)
	# Accessing and converting text content. Stored in list so value can be fed to trained model
    cleanedTextContent = [clean_text(text.get("content"))]

    # Loading trained classification model
    textModel = pickle.load(open("text_class_model.sav", 'rb'))

    # Getting prediction with probability
    #textPrediction = textModel.predict_proba(cleanedTextContent)
    textPrediction = textModel.predict(cleanedTextContent)
    return textPrediction

  def processEmail(email):
    # Accessing and converting email components. These are stored in lists so that their values can be fed to our trained model to predict on
    cleanedAdd = [clean_address(email.get("email_address"))]
    cleanedSub = [clean_body(email.get("subject_line"))]
    cleanedBod = [clean_body(email.get("content"))]

    # Loading trained class models
    addModel = pickle.load(open("address_class_model.sav", 'rb'))
    subModel = pickle.load(open("subject_class_model.sav", 'rb'))
    bodModel = pickle.load(open("body_class_model.sav", 'rb'))

    # Getting predictions with probability
    #addPrediction = addModel.predict_probs(cleanedAdd)
    #subPrediction = subModel.predict_probs(cleanedSub)
    #bodPrediction = bodModel.predict_probs(cleanedBod)
    addPrediction = addModel.predict(cleanedAdd)
    subPrediction = subModel.predict(cleanedSub)
    bodPrediction = bodModel.predict(cleanedBod)
    # Creating aggregate prediction
    if addPrediction + subPrediction + bodPrediction >= 2:
      #Using a two thirds majority to decide if spam or not
      return 1
    else:
      return 0

