#ifndef SOUND_MANAGER_H
#define SOUND_MANAGER_H

#include <SDL2/SDL_mixer.h>
#include <string>

class SoundManager {
public:
    SoundManager();
    ~SoundManager();

    void playEatSound();
    void playGameOverSound();
    void playBackgroundMusic();

private:
    Mix_Chunk* eatSound;
    Mix_Chunk* gameOverSound;
    Mix_Music* backgroundMusic;
};

#endif