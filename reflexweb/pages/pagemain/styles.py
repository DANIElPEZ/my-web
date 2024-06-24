import reflex as rx
import reflexweb.pages.pagemain.colors as cl
import reflexweb.pages.pagemain.fonts as ft

cl=cl.colors()
ft=ft.font()

class styles_general():
    'CONSTANTS'
    max_width="560px"

    'SIZE VALUES'
    size={
        "zero":"0px important!",
        "small":"0.5em",
        "medium":"0.8em",
        "normal":"1em",
        "medium_big":"1.5em",
        "big":"2em",
        "extra_big":"3.5em"
    }

    pointer="""url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="%23000000" stroke="%23FFFFFF" stroke-width="1.25" stroke-linejoin="round" d="M10 11V8.99c0-.88.59-1.64 1.44-1.86h.05A1.99 1.99 0 0 1 14 9.05V12v-2c0-.88.6-1.65 1.46-1.87h.05A1.98 1.98 0 0 1 18 10.06V13v-1.94a2 2 0 0 1 1.51-1.94h0A2 2 0 0 1 22 11.06V14c0 .6-.08 1.27-.21 1.97a7.96 7.96 0 0 1-7.55 6.48 54.98 54.98 0 0 1-4.48 0 7.96 7.96 0 0 1-7.55-6.48C2.08 15.27 2 14.59 2 14v-1.49c0-1.11.9-2.01 2.01-2.01h0a2 2 0 0 1 2.01 2.03l-.01.97v-10c0-1.1.9-2 2-2h0a2 2 0 0 1 2 2V11Z"></path></svg>'), auto;"""

    stpage={
        'background_color': '#0c151d',
        'font_family':ft.ft_page['1']
    }

    '''
    NAVIGATION BAR STYLES
    
    -navigation bar general
    -navigation bar text
    -sidebar
    -sidebar button
    .sidebar buttons links
    '''
    navbarstyles={
        'position':'fixed',
        'background_color':'#1b2b43',
        'padding_x':size["big"],
        'padding_y':size["normal"],
        'z_index':'10',
        'top':size['zero'],
        'width':'100%',
    }
    navbartext={
        'font_family':ft.ft_page['1'],
        'font_size':size['medium_big'],
        'width':'110px',
        "text_decoration":"none",
        '_hover':{}
    }

    sidebar={
        'background_color':'#0f1928',
        'transition':'0.3s',
    }
    sidenav={
        'text_align':'center',
        'color':'#ffffff',
        'font_size':'1.1em',
        "text_decoration":"none",
        'font_family':ft.ft_page['2'],
        'width':'100%',
        'cursor':'pointer',
        'transition':'0.2s',
        '_hover':{
            'cursor':pointer,
            'bg':'#105a86',
            'border_width':'0 0 0 2px',
            'border_color':'#ffffff',
        }
    }

    '''
    HEADER

    -header values
    -header part2 values
    '''
    header={
        'align_items':'start',
        'spacing':size['big'],
        'padding_top':size['extra_big'],
    }
    def idev(self,tittle,body):
        return rx.box(
            rx.chakra.span(
                tittle,
                font_weight='bold',
                color=cl.colorsg['primary']
            ),
            body,
            font_size='17px',
            color='#ffffff'
        )

    '''
    BUTTON STYLES

    -buttons sections
    -button icon link
    -button tittle values
    -button body values
    -button general values
    -button style link values
    -buttons list and heading
    '''
    headstyles={
        'width':'100%',
        'padding_top':size['normal'],
        'color':cl.colors_text['header'],
        'font_family':ft.ft_page['1']
    }
    def headingstyles(self,text:str,sizel:str,_as_:str):
        self.headstyles['size']=sizel
        return rx.heading(
            text,
            as_=_as_,
            size=sizel,
            style=self.headstyles
        )

    bt_tittle={
        "font_size":size["normal"],
        'color':'#ffffff',
        'font_family':ft.ft_page['2']
    }
    bt_body={
        "font_size":size["medium"],
        'color':'#ffffff'
    }
    button={
        'width':"100%",
        'height':"100%",
        'display':"block",
        'white_space':'normal',
        'padding':size['small'],
        'border_radius':size['normal'],
        'background_color':'rgba(70,70,70,0.4)',
        'color':cl.colors_text['header'],
    }
    blink={
        "text_decoration":"none",
        'width':"100%",
        'margin':size['zero'],
        'spacing':size['small'],
        "_hover":{}
    }
    links_section={
        'spacing':size['medium'],
        'max_width':max_width,
        'width':'100%'
    }

    '''
    FOOTER VALUES

    -footer values
    -footer style values
    -footer link values
    '''
    footer={
        'color':cl.colors_text['footer'],
        'padding':size['medium'],
        'width':'100%'
    }
    iconstylef={
        'width':size['medium_big'],
        'height':size['medium_big'],
        'margin':size['medium'],
        'padding': '2px',
        '_hover':{
            'border':'2px',
            'border_color':cl.colorsg['withe'],
            'cursor':pointer
        }
    }
    flink={
        "text_decoration":"none",
        "margin_top":size['medium'],
        "_hover":{
            'color':cl.colors_text['footerhover'],
            'cursor':pointer
        }
    }