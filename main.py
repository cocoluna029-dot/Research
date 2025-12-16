from kivy.resources import resource_add_path
import os
import sys
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import SoundLoader
from kivy.lang import Builder


class StartScreen(Screen):
    pass

class ZWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/zoo.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")

class YWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/yak.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")

class XWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/x-ray.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")


class WWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/wig.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")


class VWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/van.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")

class UWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/urn.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")


class TWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/toy.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")


class SWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/sun.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")

class RWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/rat.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")


class QWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/queen.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")


class PWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/pen.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")

class OWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/old.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")

class NWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/net.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")

class MWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/map.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")

class LWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/leg.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")

class KWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/keg.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")

class JWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/jar.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")

class IWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/ink.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")

class HWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/hat.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")

class GWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/gun.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")

class FWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/fan.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")

class EWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/egg.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")

class DWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/dog.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")

class CWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/cat.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")

class BWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/bat.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")

class EyWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/ant.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")

class YaWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/yoyo.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")


class WaWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/wala.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")

class UuWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/unan.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")


class TaWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/tasa.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")


class SaWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/susi.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")


class RaWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/relo.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")


class PaWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/pala.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")


class OoWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/oso.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")


class NaWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/nota.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")


class MaWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/mata.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")


class LaWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/laso.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")


class IiWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/isda.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")


class HaWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/hari.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")


class GaWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/guro.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")


class EeWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/ekis.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")


class DaWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/daga.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")


class KaWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/kama.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")


class BaWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/bata.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")

class AWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/aso.wav')
        if sound:
            sound.play()
        else:
            print("Audio file missing.")

class TenWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/ten.wav')
        if sound:
            sound.play()

class NineWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/nine.wav')
        if sound:
            sound.play()

class EightWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/eight.wav')
        if sound:
            sound.play()

class SevenWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/seven.wav')
        if sound:
            sound.play()

class SixWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/six.wav')
        if sound:
            sound.play()

class FiveWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/five.wav')
        if sound:
            sound.play()

class FourWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/four.wav')
        if sound:
            sound.play()

class ThreeWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/three.wav')
        if sound:
            sound.play()

class TwoWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/two.wav')
        if sound:
            sound.play()

class OneWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/one.wav')
        if sound:
            sound.play()

class SampuWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/sampu.wav')
        if sound:
            sound.play()
        else:
            print("Audio file not found.")

class SiyamWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/siyam.wav')
        if sound:
            sound.play()

class WaloWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/walo.wav')
        if sound:
            sound.play()

class PitoWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/pito.wav')
        if sound:
            sound.play()

class AnimWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/anim.wav')
        if sound:
            sound.play()

class LimaWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/lima.wav')
        if sound:
            sound.play()

class ApatWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/apat.wav')
        if sound:
            sound.play()

class TatloWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/tatlo.wav')
        if sound:
            sound.play()

class DalawaWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/dalawa.wav')
        if sound:
            sound.play()

class IsaWindow(Screen):
    def play_audio(self):
        sound = SoundLoader.load('audio/isa.wav')
        if sound:
            sound.play()

class AlpabetoNextWindow(Screen):
    pass

class AlpabetoWindow(Screen):
    pass

class BilangWindow(Screen):
    pass

class NumbersWindow(Screen):
    pass

class AlphabetWindow(Screen):
    pass

class FilipinoWindow(Screen):
    pass

class EnglishWindow(Screen):
    pass

class HomeWindow(Screen):
    pass

class AlphabetNextWindow(Screen):
    pass



