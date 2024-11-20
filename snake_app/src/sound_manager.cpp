#include "sound_manager.h"
#include <iostream>

SoundManager::SoundManager() {
    if (Mix_OpenAudio(44100, MIX_DEFAULT_FORMAT, 2, 2048) < 0) {
        std::cerr << "Failed to initialize SDL_mixer: " << Mix_GetError() << std::endl;
        exit(1);
    }

    eatSound = Mix_LoadWAV("assets/eat_sound.mp3");
    gameOverSound = Mix_LoadWAV("assets/game_over.mp3");
    backgroundMusic = Mix_LoadMUS("assets/music.mp3");

    if (!eatSound || !gameOverSound || !backgroundMusic) {
        std::cerr << "Failed to load sounds: " << Mix_GetError() << std::endl;
        exit(1);
    }

    std::cout << "SoundManager initialized successfully." << std::endl;
}

SoundManager::~SoundManager() {
    Mix_FreeChunk(eatSound);
    Mix_FreeChunk(gameOverSound);
    Mix_FreeMusic(backgroundMusic);
    Mix_CloseAudio();
    std::cout << "SoundManager cleaned up successfully." << std::endl;
}