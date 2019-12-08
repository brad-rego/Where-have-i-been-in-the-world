# this is the main file for the colourful map generatior
#Bradley Rego 2019
import os
from visited_countries import visited_countries
from countries import list_Countries


def randomColourGenerator():
    return [random.randint(1,255),random.randint(1,255),random.randint(1,255)]

#reset the visited_countries
def reset():
    list_Countries.clear()
#converstions pdf and png
#if cairo is not installed this will produce an error
def conversion(scale,conversion_type):
    try:
        import cairo
    except ImportError as ex:
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

def getCode(country):
    print(list_Countries.keys())
    return list_Countries.get(country)

# def loop(selected, countries_visited):
#     for i in countries_visited:
#         if countries_visited == selected:
#
#
def main():
    while True:
        country = input("enter the countries you have been to, enter 'finished' when you are done. \n")
        if country == "finished":
            break
        else:
            # call country code finder
            code = getCode(country)
            if code == None:
                print("invalid Country, please type it in again")
            # add code to list
            visited_countries.append(code)

    #open world map
    with open(getMap()) as map:
        world_map = map.read()
    #countries list
    edits = list()
    for country in list_Countries.values():
        for i in countries_visited:
            if i  == country:
                x  = randomColourGenerator()
                colour = "rgb({},{},{})".format(x[0],x[1],x[2])
                code.append("#{} {{fill: {};}}".format(country, colour))

    map = world_map.replace("<!-- PYTHON Style1 -->", "\n".join(code))


    #write the changes:
    with open("output.svg", "w") as out_file:
        out_file.write(world_map)
    conversion(1,"png")

if __name__ == "__main__":
    main()
