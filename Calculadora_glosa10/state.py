import reflex as rx
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

#Funciones para calcular valores de terreno

def calculo_terreno(n_familias,valor_terreno,ahorro_inicial,subsidio_base,porc,limite,adicion):
    valor_terreno_familia=valor_terreno/n_familias
    ahorro_mas_subsidio=ahorro_inicial+subsidio_base
    saldo_terreno=valor_terreno_familia-ahorro_mas_subsidio
    if (saldo_terreno*porc) > limite:
        subsidio_adicional=limite
    else:
        subsidio_adicional=saldo_terreno*porc
    ahorro_adicional=saldo_terreno-subsidio_adicional
    ahorro_total=ahorro_adicional+adicion
    subsidio_terreno_total=subsidio_base+subsidio_adicional
    return(valor_terreno_familia,ahorro_inicial,subsidio_base,ahorro_mas_subsidio,saldo_terreno,porc,subsidio_adicional,ahorro_adicional,ahorro_total,subsidio_terreno_total)

def a1_menos40p(n_familias,valor_terreno):
    valor_terreno_familia=valor_terreno/n_familias
    ahorro_inicial=10
    subsidio_base=250
    porc=0.8
    limite=350
    adicion=10
    valor_terreno_familia,ahorro_inicial,subsidio_base,ahorro_mas_subsidio,saldo_terreno,porc,subsidio_adicional,ahorro_adicional,ahorro_total,subsidio_terreno_total=calculo_terreno(n_familias,valor_terreno,ahorro_inicial,subsidio_base,porc,limite,adicion)
    return(valor_terreno_familia,ahorro_inicial,subsidio_base,ahorro_mas_subsidio,saldo_terreno,porc,subsidio_adicional,ahorro_adicional,ahorro_total,subsidio_terreno_total)

def a1_mas40p(n_familias,valor_terreno):
    valor_terreno_familia=valor_terreno/n_familias
    ahorro_inicial=15
    subsidio_base=245
    porc=0.75
    limite=350
    adicion=15
    valor_terreno_familia,ahorro_inicial,subsidio_base,ahorro_mas_subsidio,saldo_terreno,porc,subsidio_adicional,ahorro_adicional,ahorro_total,subsidio_terreno_total=calculo_terreno(n_familias,valor_terreno,ahorro_inicial,subsidio_base,porc,limite,adicion)
    return(valor_terreno_familia,ahorro_inicial,subsidio_base,ahorro_mas_subsidio,saldo_terreno,porc,subsidio_adicional,ahorro_adicional,ahorro_total,subsidio_terreno_total)

def a2_menos40p(n_familias,valor_terreno):
    valor_terreno_familia=valor_terreno/n_familias
    ahorro_inicial=10
    subsidio_base=200
    porc=0.75
    limite=250
    adicion=10
    valor_terreno_familia,ahorro_inicial,subsidio_base,ahorro_mas_subsidio,saldo_terreno,porc,subsidio_adicional,ahorro_adicional,ahorro_total,subsidio_terreno_total=calculo_terreno(n_familias,valor_terreno,ahorro_inicial,subsidio_base,porc,limite,adicion)
    return(valor_terreno_familia,ahorro_inicial,subsidio_base,ahorro_mas_subsidio,saldo_terreno,porc,subsidio_adicional,ahorro_adicional,ahorro_total,subsidio_terreno_total)

def a2_mas40p(n_familias,valor_terreno):
    valor_terreno_familia=valor_terreno/n_familias
    ahorro_inicial=15
    subsidio_base=195
    porc=0.70
    limite=250
    adicion=15
    valor_terreno_familia,ahorro_inicial,subsidio_base,ahorro_mas_subsidio,saldo_terreno,porc,subsidio_adicional,ahorro_adicional,ahorro_total,subsidio_terreno_total=calculo_terreno(n_familias,valor_terreno,ahorro_inicial,subsidio_base,porc,limite,adicion)
    return(valor_terreno_familia,ahorro_inicial,subsidio_base,ahorro_mas_subsidio,saldo_terreno,porc,subsidio_adicional,ahorro_adicional,ahorro_total,subsidio_terreno_total)

def analisis_critico(n_familias,valor_terreno):
    data=pd.DataFrame(columns=["N° Familias","Valor del Terreno (UF) (Sin puntos)"])
    data.loc[len(data)] = [n_familias,valor_terreno]

    for index,row in data.iterrows():
        resultados=[]
        resultados_2=[]
        rango_familias=20
        intervalo_familias=3
        rango_monto=2000
        intervalo_monto=1000
        n_familias=int(row["N° Familias"])
        valor_terreno=int(row["Valor del Terreno (UF) (Sin puntos)"])
        #valor_terreno_familia_menos40p,ahorro_inicial_menos40p,subsidio_base_menos40p,ahorro_mas_subsidio_menos40p,saldo_terreno_menos40p,porc_menos40p,subsidio_adicional_menos40p,ahorro_adicional_menos40p,ahorro_total_menos40p,subsidio_terreno_total_menos40p=a1_menos40p(n_familias,valor_terreno)
        #valor_terreno_familia_mas40p,ahorro_inicial_mas40p,subsidio_base_mas40p,ahorro_mas_subsidio_mas40p,saldo_terreno_mas40p,porc_mas40p,subsidio_adicional_mas40p,ahorro_adicional_mas40p,ahorro_total_mas40p,subsidio_terreno_total_mas40p=a1_mas40p(n_familias,valor_terreno)
        for i in range(n_familias-rango_familias,n_familias+rango_familias,intervalo_familias):
            if i > 0:
                for j in range(valor_terreno-rango_monto,valor_terreno+rango_monto,intervalo_monto):
                    if j >0:
                        n_familias_i=i
                        valor_terreno_j=j
                        valor_terreno_familia_menos40p,ahorro_inicial_menos40p,subsidio_base_menos40p,ahorro_mas_subsidio_menos40p,saldo_terreno_menos40p,porc_menos40p,subsidio_adicional_menos40p,ahorro_adicional_menos40p,ahorro_total_menos40p,subsidio_terreno_total_menos40p=a1_menos40p(n_familias_i,valor_terreno_j)
                        valor_terreno_familia_mas40p,ahorro_inicial_mas40p,subsidio_base_mas40p,ahorro_mas_subsidio_mas40p,saldo_terreno_mas40p,porc_mas40p,subsidio_adicional_mas40p,ahorro_adicional_mas40p,ahorro_total_mas40p,subsidio_terreno_total_mas40p=a1_mas40p(n_familias_i,valor_terreno_j)
                        aux=[n_familias_i,valor_terreno_j,ahorro_total_menos40p,ahorro_total_mas40p]
                        resultados.append(aux)
                    else:
                        pass
            else:
                pass
        return(resultados)
    

