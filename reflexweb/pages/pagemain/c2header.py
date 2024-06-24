import reflex as rx
import reflexweb.pages.pagemain.styles as st
import datetime as dt
import reflexweb.pages.pagemain.colors as cl
import reflexweb.pages.pagemain.fonts as ft

cl=cl.colors()
st=st.styles_general()
ft=ft.font()

def headerpt1():
    return rx.hstack(
                    rx.chakra.avatar(
                        size="xl",
                        src='/DNV.png',
                        bg=cl.colorsg['content'],
                        border='4px',
                        border_color=cl.colorsg['navbar']
                    ),
                    rx.vstack(
                        rx.heading(
                            'DANI',
                             as_='h1',
                             size='7',
                             color='#ffffff',
                             font_family='open sans'
                        ),
                        rx.heading(
                            "@Danidev",
                            size='3',
                            as_='h3',
                            padding_top='0px !important',
                            color='#ffffff'
                        ),
                        width='100%',
                        align_items='start'
                    ),
                    spacing='4',
                    class_name='animate__animated animate__flipInX'
            )

def headerpt2():
    return rx.flex(
                    st.idev(
                        f'+{dt.date.today().year-2023} ',
                        'Años en crear aplicaciones'
                    ),
                    rx.spacer(),
                    st.idev(
                        '+6 ',
                        'proyectos realizados'
                    ),
                    width='100%',
                    class_name='animate__animated animate__zoomIn'
                )

def headerpt3():
    return rx.text(
                'Bienvenid@s mi nombre es DANIEL SANTIAGO ANGEL GONZALEZ UBAQUE y soy estudiante de la carrera ',
                rx.chakra.icon(tag="arrow_forward"),
                ' Ingeniería informatica. Ser un excelente programador en el lenguaje de programación Python3.',
                 color='#ffffff',
                 font_size='15px',
                 text_align='justify',
                 class_name='animate__animated animate__zoomIn'
            )

def headerpt4():
    return rx.vstack(
        rx.heading(
            'Mis proyectos para',
            size='3',
            as_='h2',
            padding_top='0px !important',
            color="#e7ecf1",
            class_name='animate__animated animate__zoomIn'
        ),
        rx.hstack(
            rx.link(
                rx.chakra.button("Escritorio",
                    bg='#0a837b',
                    _hover={
                        'bg':'#0a837b',
                        'cursor':st.pointer
                    },
                    class_name='css-button-arrow--green'
                ),
                href='/services/desktop'
            ),
            class_name='animate__animated animate__rollIn'
        )
    )

def header():
    return rx.vstack(
                headerpt1(),
                headerpt2(),
                headerpt3(),
                headerpt4(),
                style=st.header
        )