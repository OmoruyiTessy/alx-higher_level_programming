#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: stingly-linked list.
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tessy, *hessy;

	if (list == NULL || list->next == NULL)
		return (0);
	tessy = list->next;
	hessy = list->next->next;

	while (tessy && hessy && hessy->next)
	{
		tessy = tessy->next;
		hessy = hessy->next->next;

		if (tessy == hessy)
		{
			return (1);
		}
	}
	return (0);
}
