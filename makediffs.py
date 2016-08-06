# I have modified the game .exe by directly changing assembly instructions in OllyDbg
# this script just turned those modifications into a small portable patch file and it isn't used anywhere during
# the execution of reternal.py

import bsdiff4

# patch 1: this hooks the execution and updates resolution in memory
bsdiff4.file_diff("Eternal Daughter.exe", "fixres1.exe", "patch1")

# patch 2: this changes the resolution only when the window is drawn;
#          as a result, the game isn't upscaled but you also don't get artifacts on smaller levels
bsdiff4.file_diff("Eternal Daughter.exe", "fixres2.exe", "patch2")