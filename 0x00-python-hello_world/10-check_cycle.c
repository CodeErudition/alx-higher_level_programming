#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *second = list;

	if (!list)
	{
		return (0);
	}
	while (second && first && first->next)
	{
		second = second->next;
		first = first->next->next;
		if (second == first)
		{
			return (1);
		}
	}
	return (0);
}
