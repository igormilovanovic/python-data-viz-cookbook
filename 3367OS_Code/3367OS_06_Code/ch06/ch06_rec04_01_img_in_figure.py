import matplotlib.pyplot as plt
from matplotlib._png import read_png
from matplotlib.offsetbox import TextArea, OffsetImage, \
     AnnotationBbox


def load_data():
    import csv
    with open('pirates_temperature.csv', 'r') as f:
        reader = csv.reader(f)
        header = reader.next()
        datarows = []
        for row in reader:
            datarows.append(row)
    return header, datarows


def format_data(datarows):
    years, temps, pirates = [], [], []
    for each in datarows:
        years.append(each[0])
        temps.append(each[1])
        pirates.append(each[2])
    return years, temps, pirates

if __name__ == "__main__":
    fig = plt.figure(figsize=(16,8))
    ax = plt.subplot(111)  # add sub-plot

    header, datarows = load_data()
    xlabel, ylabel, _ = header
    years, temperature, pirates = format_data(datarows)
    title = "Global Average Temperature vs. Number of Pirates"

    plt.plot(years, temperature, lw=2)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)    
    
    # for every data point annotate with image and number
    for x in xrange(len(years)):
        # current data coordinate
        xy = years[x], temperature[x]

        # add image
        ax.plot(xy[0], xy[1], "ok")

        # load pirate image 
        pirate = read_png('tall-ship.png')

        # zoom coefficient (move image with size) 
        zoomc = int(pirates[x]) * (1 / 90000.)

        # create OffsetImage 
        imagebox = OffsetImage(pirate, zoom=zoomc)

        # create anotation bbox with image and setup properties
        ab = AnnotationBbox(imagebox, xy,
                        xybox=(-200.*zoomc, 200.*zoomc),
                        xycoords='data',
                        boxcoords="offset points",
                        pad=0.1,
                        arrowprops=dict(arrowstyle="->",
                            connectionstyle="angle,angleA=0,angleB=-30,rad=3")
                        )
        ax.add_artist(ab)

        # add text
        no_pirates = TextArea(pirates[x], minimumdescent=False)
        ab = AnnotationBbox(no_pirates, xy,
                        xybox=(50., -25.),
                        xycoords='data',
                        boxcoords="offset points",
                        pad=0.3,
                        arrowprops=dict(arrowstyle="->",
                            connectionstyle="angle,angleA=0,angleB=-30,rad=3")
                        )
        ax.add_artist(ab)

    plt.grid(1)
    plt.xlim(1800, 2020)
    plt.ylim(14, 16)
    plt.title(title)
    plt.show()
