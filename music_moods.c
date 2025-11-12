#include <stdio.h>
#include <string.h>
#include <ctype.h>

struct music
{
    char name[100];
    char singer[100];
    char mood[100];
};

void toLowerCase(char str[])
{
    for(int i=0; str[i]; i++)
    {
        str[i] = tolower(str[i]);
    }
}

int main()
{
    struct music songs[] =
    {
        {"PHIR SE UD CHALA", "By-MOHIT CHAUHAN", "happy"},
        {"ILAHI", "By-ARIJIT SINGH", "happy"},
        {"ON TOP OF THE WORLD", "By-IMAGINE DRAGONS", "happy"},
        
        {"CHANNA MEREYA", "By-ARIJIT SINGH", "sad"},
        {"TUJHE KITNA CHAHNE LAGE", "By-ARIJIT SINGH", "sad"},
        {"FIX YOU", "By-COLDPLAY", "sad"},
        
        {"LET IT BE", "By-THE BEATLES", "calm"},
        {"PERFECT", "By-ED SHEERAN", "calm"},
        {"KHARIYAT", "By-ARIJIT SINGH", "calm"},

        {"TUM HI HO", "By-ARIJIT SINGH", "romantic"},
        {"RAABTA", "By-ARIJIT SINGH", "romantic"},
        {"PEHLA NASHA", "By-UDIT NARAYAN", "romantic"},

        {"ZINDA", "By-SIDDHARTH MAHADEVAN", "energetic"},
        {"BELIEVER", "By-IMAGINE DRAGONS", "energetic"},
        {"LAKSHYA", "By-SHANKAR MAHADEVAN", "energetic"},

        {"KAR HAR MAIDAAN FATEH", "By-SHREYA GHOSHAL & SUKHWINDER SINGH", "motivational"},
        {"AASHAYEIN", "By-KK", "motivational"},
        {"HALL OF FAME", "By-THE SCRIPT", "motivational"},

        {"JO BHEJI THI DUAA", "By-NANDINI SRIKAR", "lonely"},
        {"SHAYAD", "By-ARIJIT SINGH", "lonely"},
        {"SOMEONE LIKE YOU", "By-ADELE", "lonely"},
    };

    int total = sizeof(songs) / sizeof(songs[0]);
    char moodinput[100];

    printf("\nWelcome!!\n\n");
    printf("MOOD BASED MUSIC SUGGESTION PROJECT\n");
    printf("How are you feeling today?😇\n");

    fgets(moodinput, sizeof(moodinput), stdin);
    moodinput[strcspn(moodinput, "\n")] = '\0';
    toLowerCase(moodinput);

    if(strstr(moodinput,"happy😄")||strstr(moodinput,"excited😄")||strstr(moodinput,"joyful😄")||strstr(moodinput,"jolly😄")||strstr(moodinput,"cheerful😄"))
        strcpy(moodinput,"happy😄");
    else if(strstr(moodinput,"sad🥺")||strstr(moodinput,"unhappy🥺")||strstr(moodinput,"sorrowful🥺")||strstr(moodinput,"downcast🥺"))
        strcpy(moodinput,"sad🥺");
    else if(strstr(moodinput,"angry😠")||strstr(moodinput,"mad😠")||strstr(moodinput,"irritated😠")||strstr(moodinput,"annoyed😠")||strstr(moodinput,"furious😠"))
        strcpy(moodinput,"angry😠");
    else if(strstr(moodinput,"relaxed😌")||strstr(moodinput,"calm😌")||strstr(moodinput,"peaceful😌"))
        strcpy(moodinput,"calm😌");
    else if(strstr(moodinput,"lonely💔"))
        strcpy(moodinput,"lonely💔");
    else if(strstr(moodinput,"romantic🥰"))
        strcpy(moodinput,"romantic🥰");
    else if(strstr(moodinput,"energetic🤩"))
        strcpy(moodinput,"energetic🤩");
    else if(strstr(moodinput,"motivated😎")||strstr(moodinput,"motivational😎")||strstr(moodinput,"inspired😎"))
        strcpy(moodinput,"motivational😎");

    printf("\nTHE DETECTED MOOD IS: %s\n", moodinput);
    printf("\nHere are some mood-based song suggestions:\n");

    int detect = 0;
    for(int i=0; i<total; i++)
    {
        if(strcmp(songs[i].mood, moodinput)==0)
        {
            printf("%s - %s\n", songs[i].name, songs[i].singer);
            detect = 1;
        }
    }

    if(!detect)
    {
        printf("\nSORRY!\nNo songs found for this mood.\nTry using simple words like happy, sad, angry, calm, etc.\n");
    }

    printf("\n\nTHANK YOU FOR USING OUR PROGRAM!🥰\n");

    return 0;
}