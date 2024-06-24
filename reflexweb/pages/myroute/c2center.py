import reflex as rx
import reflexweb.pages.pagemain.styles as st
from reflexweb.pages.pagemain.c3links import buttons_links

st=st.styles_general()

def center():
    return rx.vstack(
        st.headingstyles("Mi ruta",'7','h2'),
        st.headingstyles("Python","4",'h3'),
        buttons_links(
            "Programacion basica",
            "La Geekipedia De Ernesto",
            "https://youtube.com/playlist?list=PLyvsggKtwbLW1j0d5yaCkRF9Axpdlhsxz&si=M5M5K-rdnnfGFoil",
            "/Python.png",
            True,
            "#0C2D57",
            'rgba(160,160,160,0.4)'
        ),
        buttons_links(
            "Programacion orientada a objetos",
            "Soy Dalto",
            "https://youtu.be/HtKqSJX7VoM?si=5PuNd_mnOlZ0ZCjb",
            "/Python.png",
            True,
            "#0C2D57",
            'rgba(160,160,160,0.4)'
        ),
        st.headingstyles("Aplicaciones de escritorio","4",'h3'),
        buttons_links(
            "Interfaz grafica tkinter",
            "Pildoras informaticas + ChatGPT",
            "https://youtube.com/playlist?list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&si=56SoTRuXUDsUfpjm",
            "/tk.png",
            True,
            "#365486",
            'rgba(160,160,160,0.4)'
        ),
        buttons_links(
            "Interfaz grafica PyQt6",
            "Jesús Conde + ChatGPT",
            "https://youtube.com/playlist?list=PLEtcGQaT56cj81xiNCrJnoAjc66uZVXDa&si=dIgEuI88krhC-vjN",
            "/qt.png",
            True,
            "#4d9b2b",
            'rgba(160,160,160,0.4)'
        ),
        st.headingstyles("Web frontend","4",'h3'),
        buttons_links(
            "Reflex framework",
            "MoureDev by Brais Moure",
            "https://youtu.be/n2YrGsXJC6Y?si=zGhxNlyym6vWWg-T",
            "/reflex.png",
            True,
            "#474F7A",
            'rgba(160,160,160,0.4)'
        ),
        st.headingstyles("Base de datos","4",'h3'),
        buttons_links(
            "SQL",
            "Soy Dalto",
            "https://youtu.be/DFg1V-rO6Pg?si=A1H-BkuislScjtQz",
            "/sqlite.png",
            True,
            "#3A98B9",
            'rgba(160,160,160,0.4)'
        ),
        st.headingstyles("Git and GitHub","4",'h3'),
        buttons_links(
            "Git and GitHub",
            "Soy Dalto",
            "https://youtu.be/9ZJ-K-zk_Go?si=hb30_w2Me-m7dJ_d",
            "/git.png",
            True,
            "#c8983d",
            '#ffffff'
        ),
        st.headingstyles("Enlace para aprender","4",'h3'),
        buttons_links(
            "W3schools",
            "Mas tecnologias",
            "https://www.w3schools.com/",
            "/w3s.png",
            True,
            "#186F65",
            'rgba(160,160,160,0.4)'
        ),
        style=st.links_section,
        class_name='animate__animated animate__fadeInUp'
    )