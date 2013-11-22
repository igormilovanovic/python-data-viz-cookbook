import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# properties:
families = ['serif', 'sans-serif', 'cursive', 'fantasy', 'monospace']
sizes  = ['xx-small', 'x-small', 'small', 'medium', 'large',
         'x-large', 'xx-large']
styles  = ['normal', 'italic', 'oblique']
weights = ['light', 'normal', 'medium', 'semibold', 'bold', 'heavy', 'black']
variants = ['normal', 'small-caps']

fig = plt.figure(figsize=(9,17))
ax = fig.add_subplot(111)
ax.set_xlim(0,9)
ax.set_ylim(0,17)


# VAR: FAMILY, SIZE
y = 0
size = sizes[0]
style = styles[0]
weight = weights[0]
variant = variants[0]

for family in families:
    x = 0
    y = y + .5
    for size in sizes:
        y = y + .4
        sample = family + " " + size
        ax.text(x, y, sample,
                family=family,
                size=size,
                style=style,
                weight=weight,
                variant=variant)
        
# VAR: STYLE, WEIGHT
y = 0
family = families[0] 
size = sizes[4]
variant = variants[0]

for weight in weights:
    x = 5
    y = y + .5
    for style in styles:
        y = y + .4
        print x, y
        sample = weight + " " + style
        ax.text(x, y, sample,
                family=family,
                size=size,
                style=style,
                weight=weight,
                variant=variant)

ax.set_axis_off()
plt.show()