class MyApp(App):
    def build(self):
        Builder.load_file("main.kv")
        sm = ScreenManager()

        sm.add_widget(StartScreen(name='start'))

        sm.add_widget(HomeWindow(name='home'))

        sm.add_widget(FilipinoWindow(name='filipino'))

        sm.add_widget(AlpabetoWindow(name='alpabeto'))

        sm.add_widget(AWindow(name='a'))
        sm.add_widget(BaWindow(name='ba'))
        sm.add_widget(KaWindow(name='ka'))
        sm.add_widget(DaWindow(name='da'))
        sm.add_widget(EeWindow(name='ee'))
        sm.add_widget(GaWindow(name='ga'))
        sm.add_widget(HaWindow(name='ha'))
        sm.add_widget(IiWindow(name='ii'))
        sm.add_widget(LaWindow(name='la'))
        sm.add_widget(MaWindow(name='ma'))

        sm.add_widget(AlpabetoNextWindow(name='alpabeto_next'))

        sm.add_widget(NaWindow(name='na'))
        sm.add_widget(OoWindow(name='oo'))
        sm.add_widget(PaWindow(name='pa'))
        sm.add_widget(RaWindow(name='ra'))
        sm.add_widget(SaWindow(name='sa'))
        sm.add_widget(TaWindow(name='ta'))
        sm.add_widget(UuWindow(name='uu'))
        sm.add_widget(WaWindow(name='wa'))
        sm.add_widget(YaWindow(name='ya'))

        sm.add_widget(EnglishWindow(name='english'))

        sm.add_widget(AlphabetWindow(name='alphabet'))

        sm.add_widget(EyWindow(name='ey'))
        sm.add_widget(BWindow(name='b'))
        sm.add_widget(CWindow(name='c'))
        sm.add_widget(DWindow(name='d'))
        sm.add_widget(EWindow(name='e'))
        sm.add_widget(FWindow(name='f'))
        sm.add_widget(GWindow(name='g'))
        sm.add_widget(HWindow(name='h'))
        sm.add_widget(IWindow(name='i'))
        sm.add_widget(JWindow(name='j'))
        sm.add_widget(KWindow(name='k'))
        sm.add_widget(LWindow(name='l'))
        sm.add_widget(MWindow(name='m'))

        sm.add_widget(AlphabetNextWindow(name='alphabet_next'))

        sm.add_widget(NWindow(name='n'))
        sm.add_widget(OWindow(name='o'))
        sm.add_widget(PWindow(name='p'))
        sm.add_widget(QWindow(name='q'))
        sm.add_widget(RWindow(name='r'))
        sm.add_widget(SWindow(name='s'))
        sm.add_widget(TWindow(name='t'))
        sm.add_widget(UWindow(name='u'))
        sm.add_widget(VWindow(name='v'))
        sm.add_widget(WWindow(name='w'))
        sm.add_widget(XWindow(name='x'))
        sm.add_widget(YWindow(name='y'))
        sm.add_widget(ZWindow(name='z'))

        sm.add_widget(NumbersWindow(name='numbers'))

        sm.add_widget(TenWindow(name='ten'))
        sm.add_widget(NineWindow(name='nine'))
        sm.add_widget(EightWindow(name='eight'))
        sm.add_widget(SevenWindow(name='seven'))
        sm.add_widget(SixWindow(name='six'))
        sm.add_widget(FiveWindow(name='five'))
        sm.add_widget(FourWindow(name='four'))
        sm.add_widget(ThreeWindow(name='three'))
        sm.add_widget(TwoWindow(name='two'))
        sm.add_widget(OneWindow(name='one'))

        sm.add_widget(BilangWindow(name='bilang'))

        sm.add_widget(SampuWindow(name='sampu'))
        sm.add_widget(SiyamWindow(name='siyam'))
        sm.add_widget(WaloWindow(name='walo'))
        sm.add_widget(PitoWindow(name='pito'))
        sm.add_widget(AnimWindow(name='anim'))
        sm.add_widget(LimaWindow(name='lima'))
        sm.add_widget(ApatWindow(name='apat'))
        sm.add_widget(TatloWindow(name='tatlo'))
        sm.add_widget(DalawaWindow(name='dalawa'))
        sm.add_widget(IsaWindow(name='isa'))
        return sm

if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(sys._MEIPASS)
    else:
        resource_add_path(os.path.abspath('.'))
    MyApp().run()
