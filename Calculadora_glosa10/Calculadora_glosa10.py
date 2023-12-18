
import reflex as rx
from Calculadora_glosa10 import style
from Calculadora_glosa10 import Navbar as nv
from Calculadora_glosa10 import state as st
import plotly.express as px

def formulario():
    return rx.vstack(
        rx.text("Ingrese los datos del proyecto.", font_size="2em"),
        rx.form(
        rx.hstack(
            #Primera Columna
            rx.vstack(   
                rx.input(
                    placeholder="Entidad Solicitante",
                    id="nombre_ep",
                ),
                rx.input(
                    placeholder="Nombre del Proyecto",
                    id="nombre_proyecto",
                ),
                rx.input(
                    placeholder="Código del Proyecto",
                    id="codigo_proyecto",
                ),
            ),
            #Segunda Columna
            rx.vstack(
                rx.input(
                    placeholder="Número de Familias",
                    id="num_familias",
                ),
                rx.select(
                    ["Area 1", "Area 2"],
                    placeholder="Seleccione un Área",
                    id="area_terreno",
                ),
                rx.input(
                    placeholder="Valor del Terreno (UF) (Sin puntos)",
                    id="valor_terreno",
                ),
                
            ),
            spacing="2em",  
        ),
        #Boton de envio
        rx.vstack(
            rx.button("Calcular!", type_="submit"),
            padding_top="1em",
        ),
        on_submit=st.FormState.handle_submit,
        ),
        
        width="100%",
    )

def resultados():
        return rx.vstack(
        rx.heading("Resultados"),
        rx.hstack(
             #Primera Columna
             rx.vstack(
                rx.heading("Familias con mas de 40% RSH", size="lg"),
                rx.hstack(
                    rx.text("Valor Terreno por Familia:"),
                    rx.text(st.FormState.results_mas40[0]),
                ),
                 rx.hstack(
                    rx.text("Ahorro Inicial:"),
                    rx.text(st.FormState.results_mas40[1]),
                ),
                rx.hstack(
                    rx.text("Subsidio Base:"),
                    rx.text(st.FormState.results_mas40[2]),
                ),
                rx.hstack(
                    rx.text("Ahorro mas Subsidio:"),
                    rx.text(st.FormState.results_mas40[3]),
                ),
                rx.hstack(
                    rx.text("Saldo del Terreno:"),
                    rx.text(st.FormState.results_mas40[4]),
                ),
                rx.hstack(
                    rx.text("%:"),
                    rx.text(st.FormState.results_mas40[5]),
                ),
                rx.hstack(
                    rx.text("Subsidio Adicional:"),
                    rx.text(st.FormState.results_mas40[6]),
                ),
                rx.hstack(
                    rx.text("Ahorro Adicional:"),
                    rx.text(st.FormState.results_mas40[7]),
                ),
                rx.hstack(
                    rx.text("Ahorro Total:"),
                    rx.text(st.FormState.results_mas40[8]),
                ),
                rx.hstack(
                    rx.text("Subsidio Terreno Total:"),
                    rx.text(st.FormState.results_mas40[9]),
                ), 
             ),
             #Segunda Columna
             rx.vstack(
                rx.heading("Familias con menos de 40% RSH", size="lg"),
                rx.hstack(
                    rx.text("Valor Terreno por Familia:"),
                    rx.text(st.FormState.results_menos40[0]),
                ),
                rx.hstack(
                    rx.text("Ahorro Inicial:"),
                    rx.text(st.FormState.results_menos40[1]),
                ),
                rx.hstack(
                    rx.text("Subsidio Base:"),
                    rx.text(st.FormState.results_menos40[2]),
                ),
                rx.hstack(
                    rx.text("Ahorro mas Subsidio:"),
                    rx.text(st.FormState.results_menos40[3]),
                ),
                rx.hstack(
                    rx.text("Saldo del Terreno:"),
                    rx.text(st.FormState.results_menos40[4]),
                ),
                rx.hstack(
                    rx.text("%:"),
                    rx.text(st.FormState.results_menos40[5]),
                ),
                rx.hstack(
                    rx.text("Subsidio Adicional:"),
                    rx.text(st.FormState.results_menos40[6]),
                ),
                rx.hstack(
                    rx.text("Ahorro Adicional:"),
                    rx.text(st.FormState.results_menos40[7]),
                ),
                rx.hstack(
                    rx.text("Ahorro Total:"),
                    rx.text(st.FormState.results_menos40[8]),
                ),
                rx.hstack(
                    rx.text("Subsidio Terreno Total:"),
                    rx.text(st.FormState.results_menos40[9]),
                ),

             ),
             spacing="5em",
             padding_top="1em",
        )
        )

def analisis_critico():
     return rx.vstack(
                rx.heading("Analisis de Sensibilidad de Variables"),
                rx.heading("Num Familias (Eje X) VS Ahorro UF (Eje Y)",size="md"),
                rx.heading("Cada categoría es un valor de terreno diferente",size="sm"),
                rx.plotly(data=st.FormState.scat_fig, layout={"width": "1000", "height": "600"})
     )

def index():
    return rx.center(
        rx.vstack(
            nv.navbar(),
            formulario(),
            rx.divider(),
            resultados(),
            rx.divider(),
            analisis_critico(), 
            padding_top="7em",
            width="100%",
    ))



# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()