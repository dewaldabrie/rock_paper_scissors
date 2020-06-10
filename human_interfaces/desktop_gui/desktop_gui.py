import os

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.animation import Animation

from human_interfaces.base import HumanInterfaceBase


class RPSLayout(FloatLayout):

    def __init__(self, *args, engine=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.engine = engine
        self.new_choice = False
        self.choice = None
        self.state = self.engine.state
        self.labels = {}
        self.buttons = {}
        self.images = {}
        self.animations = {}
        self.build()

    def get_move(self):
        self.new_choice = False
        return self.choice

    def sync_widgets_with_game_state(self, *args):
        for widget, attr, func in list(self.labels.values()) + list(self.images.values()) + list(self.buttons.values()):
            if func:
                setattr(widget, attr, func(self.state))

    def show_error(self, err_msg):
        pass

    def animation(self):
        image_ids = ['player1_future_move_image', 'player2_future_move_image']

        def pos_hint_move(pos_hint, x, y):
            p = pos_hint.copy()
            p['x'] += x
            p['y'] += y
            return p

        for image_id in image_ids:
            image = self.images[image_id][0]
            pos_hint_init = image.pos_hint
            mag = 0.02
            dur = 0.2
            anim = Animation(pos_hint=pos_hint_move(image.pos_hint, 0, mag), duration=dur)
            anim += Animation(pos_hint=pos_hint_move(image.pos_hint, 0, -1*mag), duration=dur)
            anim += Animation(pos_hint=pos_hint_move(image.pos_hint, 0, mag), duration=dur)
            anim += Animation(pos_hint=pos_hint_init, duration=dur)
            anim.bind(on_complete=self.sync_widgets_with_game_state)
            anim.start(image)

    def rock(self, button):
        self.choice = 'r'
        self.new_choice = True
        self.state = self.engine.advance()
        self.animation()

    def paper(self, button):
        self.choice = 'p'
        self.new_choice = True
        self.state = self.engine.advance()
        self.animation()

    def scissors(self, button):
        self.choice = 's'
        self.new_choice = True
        self.state = self.engine.advance()
        self.animation()


    def build(self):
        """Build the UI Layout"""

        label_default_kwargs = {
            'color': (0, 0, 0, 1),
            'font_size': 40,
            'size_hint': (0.3, 0.3),
        }
        col1 = 0.05
        col2 = 0.35
        col3 = 0.65
        row1 = 0.7
        row2 = 0.5
        row1b = 0.6
        row4 = 0.4
        row5 = 0.3
        row6 = 0.1
        row7 = 0.0

        images_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')
        init_img_path = os.path.join(images_dir, 'init.jpg')
        blank_img_path = os.path.join(images_dir, 'blank.jpg')
        rock_img_path = os.path.join(images_dir, 'rock.jpg')
        paper_img_path = os.path.join(images_dir, 'paper.jpg')
        scissors_img_path = os.path.join(images_dir, 'scissors.jpg')

        self.img_select = {
            'i': init_img_path,
            'r': rock_img_path,
            'p': paper_img_path,
            's': scissors_img_path
        }

        latest_outcome_select = {
            (1, 0): 'Win!',
            (0, 1): 'Lose!',
            (0, 0): 'Tie!',
        }
        previous_outcome_select = {
            (1, 0): 'Won',
            (0, 1): 'Lost',
            (0, 0): 'Tied',
        }

        def add_player_widgets(player_num, opponent_player_num, col):
            
            self.labels['player%d_total_score_label' % player_num] = (
                Label(text='Total Score',
                      pos_hint={'x': col, 'y': row1b + 0.05},
                      **label_default_kwargs),  # widget object
                None,  # attribute to sync
                None  # function to apply to state for sync value
            )
            self.labels['player%d_total_score_number' % player_num] = (
                Label(text='0',
                      pos_hint={'x': col, 'y': row1b},
                      **label_default_kwargs),
                'text',
                lambda s: str(s['player%d_total_score' % player_num])
            )
            self.labels['player%d_name' % player_num] = (
                Label(text='Player 1',
                      pos_hint={'x': col, 'y': row2},
                      **label_default_kwargs),
                'text',
                lambda s: str(s['player%d_name' % player_num])
            )

            self.images['player%d_future_move_image' % player_num] = (
                Image(source=init_img_path,
                      pos_hint={'x': col, 'y': row4},
                      size_hint=(0.3, 0.3),
                      ),
                'source',
                lambda s: init_img_path
            )
            self.images['player%d_latest_move_image' % player_num] = (
                Image(source=blank_img_path,
                      pos_hint={'x': col, 'y': row5},
                      size_hint=(0.3, 0.3),
                      ),
                'source',
                lambda s: blank_img_path if s['player%d_latest_move' % player_num] is None else self.img_select[s['player%d_latest_move' % player_num]]
            )
            self.images['player%d_previous_move_image' % player_num] = (
                Image(source=blank_img_path ,
                      pos_hint={'x': col, 'y': row6},
                      size_hint=(0.3, 0.3),
                      ),
                'source',
                lambda s: blank_img_path if s['player%d_previous_move' % player_num] is None else self.img_select[s['player%d_previous_move' % player_num]]
            )
            self.labels['player%d_latest_outcome_label' % player_num] = (
                Label(text='',
                      pos_hint={'x': col + 0.1, 'y': row5},
                      **label_default_kwargs),
                'text',
                lambda s: '' if s['player%d_latest_point' % player_num] is None else str(
                    latest_outcome_select[(s['player%d_latest_point' % player_num], s['player%d_latest_point' % opponent_player_num])])
            )
            self.labels['player%d_previous_outcome_label' % player_num] = (
                Label(text='',
                      pos_hint={'x': col + 0.1, 'y': row6},
                      **label_default_kwargs),
                'text',
                lambda s: '' if s['player%d_previous_point' % player_num] is None else str(
                    previous_outcome_select[(s['player%d_previous_point' % player_num], s['player%d_previous_point' % opponent_player_num])])
            )

        add_player_widgets(1, 2, col1)
        add_player_widgets(2, 1, col3)

        self.labels['RPS_label'] = (
            Label(text='RockPaperScissors',
                  pos_hint={'x': col2, 'y': row1 + 0.05},
                  color=(0, 0, 0, 1),
                  font_size=60,
                  size_hint=(0.3, 0.3),
                  bold=True,
                  ),
            None,
            None
        )
        self.labels['num_rounds_label'] = (
            Label(text='Round No.',
                  pos_hint={'x': col2, 'y': row1b + 0.05},
                  **label_default_kwargs),
            None,
            None
        )
        self.labels['num_rounds_number'] = (
            Label(text='0',
                  pos_hint={'x': col2, 'y': row1b},
                  **label_default_kwargs),
            'text',
            lambda s: str(s['num_rounds'])
        )

        button_default_kwargs = {
            'color': (0, 0, 0, 1),
            'font_size': 40,
            'background_color': (0.8, 0.9, 1.0, 1),
            'size_hint': (0.15, 0.15),
        }
        button_background_color_active = (0.6, 0.7, 0.8, 1)
        self.buttons['rock'] = (
            Button(text='Rock',
                   **button_default_kwargs,
                   pos_hint={'x': col1, 'y': row7},
                   on_press=self.rock,
                   ),
            'background_color',
            lambda s: button_background_color_active
            if s['player1_latest_move'] == 'r'
            else button_default_kwargs['background_color']
        )
        self.buttons['paper'] = (
            Button(text='Paper',
                   **button_default_kwargs,
                   pos_hint={'x': col1 + 0.15, 'y': row7},
                   on_press=self.paper,
                   ),
            'background_color',
            lambda s: button_background_color_active
            if s['player1_latest_move'] == 'p'
            else button_default_kwargs['background_color']
        )
        self.buttons['scissors'] = (
            Button(text='Scissors',
                   **button_default_kwargs,
                   pos_hint={'x': col1 + 0.3, 'y': row7},
                   on_press=self.scissors,
                   ),
            'background_color',
            lambda s: button_background_color_active
            if s['player1_latest_move'] == 's'
            else button_default_kwargs['background_color']
        )

        self.sync_widgets_with_game_state()

        # add widgets to layout
        for item, _, _ in list(self.labels.values()) + list(self.images.values()) + list(self.buttons.values()):
            self.add_widget(item)

        # white canvas
        Window.clearcolor = (1, 1, 1, 1)

class KiviApp(App):
    title = 'Paper Rock Scissors'

    def __init__(self, engine=None, **kwargs):
        super().__init__(**kwargs)
        self.layout = RPSLayout(engine=engine)

    def build(self):
        return self.layout

class RPSGUI(HumanInterfaceBase):

    def __init__(self, engine=None, player1_class=None, player2_class=None):
        super().__init__(engine=engine, player1_class=player1_class, player2_class=player2_class)
        self.app = KiviApp(engine=self.engine)

    def get_move(self):
        return self.app.layout.get_move()

    def show_error(self, err_msg):
        pass  # TODO: implement this for completeness sake

    def update(self):
        self.app.layout.update()

    def run(self):
        self.app.run()



