label start:


    $ anticheat = persistent.anticheat


    $ chapter = 0



    $ s_name = "Сайорі"
    $ m_name = "Моніка"
    $ n_name = "Нацукі"
    $ y_name = "Юрі"

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ in_sayori_kill = None
    $ allow_skipping = True
    $ config.allow_skipping = True
    $ _dismiss_pause = config.developer

    if persistent.playthrough == 0:
        $ settingsstart = True
        $ playerlow = player.lower()
        $ player_p = player[0]
        call script_exitmusic from _call_script_exitmusic

    return

label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return

label restart:
    $ renpy.full_restart()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