class FormState(rx.State):
    form_data: dict = {}
    results: dict = {}
    results_mas40 = []
    results_menos40 = []
    resultado_variable=[]

    
    def handle_submit(self, form_data: dict):
        self.form_data = form_data

         #Saco los valores del calculo de terrenos
        n_familias=int(form_data["num_familias"])
        valor_terreno=int(form_data["valor_terreno"])
        area_terreno=form_data["area_terreno"]
        if area_terreno=="Area 1":
            valor_terreno_familia_menos40p,ahorro_inicial_menos40p,subsidio_base_menos40p,ahorro_mas_subsidio_menos40p,saldo_terreno_menos40p,porc_menos40p,subsidio_adicional_menos40p,ahorro_adicional_menos40p,ahorro_total_menos40p,subsidio_terreno_total_menos40p=a1_menos40p(n_familias,valor_terreno)
            valor_terreno_familia_mas40p,ahorro_inicial_mas40p,subsidio_base_mas40p,ahorro_mas_subsidio_mas40p,saldo_terreno_mas40p,porc_mas40p,subsidio_adicional_mas40p,ahorro_adicional_mas40p,ahorro_total_mas40p,subsidio_terreno_total_mas40p=a1_mas40p(n_familias,valor_terreno)
        else:
            valor_terreno_familia_menos40p,ahorro_inicial_menos40p,subsidio_base_menos40p,ahorro_mas_subsidio_menos40p,saldo_terreno_menos40p,porc_menos40p,subsidio_adicional_menos40p,ahorro_adicional_menos40p,ahorro_total_menos40p,subsidio_terreno_total_menos40p=a2_menos40p(n_familias,valor_terreno)
            valor_terreno_familia_mas40p,ahorro_inicial_mas40p,subsidio_base_mas40p,ahorro_mas_subsidio_mas40p,saldo_terreno_mas40p,porc_mas40p,subsidio_adicional_mas40p,ahorro_adicional_mas40p,ahorro_total_mas40p,subsidio_terreno_total_mas40p=a2_mas40p(n_familias,valor_terreno)

        resultados={"menos 40":[valor_terreno_familia_menos40p,ahorro_inicial_menos40p,subsidio_base_menos40p,ahorro_mas_subsidio_menos40p,saldo_terreno_menos40p,porc_menos40p,subsidio_adicional_menos40p,ahorro_adicional_menos40p,ahorro_total_menos40p,subsidio_terreno_total_menos40p],
                    "mas 40": [valor_terreno_familia_mas40p,ahorro_inicial_mas40p,subsidio_base_mas40p,ahorro_mas_subsidio_mas40p,saldo_terreno_mas40p,porc_mas40p,subsidio_adicional_mas40p,ahorro_adicional_mas40p,ahorro_total_mas40p,subsidio_terreno_total_mas40p]}
        self.results=resultados
        self.results_mas40=resultados["mas 40"]
        self.results_menos40=resultados["menos 40"]

        #Realizo el analisis de variable
        self.resultado_variable=analisis_critico(n_familias,valor_terreno)

    
    @rx.var
    def scat_fig(self)-> go.Figure:
        #### 2D plot
        familias_plot=[self.resultado_variable[i][0] for i in range(len(self.resultado_variable))]
        terreno_plot=[self.resultado_variable[i][1] for i in range(len(self.resultado_variable))]
        terreno_plot_categorico=[str(self.resultado_variable[i][1]) for i in range(len(self.resultado_variable))]
        ahorro_plot=[self.resultado_variable[i][2] for i in range(len(self.resultado_variable))]
        df_3d = pd.DataFrame()
        df_3d['N° familias'] = familias_plot
        df_3d['Valor Terreno'] = terreno_plot
        df_3d['Valor Terreno Categorico'] = terreno_plot_categorico
        df_3d['Ahorro (UF)'] = ahorro_plot
        df2 = px.data.gapminder().query("country=='Canada'")
        return px.scatter(
                df_3d,
                x='N° familias',
                y='Ahorro (UF)',
                symbol='Valor Terreno',
                color='Valor Terreno Categorico',
                title = "Num Familias (Eje X) VS Ahorro UF (Eje Y)"
            )
        
    


