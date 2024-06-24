import reflex as rx
from reflexweb.pages.pagemain.c1navbar import navbar
from reflexweb.pages.pagemain.c4footer import footer
import reflexweb.rxpage as rdx
import reflexweb.pages.pagemain.styles as st
import datetime as dt

rdx=rdx.rxpg()
st=st.styles_general()

def iam():
    return rx.box(
        rx.flex(
            rx.avatar(
                    src='/DNV.png',size='7',
                    margin_right='10px',
                    class_name="animate__animated animate__fadeInTopLeft"
            ),
            rx.chakra.text(
                '''
                Hola yo soy Daniel Santiago Angel Gonzalez Ubaque, 
                aquí comparto unos conocimientos, 
                donde te van ayudar a solucionar problemas, 
                ser más productivo como programador y parte de mi vida cotidiana.
                ''',
                text_align='justify',
                color='#ffffff',
                class_name="animate__animated animate__fadeInTopRight"
            )
        ),
        padding_top=st.size['big']
    )

def mytoolsdk():
    return rx.box(
        rx.box(
            rx.heading('Mis Herramientas',
                    size='6',
                    color='#b9ccf2',
                    padding_top='25px',
                    as_='h2'
                    ),
            rx.heading('IDE',
                    size='4',
                    color='#29e1c9',
                    padding_top='18px',
                    as_='h3'
                    ),
            class_name='animate__animated animate__slideInLeft'
        ),
        rx.image(
                    src='/blgvsc.jpg',
                    padding_y='10px',
                    width=st.max_width,
                    class_name='animate__animated animate__flipInY'
                    ),
        
            rx.text(
                '''
                Visual Studio Code, 
                es un editor de código, el cual te ayuda a escribir código más rápido, 
                dentro del editor puedes instalar varias extensiones, 
                de las cuales uso las siguientes:''',
                color='#ffffff',
                text_align='justify',
                class_name='animate__animated animate__fadeInUp'
            ),
            rx.list.unordered(
                    rx.list.item('Error Lens.'),
                    rx.list.item('indent-rainbow.'),
                    rx.list.item('indenticator.'),
                    rx.list.item('Jupyter.'),
                    rx.list.item('Material Icon Theme.'),
                    rx.list.item('One Dark Pro.'), 
                    rx.list.item('Palenight Theme.'),
                    rx.list.item('Prettier - Code formatter.'),
                    rx.list.item('Pylance.'),
                    rx.list.item('Python.'),
                    rx.list.item('Python Debugger.'),
                    rx.list.item('Rainbow CSV.'),
                    rx.list.item('Subtle Match Brackets.'),
                    rx.list.item('Thunder Client. '),
                    rx.list.item('Live Preview.'),
                    color='#ffffff',
                    class_name='animate__animated animate__fadeInUp'
                ),
        rx.heading('Herramientas',
                   size='4',
                   color='#29e1c9',
                   padding_top='18px',
                   as_='h3'
                   ),
        rx.image(
                src='/pwtoys.jpg',
                padding_y='10px',
                width=st.max_width
                 ),
        rx.text(
                '''
                Power Toys es una herramienta, donde tiene varias aplicaciones, 
                el uso más común que yo hago es obtener el RGB O HEX del color de forma rápida, 
                esta herramienta incluye:''',
                rx.list.unordered(
                    rx.list.item('Always On Top.'),
                    rx.list.item('PowerToys Awake.'),
                    rx.list.item('Selector de colores.'),
                    rx.list.item('No se encontró el comando.'),
                    rx.list.item('Recortar y bloquear.'),
                    rx.list.item('Variables de entorno.'),
                    rx.list.item('FancyZones.'),
                    rx.list.item('Complementos de File Explorer.'),
                    rx.list.item('File Locksmith.'),
                    rx.list.item('Editor del archivo "Hosts".'),
                    rx.list.item('Cambio de tamaño de imágenes.'),
                    rx.list.item('Administrador de teclado.'),
                    rx.list.item('Administrador de teclado.'),
                    rx.list.item('Utilidades del mouse.'),
                    rx.list.item('Mouse sin límites.'),
                    rx.list.item('Pegar como texto sin formato.'),
                    rx.list.item('Ojear.'),
                    rx.list.item('PowerRename.'),
                    rx.list.item('PowerToys Run.'),
                    rx.list.item('Acento rápido.'),
                    rx.list.item('Vista previa del Registro.'),
                    rx.list.item('Regla en pantalla.'),
                    rx.list.item('Guía de métodos abreviados de teclado.'),
                    rx.list.item('Extractor de texto, '),
                    rx.list.item('Silencio de videoconferencia.'),
                ),
                color='#ffffff',
                text_align='justify'
                ),
        
    )


