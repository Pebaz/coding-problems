#include <stdio.h>
#include <set>

int main()
{
    std::set<int> nums;

    nums.insert(25);
    nums.insert(200);
    nums.insert(201);
    nums.insert(255);

    std::set<int>::iterator inside = nums.find(200);

    if (inside != nums.end())
    {
        printf("%i", *inside);
    }
}
