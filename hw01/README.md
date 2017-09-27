Douglas wise
Sep 13, 2017
README for hw01 Etch program

Requirements for hw01:
    1. latest image for the beagle bone intalled    done
    2. host computer set up with linux              done
    3. SD cards and cables gathered                 done
    4. git on host                                  done
    5. beagle bone groups joined                    done
    6. Etch-a-sketch program                        done

Etch-a-sketch instructions:
    1. Read README
    2. Run install.sh
            host$ ./install.sh
    3. Run Etch.py
            host$ python Etch.py
    4. follow terminal prompts for game size
    5. instructions on how to play are printed in terminal


// Comment from Prof. Yoder
// README missing
// See README requirements
// I'm having trouble running your python code.  Please demo in class
//  Thanks for the demo
// Grade:  10/10

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
