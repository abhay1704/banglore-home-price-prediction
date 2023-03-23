import pickle
import numpy as np

__model =None
__location_encoder = None
__location_list = None


def load_assests():
    global __model
    global __location_encoder
    global __location_list

    with open('assets/banglore_price_prediction_model.pickle', 'rb') as f:
        __model = pickle.load(f)
    with open('assets/location_encoder.pickle', 'rb') as ld:
        __location_encoder= pickle.load(ld)
    __location_list = __location_encoder.categories_[0]

def get_estimated_price(location,bhk,tsqft,bath):
    try:
        x = __location_encoder.transform([[location]]).toarray()[0]
    except:
        x = np.zeros(len(__location_list))

    x = np.append(x[1:], np.array([bhk, tsqft, bath]))
    return __model.predict(x.reshape(1, -1))[0]

# load_assests()
# get_estimated_price('Devarabeesana Halli', 2, 1100.0, 2.0)
