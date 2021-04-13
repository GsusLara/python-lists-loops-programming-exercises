all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:
def generate_li(color):
    return("<li>"+str(color["label"])+"</li>")
def filter_colors(x):
    return x["sexy"]==True
listaFiltrada=list(filter(filter_colors,all_colors))
listaEstructurada=list(map(generate_li, listaFiltrada))
salida=""
for i in listaEstructurada:
    salida+=i 
print(salida)