import reflex as rx
import reflexweb.pages.pagemain.styles as st
import reflexweb.pages.pagemain.colors as cl

st=st.styles_general()
cl=cl.colors()

def buttons_links(text1:str,text2:str,url:str,icono:str,goout:bool,hover:str,bg:str):
    return rx.link(
                rx.chakra.button(
                    rx.chakra.hstack(
                        rx.chakra.avatar(
                            src=icono,
                            style={
                                'width':st.size['big'],
                                'height':st.size['big'],
                                'margin':st.size['medium'],
                                'padding': '2px',
                                'bg':bg
                            },
                            _hover={
                                'border':'2px',
                                'border_color':cl.colorsg['withe']
                            }
                        ),
                        rx.chakra.vstack(
                            rx.text(
                                text1,
                                style=st.bt_tittle
                            ),
                            rx.text(
                                text2,
                                style=st.bt_body
                            ),
                            align_items="start"
                        )
                    ),
                    style=st.button,
                    _hover={
                        "background_color":hover,
                        'cursor':st.pointer
                        },
                ),
                href=url,
                is_external=goout,
                style=st.blink
            )

def links():
    return rx.vstack(
        st.headingstyles("Enlaces para visitar",'7','h2'),
        st.headingstyles('Redes de contacto','4','h3'),
        buttons_links(
            "LinkedIn",
            "Perfil de LinkedIn",
            "https://www.linkedin.com/in/daniel-santiago-gonzalez-ubaque-87a1b22b5",
            "/LinkedIn.png",
            True,
            '#055d91',
            '#ffffff'
                    ),
        buttons_links(
            "GitHub",
            "Perfil de GitHub",
            "https://github.com/DANIElPEZ/",
            "/Github.png",
            True,
            '#444444',
            '#ffffff'
                    ),
             buttons_links(
            "Instagram",
            "Perfil de instagram",
            "https://www.instagram.com/dani.g.dev?igsh=cnhlZTRqMnVwZzZp",
            "/Instagram.png",
            True,
            '#785937',
            '#ffffff'
                    ),
        buttons_links(
            "Facebook",
            "Perfil de facebook",
            "https://www.facebook.com/danielsantiagoangel.gonzalezubaque?mibextid=ZbWKwL",
            "/Facebook.png",
            True,
            '#033c5d',
            '#ffffff'
                    ),
        st.headingstyles('Mi ruta','4','h3'),
        buttons_links(
            "Recursos para estudiar",
            "Mis habilidades",
            '/myroute',
            "/route.png",
            False,
            '#667136',
            'rgba(120,120,120,0.8)'
                    ),
        st.headingstyles('Otros enlaces','4','h3'),
        buttons_links(
            "Herramientas",
            "Paginas externas",
            '/tools',
            "/Sql.png",
            False,
            '#122b61',
            'rgba(160,160,160,0.4)'
                    ),
        style=st.links_section,
        class_name='animate__animated animate__fadeInUp'
        )