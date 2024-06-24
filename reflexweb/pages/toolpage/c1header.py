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
                                src='/Sql.png',
                                size='xl',
                                padding='2px',
                                border='4px',
                                border_color='#ffffff',
                                class_name='animate__animated animate__flipInX'
                            )
                        ),
                        rx.heading(
                            "Herramientas",
                            as_='h2',
                            style=st.styleshd,
                            class_name='animate__animated animate__jello'
                        ),
                        rx.text(
                            'Acá encontraras link externos y herramientas para acelerar tu trabajo.',
                            style=st.texthd,
                            class_name='animate__animated animate__jello'
                        ),

                ),
                max_width='100%',
                padding_top=stpg.size['extra_big']
            )