import raylibpy as rl

# 1-Initialize screen parameters by using rl.init_window
screen_width = 800
screen_height = 450

rl.init_window(screen_width, screen_height, "raylib [audio] example - sound loading and playing")

# 2- Initialize audio device by using rl.init_audio_device

rl.init_audio_device()  
# 3- create variables to load the wav files using rl.load_sound
# 4- set the game timing per frames per second(fps) rl.set_target_fps

fx_wav = rl.load_sound("resources/D&B Kick 02.wav")  # Load WAV audio file
fx_ogg = rl.load_sound("resources/D&B Open Hat 01.wav")  # Load OGG audio file

rl.set_target_fps(60)  # Set our game to run at 60 frames per second

# 5- Initialize the Main game loop
while not rl.window_should_close():  # Detect window close button or ESC key
    # Update
    if rl.is_key_pressed(rl.KEY_SPACE):
        rl.play_sound(fx_wav)  # Play WAV sound
    if rl.is_key_pressed(rl.KEY_ENTER):
        rl.play_sound(fx_ogg)  # Play OGG sound

    # 6- Initialise the draw of the window
    rl.begin_drawing()
    #7- set the colour
    rl.clear_background(rl.RAYWHITE)
    #8- Add texts and colour to window
    rl.draw_text("Press SPACE to PLAY the WAV sound!", 200, 180, 20, rl.LIGHTGRAY)
    rl.draw_text("Press ENTER to PLAY the OGG sound!", 200, 220, 20, rl.LIGHTGRAY)
    
    rl.end_drawing()

# 9- De-Initialization when window is closed
rl.unload_sound(fx_wav)  # Unload sound data
rl.unload_sound(fx_ogg)  # Unload sound data

rl.close_audio_device()  # Close audio device

rl.close_window()  # Close window and OpenGL context
