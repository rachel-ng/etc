from decimal import Decimal


def conversion_function(category: str, activity: str, usage: Decimal): 
    
    rates = {
      'Bus' : 0.105,
      'Car' : 0.404,
      'Plane' : 0.21463,
      'Train' : 0.125, 
      'Boat' : 3.211,
      'Bike' : 0,
      'Walk' : 0,
      'Light' : 0.72595490867,
      'Heat' : 0.309
    }
    # rates = {'gasoline': 8.887,
    #  'diesel': 10.18,
    #  'mile': 0.404,
    #  'sedan': 0.3773,
    #  'SUV': 0.44521,
    #  'Urban bus': 0.08298,
    #  'commuter rail': 0.171,
    #  'light rail': 0.17178,
    #  'hybrid light rail': 0.06834,
    #  'small aircraft': 0.29349,
    #  'midsize aircraft': 0.21463,
    #  'large aircraft': 0.19826,
    #  'plug-in hybrid': 0.06949,
    #  'train rapid transit': 0.125,
    #  'bus rapid transit': 0.105,
    #  'Boeing 737': 0.27,
    #  'household time': 0.72595490867,
    #  'natural gas': 116.06198,  #monthly
    #  'fuel oil': 183.21995,  #monthly
    #  'waste': 26.152683,  #monthly
    #  'recycling': -3.3779,  #monthly 
    #  'recycling plastic': -1.343915,  #monthly
    #  'recycling glass': -0.959562,  #monthly
    #  'recycling newspapers': -4.275888,  #monthly
    #  'recycling magazines': -1.037793,  #monthly
    #  'replacing boiler': -67.4222525,  #monthly
    #  'passenger mile': 0.41138322
    # }


    
    
    result = usage * Decimal(rates[activity])
    
    
    # print(f"\n[{category}] {activity}\n\tusage: {usage}\n\tconverted: {result}")

    return result
  