    
data =  {
        "ACC": 0.16666666666666696,
        "Big 12": 0.5833333333333339,
        "Big East": 1.0,
        "Big Ten": 0.6363636363636358,
        "Sun Belt": 0.41666666666666696,
        "CUSA": 0.3333333333333339,
        "Ind": 2.75,
        "MAC": 0.13461538461538503,
        "MWC": 0.6666666666666661,
        "Pac-10": 0.20000000000000018,
        "SEC": 1.333333333333334,
        "WAC": 1.666666666666667
    }

adjusted_data = {key: value - 0.5 for key, value in data.items()}
