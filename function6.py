# create a unction that convert km into miles


def convert_km(kilometers):
    miles=0.621371*kilometers
    return(f"{kilometers} kilometer is = {miles} miles")
    

print(convert_km(2))