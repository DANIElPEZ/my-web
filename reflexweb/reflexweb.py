import reflex as rx
from reflexweb.pages.pagemain.c1navbar import navbar
from reflexweb.pages.pagemain.c2header import header
from reflexweb.pages.pagemain.c3links import links
from reflexweb.pages.pagemain.c4footer import footer
import reflexweb.pages.pagemain.styles as st
import reflexweb.pages.pagemain.fonts as ft
#pages
from reflexweb.pages.toolpage.toolpg import toolpg
from reflexweb.pages.myroute.myroute import myroute
from reflexweb.pages.juegoweb.jugar import juego
from reflexweb.pages.comentarios.commentpg import comentpg
from reflexweb.pages.sevices.service import service_examples
from reflexweb.pages.blog.blog import blog
from reflexweb.pages.credits.credits import credits
import reflexweb.rxpage as rxd
#coroutines api
from reflexweb.pages.backend.backend import buscar, insertar

st=st.styles_general()
ft=ft.font()
rxd=rxd.rxpg()

@rx.page(
        route='/',
        title=rxd.title,
        image=rxd.img,
        description=rxd.description,
        meta=rxd.meta
        )
def index():
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=st.max_width,
                width="100%",
                margin_y=st.size['big'],
                padding=st.size['big']
            )
        ),
        footer()
    )

app = rx.App(
    style=st.stpage,
    stylesheets=[
        "/styles.css",
        "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"
    ]
)
app.add_page(index)
app.api.add_api_route("/find/",buscar)
app.api.add_api_route("/search/",insertar)