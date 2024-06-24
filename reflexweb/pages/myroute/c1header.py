import reflex as rx
import reflexweb.pages.toolpage.styles as st
import reflexweb.pages.pagemain.styles as stp

st=st.styles_mtpg()
stpg=stp.styles_general()

def header():
    return rx.vstack(
                rx.box(
                        rx.center(
                            rx.chakra.avatar(
                                src='/route.png',
                                size='xl',
                                padding='2px',
                                border='4px',
                                border_color='#ffffff',
                                class_name='animate__animated animate__flipInX'
                            )
                        ),
                        rx.heading(
                            "Mi ruta",
                            as_='h2',
                            style=st.styleshd,
                            class_name='animate__animated animate__jello'
                        ),
                        rx.text(
                            'En esta página veras la ruta que he tomado con python, otras tecnologías y otros enlaces para aprender.',
                            style=st.texthd,
                            class_name='animate__animated animate__jello'
                        ),

                ),
                max_width='100%',
                padding_top=stpg.size['extra_big']
            )