def hobbies():
    return rx.box(
        rx.heading(
            'Mis hobbies',
            size='6',
            color='#a0e69c',
            as_='h3'
            ),
        rx.heading(
            'La aviación',
            sixe='4',
            color='#9ce6df',
            padding_y='18px',
            as_='h3'
            ),
        rx.text('''
                La aviación sigue siendo uno de mis hobbies principales,
                para ello uso 3 simuladores dependiendo del avión que quiera volar, 
                aeropuertos, entre otras cosas específicas de cada simulador:''',
                rx.list.unordered(
                    rx.list.item('X-PLANE 11.'),
                    rx.list.item('MICROSOFT FLIGHT SIMULATOR X STEAM EDITION.')
                ),
                color='#ffffff',
                text_align='justify'
                ),
        rx.desktop_only(
            rx.hstack(
                rx.image(
                    src='/xplane-11.jpg',
                    height='120px'
                ),
                rx.image(
                    src='/fsx.jpg',
                    height='120px'
                ),
                margin_y='10px',
            )
        ),
        rx.mobile_and_tablet(
            rx.center(
                rx.vstack(
                    rx.image(
                        src='/xplane-11.jpg',
                        width='500px'
                    ),
                    rx.image(
                        src='/fsx.jpg',
                        width='500px'
                    ),
                    margin_y='10px',
                )
            )
        ),
        st.idev(f'+{dt.date.today().year-2019}',' Años en simulación de vuelo.',
                ),
        rx.heading(
            'Aviones preferidos',
            sixe='4',
            color='#9ce6df',
            padding_y='18px',
            as_='h3'
            ),
            rx.box(
                rx.heading(
                        'Lockheed Constellation L049',
                        size='3',
                        color='#d4ac6c',
                        padding_y='10px',
                        as_='h3'
                ),
                rx.desktop_only(
                    rx.hstack(
                        rx.image(src='/ckconstellation.jpg',height='127px'),
                        rx.image(src='/outconstellation.jpg',height='127px')
                    ),
                ),
                rx.mobile_and_tablet(
                    rx.image(src='/ckconstellation.jpg'),
                    rx.image(src='/outconstellation.jpg'),
                ),
                rx.heading(
                        'Concorde',
                        size='3',
                        color='#d4ac6c',
                        padding_y='10px',
                        as_='h3'
                ),
                rx.desktop_only(
                    rx.hstack(
                        rx.image(src='/ckconcorde.webp',height='134px'),
                        rx.image(src='/outconcorde.webp',height='134px')
                    )
                ),
                rx.mobile_and_tablet(
                    rx.image(src='/ckconcorde.webp'),
                    rx.image(src='/outconcorde.webp')
                )
            ),
        rx.heading(
            'El ilusionismo',
            sixe='4',
            color='#9ce6df',
            padding_y='18px',
            as_='h3'
        ),
        rx.heading(
            'Cartomagia Lentidigitación',
            color='#cbcbcb',
            as_='h3'
            ),
        rx.text('''
                El ilusionismo es mi segundo hobbie, 
                donde yo me represento con esta área del ilusionismo que es la lentidigitación, 
                el autor y creador de esta área fue el mago argentino de una sola mano Hector Rene Lavandera, 
                de los juegos que el hizo y yo también hago son:''',
                rx.list.unordered(
                    rx.list.item("No se puede hacer más lento."),
                    rx.list.item("El soneto."),
                    rx.list.item("La carta ambiciosa."),
                    rx.list.item("Mi juego credencial."),
                    rx.list.item("As, dos, tres, cuatro."),
                    rx.list.item("Adivinando.")
                ),
                color='#ffffff',
                padding_y='10px',
                text_align='justify'
            ),
        rx.center(
            rx.vstack(
                rx.image(
                    src='/rene.jpg',
                    width='350px'
                ),
                rx.video(
                    url='https://youtu.be/ZEwyIDL0YfM?si=hj77iYhR5rmGRnaG',
                    width='100%',
                    hover={
                        'cursor':st.pointer
                    }
                )
            ),
        ),
        margin_y=st.size['big']
    )

@rx.page(
    route='/blog',
    title=rdx.title,
    description=rdx.description,
    image=rdx.img,
    meta=rdx.meta
    )
def blog():
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                iam(),
                mytoolsdk(),
                hobbies(),
                max_width=st.max_width,
                width="100%",
                margin_y=st.size['big'],
                padding=st.size['big']
            )
        ),
        footer()
    )