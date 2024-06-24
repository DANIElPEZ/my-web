import reflex as rx
import reflexweb.pages.pagemain.styles as st
import reflexweb.pages.pagemain.colors as cl

cl=cl.colors()

st=st.styles_general()

class open(rx.State):
    sidebar=False
    music=False

    def toglesidebar(self):
        self.sidebar=not self.sidebar

    def setmusic(self):
        self.music = not self.music

def navigation():
    return rx.box(
        rx.vstack(
            rx.flex(
                rx.hstack(
                    rx.chakra.icon(
                        tag="close",
                        on_click=open.toglesidebar,
                        margin=st.size['small'],
                        color='#ffffff',
                        _hover={
                            'cursor':st.pointer
                        }
                    )
                ),
                width='90%'
            ),
            rx.chakra.link(
                "Inicio",
                href='/',
                style=st.sidenav,
                on_click=open.toglesidebar
            ),
            rx.chakra.link(
                "Mi blog",
                href='/blog',
                style=st.sidenav,
                on_click=open.toglesidebar
            ),
            rx.chakra.link(
                "Mi ruta",
                href='/myroute',
                style=st.sidenav,
                on_click=open.toglesidebar
            ),
            rx.chakra.link(
                "Otros enlaces",
                href='/tools',
                style=st.sidenav,
                on_click=open.toglesidebar
            ),
            rx.chakra.link(
                "Deja tu comentario",
                href='/comments',
                style=st.sidenav,
                on_click=open.toglesidebar
            ),
            rx.chakra.link(
                "Piedra Papel o Tijera",
                href='/game',
                style=st.sidenav,
                on_click=open.toglesidebar
            ),
        ),
        width='100%'
    )

def showpages():
    return rx.chakra.drawer(
                rx.chakra.drawer_overlay(),
                rx.chakra.drawer_content(
                    navigation(),
                    style=st.sidebar,
                ),
                direction='right',
                is_open=open.sidebar
            )

rx.page(route='/')
def navbar():
    return rx.hstack(
                rx.flex(
                    rx.link(
                            rx.hstack(
                                rx.text('Dani',
                                    color=cl.colorsg['withe']
                                ),
                                rx.text('Dev',
                                    color=cl.colorsg['withe']
                                ),
                                _hover={
                                    'cursor':st.pointer
                                },
                            ),
                        class_name='animate__animated animate__fadeInLeft',
                        style=st.navbartext,
                        href='/'
                    ),
                    rx.spacer(),
                        rx.cond(
                            open.music,
                            rx.box(
                                rx.image(
                                    src='/soundon.png',
                                    height='27px',
                                    margin_right='15px',
                                    on_click=open.setmusic,
                                    _hover={
                                        'cursor':st.pointer
                                    }
                                ),
                                rx.video(
                                    url='https://youtu.be/-yyXIqUV8fg?si=t3Zj1e1MB59JV9FU',
                                    playing=open.music,
                                    loop=True,
                                    width='0px',
                                    height='0px'
                                )
                            ),
                            rx.image(
                                src='/soundoff.png',
                                height='27px',
                                margin_right='15px',
                                on_click=open.setmusic,
                                _hover={
                                    'cursor':st.pointer
                                }
                            )
                        ),
                        rx.chakra.icon(
                            tag="hamburger",
                            color=cl.colorsg['withe'],
                            width='30px',
                            height='30px',
                            class_name='animate__animated animate__fadeInRight',
                            on_click=open.toglesidebar,
                            _hover={
                                'cursor':st.pointer
                            }
                        ),
                    width='100%'
                ),
                showpages(),
                style=st.navbarstyles
            )