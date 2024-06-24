import reflex as rx
from reflexweb.pages.pagemain.c1navbar import navbar
from reflexweb.pages.pagemain.c4footer import footer
import reflexweb.pages.pagemain.styles as st

st=st.styles_general()

def creditcomponent(title:str,author:str,link:str):
    return rx.box(
                rx.hstack(
                    rx.text(
                        title,
                        color="#ffffff",
                        font_size='24px'
                    ),
                    rx.link(
                        rx.text(
                            author,
                            color="#aaaaaa",
                            font_size='22px',
                            _hover={
                            'cursor':st.pointer
                        }
                        ),
                        href=link,
                        is_external=True
                    ),
                    spacing="4"
                ),
                align_items='center',
                border_width='0 0 2px 0',
                border_color='#ffffff'
            )

@rx.page( route="/credits")
def credits():
    return rx.box(
        navbar(),
        rx.chakra.center(
            rx.chakra.vstack(
                rx.text('Fotos usadas de', color='#ffffff',font_size='24px'),
                creditcomponent("Mouse",'por "SVGBackgrounds.com"',"https://www.svgbackgrounds.com/"),
                creditcomponent("Facebook foto",'por "freepnglogos.com"','https://www.freepnglogos.com/'),
                creditcomponent("Instagram foto",'por "freepnglogos.com"','https://www.freepnglogos.com/'),
                creditcomponent("Google foto",'por "freepnglogos.com"','https://www.freepnglogos.com/'),
                creditcomponent("Linkedin foto",'por "freepnglogos.com"','https://www.freepnglogos.com/'),
                creditcomponent("W3schools foto",'por "wikipedia"','https://es.wikipedia.org/wiki/Wikipedia:Portada'),
                creditcomponent("Rene foto foto",'por "wikipedia"','https://es.wikipedia.org/wiki/Wikipedia:Portada'),
                creditcomponent("Github foto",'por "wikipedia"','https://es.wikipedia.org/wiki/Wikipedia:Portada'),
                creditcomponent("Python foto",'por "wikipedia"','https://es.wikipedia.org/wiki/Wikipedia:Portada'),
                creditcomponent("PostgreSQL foto",'por "wikipedia"','https://es.wikipedia.org/wiki/Wikipedia:Portada'),
                creditcomponent("Git foto",'por "Git"','https://git-scm.com/'),
                creditcomponent("Reflex foto",'por "Reflex"','https://reflex.dev/'),
                creditcomponent("Sqlite foto",'por "Reflex"','https://reflex.dev/'),
                creditcomponent("Reflex foto",'por "Wikimedia Commons"','https://commons.wikimedia.org/wiki/Main_Page'),
                creditcomponent("Qt foto",'por "wikipedia"','https://es.wikipedia.org/wiki/Wikipedia:Portada'),
                creditcomponent("Tcl foto",'por "Wikimedia Commons"','https://commons.wikimedia.org/wiki/Main_Page'),
                creditcomponent("ChatGpt foto",'por "Wikimedia Commons"','https://commons.wikimedia.org/wiki/Main_Page'),
                creditcomponent("MongoDB foto",'por "iconduck.com"',"https://iconduck.com/"),
                creditcomponent("Visual Studio Code",'por "visualstudio.com"',"https://code.visualstudio.com/"),
                creditcomponent("MySql foto",'por "icon-icons.com"',"https://icon-icons.com/"),
                creditcomponent("Sql foto",'por "freeiconspng.com"','https://www.freeiconspng.com/'),
                creditcomponent("Tabla foto",'por "flaticon.es"','https://www.flaticon.es/'),
                creditcomponent("Code foto",'por "flaticon.es"','https://www.flaticon.es/'),
                creditcomponent("Route foto",'por "flaticon.es"','https://www.flaticon.es/'),
                creditcomponent("Tijera foto",'por "flaticon.es"','https://www.flaticon.es/'),
                creditcomponent("Sound on foto",'por "googlefonts"','https://fonts.google.com/'),
                creditcomponent("Sound on foto",'por "googlefonts"','https://fonts.google.com/'),
                creditcomponent("Piedra foto",'por "pixabay.com"','https://pixabay.com/'),
                creditcomponent("Papel foto",'por "123rf.com"','https://es.123rf.com/'),
                creditcomponent("incognito foto",'por "freeiconspng.com"','https://www.freeiconspng.com/'),
                max_width=st.max_width,
                width="100%",
                margin_y=st.size['extra_big'],
                padding=st.size['big']
            )
        )
    )