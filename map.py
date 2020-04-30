# this is the main file for the colourful map generatior
#Bradley Rego 2019
#imports
import os
import random
#getting dictonary and list from other files
from visited_countries import visited_countries
from countries import list_Countries
from difflib import get_close_matches

def get_possible_countries(name):
    return get_close_matches(name, list_Countries.keys(), n=3)

#generates number between 1 and 255
def randomColourGenerator():
    return [random.randint(1,255),random.randint(1,255),random.randint(1,255)]

#reset the visited_countries
def reset():
    list_Countries.clear()

#converstions pdf and png
#if cairo is not installed this will produce an error
def conversion(scale,conversion_type):
    try:
        import cairosvg
    except ImportError as ex:
        print(ex)
        print("Import Error, Please install cairo by typing: \n pip3 install cairo")
        return
    if conversion_type == "png":
        cairosvg.svg2png(url="output.svg",
                    write_to="output.png",
                    parent_width=1024,
                    parent_height=660,
                    scale=scale)
    if conversio_type == "pdf":
        cairosvg.svg2pdf(url="output.svg",
                    write_to="output.pdf",
                    parent_width=1024,
                    parent_height=660,
                    scale=scale)
def getMap():
    filename = 'worldHigh.svg'
    path =  os.path.join("WorldMap",filename)
    return path

#returns the countries 2 character code or None if it does not exist
def getCode(country):
    return list_Countries.get(country)

# Main Function
def main():
    while True:
        country = input("enter the countries you have been to, enter 'done' when you are done. \n")
        if country == "done":
            break
        else:
            # call country code finder
            code = getCode(country)
            if code == None:
                possible_countries = get_possible_countries(country)
                if possible_countries:
                    print("Invalid country, did you mean one of these: {}".format(", ".join(possible_countries)))
                    print("\n".join(possible_countries))
                else:
                    print("invalid Country, please type it in again")
            # add code to list
            visited_countries.append(code)

    #open world map
    with open(getMap()) as map:
        world_map = map.read()
    #countries list
    edits = list()
    for country in list_Countries.values():
        for i in visited_countries:
            if i  == country:
                x  = randomColourGenerator()
                colour = "rgb({},{},{})".format(x[0],x[1],x[2])
                y = "#{} {{fill: {};}}".format(country, colour)
                edits.append(y)
    #add edits to the world map
    world_map = world_map.replace("<!-- EDITS GO HERE -->", "\n".join(edits))


    #write the changes:
    with open("output.svg", "w") as out_file:
        out_file.write(world_map)

    # convert file
    #ask for what file they want
    imageType = input("What File type would you like, Insert 'PNG' for PNG, or 'PDF' for PDF or 'SVG' for SVG. \n")
    imageType.lower()
    if imageType != "svg":
        conversion(1,imageType)


if __name__ == "__main__":
    main()
