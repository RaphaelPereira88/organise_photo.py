import os

def extract_place(filename):
    return filename.split('_')[1]

def make_place_directories(places): #creates a directory for each country
    for place in places:
        os.mkdir(place)

def organize_photos(directory):
    os.chdir("directory") #entre ds le directory
    originals = os.listdir() #assign ethe list to the directory
    places = []
    for filename in originals:
        place = extract_place(filename)
        if place not in places:  #pour eviter que le systeme imprime plusieurs fois le meme pays
            places.append(place)

    make_place_directories(places)

    print(os.listdir())
    for filename in originals:
        place = extract_place(filename)
        os.rename(filename, os.path.join(place, filename)) #to be able to find it in mac or PC


if __name__ == "__main__":
    organize_photos("Photos")





