// Comment from Prof. Yoder
// README missing
// See README requirements
// I'm having trouble running your python code.  Please demo in class
// Grade:  3/10

python Etch.py 
ALSA lib pcm_hw.c:1713:(_snd_pcm_hw_open) Invalid value for card
Game Size: 10
Traceback (most recent call last):
  File "Etch.py", line 10, in <module>
    screen = pygame.display.set_mode((size*100,size*100))
pygame.error: Unable to open a console terminal
debian@bone-0834:~/studentWork/wise/hw01$ sudo python Etch.py 
sudo: unable to resolve host bone-0834
ALSA lib confmisc.c:767:(parse_card) cannot find card '0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_card_driver returned error: No such file or directory
ALSA lib confmisc.c:392:(snd_func_concat) error evaluating strings
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_concat returned error: No such file or directory
ALSA lib confmisc.c:1246:(snd_func_refer) error evaluating name
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM default
Game Size: 10
Traceback (most recent call last):
  File "Etch.py", line 10, in <module>
    screen = pygame.display.set_mode((size*100,size*100))
pygame.error: No video mode large enough for 1000x1000
