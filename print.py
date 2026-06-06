# =========================================
# ColorFX - Professional Terminal Colors
# Author: Muntahi
# =========================================

# ---------- TEXT FORMATTING ----------
FMTRESET   = "\033[0m"
FMTBOLD    = "\033[1m"
FMTDIM     = "\033[2m"
FMTITALIC  = "\033[3m"
FMTUNDER   = "\033[4m"
FMTBLINK   = "\033[5m"
FMTREVERSE = "\033[7m"
FMTHIDDEN  = "\033[8m"


# ---------- NORMAL TEXT COLORS ----------
CLRBLACK   = "\033[30m"
CLRRED     = "\033[31m"
CLRGREEN   = "\033[32m"
CLRYELLOW  = "\033[33m"
CLRBLUE    = "\033[34m"
CLRMAGENTA = "\033[35m"
CLRCYAN    = "\033[36m"
CLRWHITE   = "\033[37m"


# ---------- BRIGHT TEXT COLORS ----------
CLRBRIGHT_BLACK   = "\033[90m"
CLRBRIGHT_RED     = "\033[91m"
CLRBRIGHT_GREEN   = "\033[92m"
CLRBRIGHT_YELLOW  = "\033[93m"
CLRBRIGHT_BLUE    = "\033[94m"
CLRBRIGHT_MAGENTA = "\033[95m"
CLRBRIGHT_CYAN    = "\033[96m"
CLRBRIGHT_WHITE   = "\033[97m"


# ---------- BACKGROUND COLORS ----------
BG_BLACK   = "\033[40m"
BG_RED     = "\033[41m"
BG_GREEN   = "\033[42m"
BG_YELLOW  = "\033[43m"
BG_BLUE    = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN    = "\033[46m"
BG_WHITE   = "\033[47m"


# ---------- BRIGHT BACKGROUND COLORS ----------
BG_BRIGHT_BLACK   = "\033[100m"
BG_BRIGHT_RED     = "\033[101m"
BG_BRIGHT_GREEN   = "\033[102m"
BG_BRIGHT_YELLOW  = "\033[103m"
BG_BRIGHT_BLUE    = "\033[104m"
BG_BRIGHT_MAGENTA = "\033[105m"
BG_BRIGHT_CYAN    = "\033[106m"
BG_BRIGHT_WHITE   = "\033[107m"


# ---------- CUSTOM MIXED COLORS ----------
CLRBLACK_ON_GREEN   = "\033[30;42m"
CLRWHITE_ON_BLUE    = "\033[37;44m"
CLRBLACK_ON_YELLOW  = "\033[30;43m"
CLRWHITE_ON_RED     = "\033[37;41m"
CLRBRIGHT_ON_BLACK  = "\033[97;40m"


# =========================================
# HELPER FUNCTIONS (OPTIONAL BUT POWERFUL)
# =========================================

def color(text, clr):
    """Apply any color to text"""
    return clr + str(text) + " " + FMTRESET


def bold(text):
    return FMTBOLD + str(text) + FMTRESET


def error(text):
    print( FMTBOLD + CLRRED + "[ERROR]:"+str(text) + FMTRESET)
    return FMTBOLD + CLRRED + str(text) + FMTRESET


def success(text):
    print( FMTBOLD + CLRBRIGHT_GREEN + "[SUCCESS]:"+str(text) + FMTRESET)
    return FMTBOLD + CLRBRIGHT_GREEN + str(text) + FMTRESET


def warning(text):
    print( FMTBOLD + CLRYELLOW + "[WARNING]:"+str(text) + FMTRESET)
    return FMTBOLD + CLRYELLOW + str(text) + FMTRESET


def info(text):
    print( FMTBOLD + CLRCYAN + "[INFORMATION]:"+str(text) + FMTRESET)
    return CLRCYAN + str(text) + FMTRESET


def console(text):
    print( FMTBOLD + CLRBRIGHT_GREEN + "[CONSOLE]:"+str(text) + FMTRESET)
    return FMTBOLD + CLRBRIGHT_GREEN + str(text) + FMTRESET


def banner(text):
    print(CLRBLACK_ON_GREEN + "   " + str(text) + "   " + FMTRESET)
    return CLRBLACK_ON_GREEN + "   " + str(text) + "   " + FMTRESET

import os

def output(text):
    log_text = str(text)

    # Print to terminal
    print(CLRBLACK + BG_WHITE + "   " + log_text + "   " + FMTRESET)

    # Determine serial number
    if os.path.exists("output_log.txt"):
        with open("output_log.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
            serial = len(lines) + 1
    else:
        serial = 1

    # Write to log file with serial number
    with open("output_log.txt", "a", encoding="utf-8") as file:
        file.write(f"{serial}: {log_text}\n")
