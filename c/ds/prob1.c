/*
Find if a string contains all unique characters.
*/

#include <stdio.h>
#include <string.h>


enum bool {
    false = 0,
    true = 1
};


enum bool unique_chars1(char * str)
{
    for (int c1 = 0; c1 < strlen(str); c1++)
    {
        for (int c2 = 1; c2 < strlen(str) - 1; c2++)
        {
            if (c1 != c2 && str[c1] == str[c2])
            {
                return false;
            }
        }
    }

    return true;
}


void string_sort(char * str)
{
    int len = strlen(str);
    for (int c1 = 0; c1 < len - 1; c1++)
    {
        for (int c2 = c1 + 1; c2 < len; c2++)
        {
            if (str[c1] > str[c2])
            {
                char temp = str[c1];
                str[c1] = str[c2];
                str[c2] = temp;
            }
        }
    }
}


enum bool unique_chars(char * str)
{
    string_sort(str);

    for (int i = 0; i < strlen(str) - 1; i++)
    {
        if (str[i] == str[i + 1])
        {
            return false;
        }
    }

    return true;
}


int main(int argc, char** argv)
{
    char stack_allocated_str[] = "Hello!";

    if (unique_chars(stack_allocated_str))
    {
        printf("true\n");
    }
    else
    {
        printf("false\n");
    }
}
