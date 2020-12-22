import os

def extract_place(filename):
    return filename.split('_')[1]

def make_place_directories(places):        #creates a directory for each country
    for place in places:
        os.mkdir(place)

def organize_photos(directory):
    os.chdir("directory")                   #choose  directory
    originals = os.listdir()                #assign the list to the directory
    places = []
    for filename in originals:
        place = extract_place(filename)
        if place not in places:             #for the program to avoird creating duplicates files.
            places.append(place)

    make_place_directories(places)

    for filename in originals:
        place = extract_place(filename)
        os.rename(filename, os.path.join(place, filename))        #to be able to find it in mac or PC


if __name__ == "__main__":
    organize_photos("Photos")





