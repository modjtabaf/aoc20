
#include <stdio.h>

#if 0
static int init[] = {3, 8, 9, 1, 2, 5, 4, 6, 7};
#else
static int init[] = {2, 5, 3, 1, 4, 9, 8, 6, 7};
#endif

#define SIZE 1000000//9//
#define NMOVES 10000000//10//

struct Cup
{
  int value;
  Cup *next;
};

Cup data[SIZE];

int main()
{
  Cup *curr = data;
  Cup *prev = &data[SIZE-1];
  for(int i=1; i <= SIZE; i++, curr++)
  {
    curr->value = i;
    prev->next = curr;
    prev = curr;
  }

  for (int i=0; i < 9; i++)
    data[i].value = init[i];

  curr = &data[0];

  for (int i=0; i < NMOVES; i++)
  {
    if (i % 1000 == 0)
      printf("%d\n", i);

    Cup *picked = curr->next;
    curr->next = curr->next->next->next->next;

    int destv = curr->value - 1;
    while (
      destv == 0 ||
      destv == picked->value ||
      destv == picked->next->value ||
      destv == picked->next->next->value)
    {
      if (destv == 0)
        destv = SIZE;
      else
        destv -= 1;
    }

    Cup *dest;
    if (destv < 10)
    {
      dest = data;
      while(dest->value != destv)
        dest++;
    }
    else
      dest = &data[destv-1];
    
    Cup *foo = dest->next;
    dest->next = picked;
    picked->next->next->next = foo;

    curr = curr->next;
  }

  Cup *p = data;
  while(p->value != 1)
    p++;
  printf("%d * %d = %lld\n", p->next->value, p->next->next->value, (long long)p->next->value*(long long)p->next->next->value);

  return 0;
}
